module SRC.Game
( play
, tellScore
, menu_endOfLevel
, loadLevel
, askLevel
, askLevels
, askLevelsFacultative
, launch
) where

import qualified Data.List

import qualified SRC.File as F
import qualified SRC.Interaction as I
import qualified SRC.Load as Ld
import qualified SRC.List as L

import System.Random (StdGen)
import SRC.Load (Correspondence)

import Control.Monad (when)
import SRC.List (several)

{-todo:
Currently, a menu lets the user choose the folder, and another menu lets
him choose files within this folder.
The user shouldn't be limited to choosing files of only one folder.
Therefore, those two menus should be merged into one.
Also, an option for forgetting loaded levels, as well as an option to select all levels in the folder, and an option to unselect a level at a time, should be
in this new menu.
-}


play :: (Num a, Ord a, Show a) => [Correspondence] -> a -> a -> StdGen -> IO ((a, a), StdGen)
play [] mistakesCount total gen = return ((mistakesCount, total), gen)
play all mistakesCount total gen = do
        putStrLn (show (length all) ++ " remaining.\n")
        let
            (rand, newAll, newGen) = L.pickAmong all gen
            (antecedents, image) = rand
        putStrLn image
        answer <- getLine
        if answer `elem` antecedents
        then do
            putStr ("Good answer! ")
            play newAll mistakesCount (total + 1) newGen
        else do
            putStrLn (badAnswerMessage antecedents)
            play all (mistakesCount + 1) (total + 1) newGen
    where
        badAnswerMessage [] = ("Error: no answers were read from the file for this qustion.")
        badAnswerMessage (goodAnswer:[]) = ("The answer was: " ++ goodAnswer)
        badAnswerMessage goodAnswers = ("The accepted answers were:\n" ++ (snd $ I.display 1 goodAnswers))

tellScore (mistakesCount, total) = do
    let
        count = total - mistakesCount
        floatCount = fromIntegral (count)
        floatTotal = fromIntegral total
    when (floatTotal > 0)
        (
        do
            let accuracy = floatCount / floatTotal
            putStrLn ("\nAccuracy: " ++ (I.showPercentage accuracy) ++ " (" ++ (show count) ++ "/" ++ (show total) ++ ")")
            case accuracy of
                x   | x < 1.00  -> putStrLn "You should restart this level."
                    | otherwise -> putStrLn "Perfect!"
        )

data Action = Exit | ChangeLevel | ChangeGame

menu_endOfLevel :: [Correspondence] -> StdGen -> IO (Action, StdGen)
menu_endOfLevel all gen = do
    putStrLn "r + [enter]: restart this level"
    putStrLn "    [enter]: back to level selection menu"
    putStrLn "g + [enter]: back to  game selection menu"
    putStrLn "x + [enter]: exit"
    answer <- getLine
    case answer of
        "r" -> do
                (score, newGen) <- play all 0 0 gen
                tellScore score
                menu_endOfLevel all newGen
        ""  -> return (ChangeLevel, gen)
        "x" -> return (Exit, gen)
        "g" -> return (ChangeGame, gen)
        _   -> do
                putStrLn "Answer not understood."
                menu_endOfLevel all gen


askLevel defaultLevel levels =
    if (several levels)
    then do
        result <- I.selectionMenu "Levels:\n" ("\nPlease select a level (default: " ++ (show defaultLevel) ++ ").") levels
        case result of
            Just n  -> return n
            Nothing -> return defaultLevel
    else 
        return defaultLevel

askLevelsFacultative levels chosen = do
    result <- I.selectionMenu "Levels:\n" "Load one more level or press directly [enter] to play." levels
    case result of
        Just n  -> askLevelsFacultative levels (n : chosen)
        Nothing -> return chosen

askLevels :: [Int] -> [FilePath] -> IO [Int]
askLevels defaultLevels levels = do
        if (several levels)
        then do
            let msg = case defaultLevels of
                        x:[] -> ("\nPlease select a level to load (default: " ++ (show x) ++ ").\n")
                        _    -> "\nPlease select a level to load.\n"
            result <- I.selectionMenu "Levels:\n" msg levels
            case result of
                Just n  -> askLevelsFacultative levels [n]
                Nothing -> return defaultLevels
        else return defaultLevels

loadLevel :: [FilePath] -> StdGen -> IO (Bool, StdGen)
loadLevel [] gen = do
    putStrLn "Error: no level files."
    return (False, gen)
loadLevel files gen = do
    levels <- askLevels [1] files
    all <- Ld.loadCorrespondences files 1 levels []
    (score, gen2) <- play all 0 0 gen
    tellScore score
    (nextAction, gen3) <- menu_endOfLevel all gen2
    case nextAction of
        ChangeLevel ->  loadLevel files gen3
{-        ChangeLevel ->  if (length files >= 2)
                        then loadLevel files gen3
                        else return (True, gen3)-}
        ChangeGame  -> return (True,  gen3)
        Exit        -> return (False, gen3)


launch :: F.Folder -> StdGen -> IO ()
launch gamesFolder gen = do
    (folder, files) <- I.askFolderHavingFiles gamesFolder
    putStrLn ("Selected game: " ++ folder ++ "\n")
    (keepPlaying, newGen) <- loadLevel (Data.List.sort files) gen
    when keepPlaying
        (launch folder newGen)

