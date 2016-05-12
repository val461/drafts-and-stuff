module SRC.Interaction
( display
, showPercentage
, newSection
, askNumber
, selectionMenu
, askFolderHavingFiles
, plural
) where

import qualified System.Directory as D
import qualified Text.Printf as T
import qualified SRC.File as F


showPercentage :: Double -> String
showPercentage = showPercentageWithPrecision defaultPrecision
    where defaultPrecision = 2

showPercentageWithPrecision :: (Integral a, Show a) => a -> Double -> String
showPercentageWithPrecision digitsAfterComma fraction
    | (digitsAfterComma >= 1) =
        let formatString = "%." ++ (show digitsAfterComma) ++ "f%%"
        in  T.printf formatString percentage

    | (digitsAfterComma == 0) =
        let formatString = "%d%%"
        in  T.printf formatString (round percentage :: Int)

    | otherwise = error "minimal precision must be non-negative"
    where percentage = 100 * fraction


plural n    | n >= 2 = "s"
            | otherwise = ""


display :: (Num a, Show a) => a -> [String] -> (a, String)
-- make a string presenting each element of the list with an index,
-- starting with the index given as first argument
-- the first value of the resulting tuple is the last index shown in the string
display indexToShow [] = (indexToShow - 1, "")
display indexToShow (opt : options) =   let (lastIndexShown, otherOptions) = display (indexToShow + 1) options
                                        in  (lastIndexShown, show indexToShow ++ ": " ++ opt ++ "\n" ++ otherOptions)


newSection :: String
newSection = replicate 72 '*'

askNumber :: (Num a, Ord a, Read a, Show a) => String -> a -> a -> IO (Either String a)
-- accepts two inputs from user: a number or [enter]
-- anything else results in prompting the user again
askNumber msg min max
    | min <= max = do
        putStrLn msg
        line <- getLine
        putStrLn newSection
        case (reads line) of
            [] -> if line == ""
                  then return (Left "")
                  else tryAgain ("Answer not understood.")
            [(n, _)] -> do
                    if (min <= n && n <= max)
                    then return (Right n)
                    else tryAgain ("Answer must be comprised between " ++ (show min)
                                    ++ " and " ++ (show max) ++ ".")
    | min > max = askNumber msg max min
    where
        tryAgain errorMsg = do
            putStr errorMsg
            putStrLn " Please try again."
            askNumber msg min max


selectionMenu :: String -> String -> [String] -> IO (Maybe Int)
selectionMenu _ _ [] = return Nothing
selectionMenu prefix suffix options = do
    let (i, menu) = display 1 options
    answer <- askNumber (prefix ++ menu ++ suffix) 1 i
    case answer of
        (Right n)   -> return (Just n)
        (Left "")   -> return Nothing


askFolderHavingFiles :: F.Folder -> IO (F.Folder, [F.RegularFile])
-- returns a folder, selected by the user, containing regular files (at least one) and the list of these files
askFolderHavingFiles dir = do
    folder <- F.makeRelative dir
    filenames <- D.getDirectoryContents folder
    let paths = map (folder ++) (F.takeVisible filenames)
    (folders, files) <- F.groupPaths paths
    let
        validFolder = (length files > 0)    -- at least one regular file in the folder
        prefix = ("Current folder: " ++ folder ++ "\n\nSubfolders:\n")
        suffix =    if validFolder
                    then "\nnumber + [enter]: select a subfolder.\n[enter]: play in this folder.\n"
                    else "\nnumber + [enter]: select a subfolder.\n"

        tweakedFolders = folders ++ [folder ++ ".."]
        l = length tweakedFolders

    result <- selectionMenu prefix suffix tweakedFolders
    case result of
        Just n  | n == l -> do
                                parent <- F.parentOfDirectory folder
                                askFolderHavingFiles parent
                | otherwise -> askFolderHavingFiles (tweakedFolders !! (n - 1))

        Nothing ->  if validFolder
                    then return (folder, files)
                    else askFolderHavingFiles (tweakedFolders !! 0)

