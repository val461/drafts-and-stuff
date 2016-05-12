module SRC.Load
( Antecedent
, Image
, Correspondence
, parse
, loadCorrespondences
, loadCorrespondence
) where

import qualified Data.List.Split as S
import qualified SRC.File as F

type Image = String
type Antecedent = String
type Correspondence = ([Antecedent], Image)


parse :: Int -> String -> [Correspondence]
--parse minAmountOfAntecedents contents = foldr (\ x xs -> handleResults (parseLine minAmountOfAntecedents x) xs) [] (lines contents)
parse minAmountOfAntecedents contents = foldr process [] (lines contents)
    where
        process x xs =
            case parseLine minAmountOfAntecedents x of
                Nothing -> xs
                Just parsed -> parsed : xs
        parseLine minAmountOfAntecedents line =
            case (S.splitOn separator line) of
                []  -> Nothing
                image : antecedents ->  if (minAmountOfAntecedents <= length antecedents)
                                        then Just (antecedents, image)
                                        else Nothing
        -- syntactical delimiter of the elements of a line:
        separator = "|"


loadCorrespondence :: [F.RegularFile] -> Int -> Int -> [Correspondence] -> IO [Correspondence]
loadCorrespondence files minAmountOfAntecedents level correspondences = do
    let file = files !! (level - 1)
    contents <- readFile file
    let newCorrespondences = correspondences ++ (parse minAmountOfAntecedents contents)
    return newCorrespondences


loadCorrespondences :: [FilePath] -> Int -> [Int] -> [Correspondence] -> IO [Correspondence]
loadCorrespondences files minAmountOfAntecedents [] correspondences = return correspondences
loadCorrespondences files minAmountOfAntecedents (level : levels) correspondences = do
    newCorrespondences <- loadCorrespondence files minAmountOfAntecedents level correspondences
    loadCorrespondences files minAmountOfAntecedents levels newCorrespondences

