import qualified Data.List as L

dropLast = doOnLast drop
takeLast = doOnLast take
dropLastWhile = doOnLast dropWhile
doOnLast doOnFirst n = reverse . doOnFirst n . reverse


data ExactFloat = EF {getDigits :: Integer, getExponent :: Integer}

base :: Num a => a
base = 10
toFl (EF s e) = (fromInteger s) * (base^^e)

instance Num ExactFloat where
    (+) (EF a_s a_e) (EF b_s b_e) =
        let
            c_e = min a_e b_e
            c_s = a_s*(base^(a_e - c_e)) + b_s*(base^(b_e - c_e))
        in
            EF c_s c_e

    (*) (EF a_s a_e) (EF b_s b_e) =
        let
            c_s = a_s * b_s
            c_e = a_e + b_e
        in
            EF c_s c_e

    abs (EF s e) = EF (abs s) e
    signum (EF s e) = fromInteger (signum s)
    fromInteger a = EF a 0
    negate (EF s e) = EF (negate s) e

instance Show ExactFloat where
    show (EF s e) =
        let
            digits_str = show s
            (int_part, frac_part) = getParts digits_str e
            result = int_part ++ "." ++ frac_part
-- 24 * 10^-1 = 2.4
-- 24 * 10^-2 = 0.24
-- 24 * 10^-3 = 0.024

            getParts s e    | e < 0 =
                                let
                                    abs_e = fromInteger (abs e)
                                in
                                    if abs_e < length s
                                    then (dropLast abs_e s, takeLast abs_e s)
                                    else ("0", (L.genericReplicate (abs_e - length s) '0') ++ s)
                            | otherwise = (s ++ (L.genericReplicate e '0'), "0")
        in
            result

instance Read ExactFloat where
    readsPrec _ text@[] = [(fromInteger 0, text)]
    readsPrec _ text =
        let
            (int_part_str, frac_part_str) = splitOn '.' text
            frac_part_str_cleaned = dropLastWhile (== '0') frac_part_str
            s_str = int_part_str ++ frac_part_str_cleaned
            s = read s_str
            e = fromIntegral (0 - (length frac_part_str_cleaned))
            toDrop = (length int_part_str) + 1 + (length frac_part_str)
            splitOn c xs =
                let
                    (before, rest) = break (== c) xs
                    after = case rest of
                                _ : digits -> digits
                                [] -> []
                in
                    (before, after)
        in
            [(EF s e, drop toDrop text)]

-- Example:

a,b :: ExactFloat
a = read "23.2564"
b = read "1.0000000000000000000000000000000001"
c = a + b
