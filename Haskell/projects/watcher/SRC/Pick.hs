module SRC.Pick
( filesFrom
, fileFrom
, allFilesIn
) where

import System.Random (StdGen)
import qualified SRC.List as L
import qualified SRC.Log as Log

type RegularFile = FilePath
type Folder = FilePath

filesFrom :: (Num a) => Folder -> a -> StdGen -> ([RegularFile], StdGen)
-- random list of files located in ‘folder’ or its subfolders
filesFrom folder gen = L.randomize (allFilesIn folder) gen

fileFrom :: FilePath -> StdGen -> (FilePath, StdGen)
-- random file located in ‘folder’ or its subfolders
fileFrom folder = L.pickAmong (allFilesIn folder)

allFilesIn :: Folder -> [FilePath]
-- search for files in ‘folder’ and its subfolders
allFilesIn folder =
    let
        (folders, files1) = group (contentOfDir folder)
        files2 = concatMap allFilesIn folders
    in
        files1 ++ files2

contentOfDir :: Folder -> [FilePath]
group :: [FilePath] -> ([Folder], [RegularFile])


-- boilerplate for logging

filename = "Pick.hs"

fatal :: Show a => String -> a -> b
fatal msg line = Log.reportFatal filename msg line

fixme, bug, err :: Show a => a -> b
fixme = fatal L.fixMe
bug = fatal L.bug
err = fatal L.err
