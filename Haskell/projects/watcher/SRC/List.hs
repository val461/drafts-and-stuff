module SRC.List
( deleteAt
, pickAmong
, several
) where

import System.Random (StdGen, randomR)

{-
conditionalEdition :: (a -> a) -> (a -> Bool) -> a -> a
conditionalEdition editor p x =
    if p x
    then editor x
    else id x

deleteAtIf p index = conditionalEdition (deleteAt index) p
-}

deleteAt :: (Num a, Ord a) => a -> [b] -> [b]
-- delete an element at a given index from a given list
deleteAt _ [] = []
deleteAt 0 (x:xs) = xs
deleteAt i (x:xs) | i > 0 = x : deleteAt (i - 1) xs


pickAmong :: [a] -> StdGen -> (a, [a], StdGen)
-- returns a randomly chosen element of the list,
-- the list without said element, and a new random generator
pickAmong list gen =    let
                            min = 0
                            max = length list
                            (randIndex, newGen) = randomR (min, max - 1) gen
                            rand = list !! randIndex
                            newList = deleteAt randIndex list
                        in
                            (rand, newList, newGen)

randomize :: [a] -> StdGen -> ([a], StdGen)
-- “sort” randomly
randomize [] gen = ([], gen)
randomize xs gen =  let
                        (rand, rest, gen2) = pickAmong all gen
                        (rands, gen3) = randomize rest gen2
                    in
                        (rand : rands, gen3)

several :: [a] -> Bool
several elements = length elements >= 2
