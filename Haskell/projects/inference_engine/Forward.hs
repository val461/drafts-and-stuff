-- Knowledge -> Question -> Answer

question = "color(x)"
answer x = color x

data Thing = Grass | Leaf | Blood | Mars | Water
    deriving (Eq, Show)

color :: Thing -> String
color x | green x = "green"
        | red x = "red"
        | otherwise = "blue"

green x | isGrass x = True
        | isLeaf x = True
        | otherwise = False

red x   | isBlood x = True
        | isMars x = True
        | otherwise = False

isGrass = (== Grass)
isLeaf = (== Leaf)
isBlood = (== Blood)
isMars = (== Mars)
isWater = (== Water)
