data Color = Color { red :: Int, green :: Int, blue :: Int } deriving Show

c1 = newColor 230 20 13
c2 = newColor 100 200 240
res = c1 + c2
res2 = abs c1
res3 = abs c2
res4 = signum c1
res5 = signum c2
res6 = fromInteger 24 :: Color
res7 = negate c1


newColor r g b =
    let
        valid_r = makeValid r
        valid_g = makeValid g
        valid_b = makeValid b
    in
        Color valid_r valid_g valid_b

makeValid v |   v > 255 = 255
            |   v <   0 = 0
            | otherwise = v

negOne v = makeValid (255 - v)

instance Num Color where
    (+) (Color r1 g1 b1) (Color r2 g2 b2) =
        let
            r = middle r1 r2
            g = middle g1 g2
            b = middle b1 b2

            middle a b = truncate ((fromIntegral (a + b)) / 2)
        in
            Color r g b

    (*) (Color r1 g1 b1) (Color r2 g2 b2) = undefined

    abs c@(Color r g b) =
        let
            Color sr sg sb = signum c

            new_r = absOne r sr
            new_g = absOne g sg
            new_b = absOne b sb

            absOne v 0 = negOne v
            absOne v _ = v
        in
            Color new_r new_g new_b

    signum (Color r g b) =
        let
            new_r = sign r
            new_g = sign g
            new_b = sign b

            sign v  | v > 191   = 255
                    | v <  64   =   0
                    | otherwise = 127
        in
            Color new_r new_g new_b

    fromInteger n =
        let
            v = fromInteger n
        in
            Color v v v

    negate (Color r g b) =
        let
            new_r = negOne r
            new_g = negOne g
            new_b = negOne b
        in
            Color new_r new_g new_b
