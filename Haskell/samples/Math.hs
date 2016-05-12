module SRC.Math (roundTo) where


roundTo :: (Integral int1, Integral int2) => int1 -> Double -> Either int2 Double
roundTo digitsAfterComma value
    | (digitsAfterComma >= 1) =
        let
            factor = fromIntegral (10 ^ digitsAfterComma)
            result = ((/ factor) . fromIntegral . round . (* factor)) value
        in
            Right result
    | (digitsAfterComma == 0) = Left (round value)
    | otherwise = error "minimal precision must be non-negative"



