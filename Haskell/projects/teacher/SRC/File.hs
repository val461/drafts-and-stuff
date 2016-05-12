module SRC.File
( RegularFile
, Folder
, groupPaths
, takeVisible
, makeRelative
, parentDirectory
, parentOfDirectory
) where

import System.Directory (doesDirectoryExist, doesFileExist, canonicalizePath, makeRelativeToCurrentDirectory)
import qualified System.FilePath as FP
import qualified System.Posix.Files as F

type RegularFile = FilePath
type Folder = FilePath


{- TODO
    adapt to API System.FilePath
-}


groupPaths :: [FilePath] -> IO ([Folder], [RegularFile])
groupPaths paths = group paths [] []
    where
        group :: [FilePath] -> [Folder] -> [RegularFile] -> IO ([Folder], [RegularFile])
        group [] folders files = return (folders, files)
        group (path:paths) folders files = do
            isDir <- doesDirectoryExist path
            if isDir
            then
                let pathToAdd = path ++ "/"
                in  group paths (pathToAdd : folders) files
            else do
                isFile <- doesFileExist path
                if isFile
                then group paths folders (path : files)
                else group paths folders files


takeVisible files = filter isVisible files
    where isVisible filename = ((filename !! 0) /= '.')


makeRelative initialPath = do
    canonicPath <- canonicalizePath initialPath
    relativePath <- makeRelativeToCurrentDirectory canonicPath
    let path = relativePath ++ "/"
    return path


parentDirectory path =  let revParent = dropWhile (/= separator) (reverse path)
                        in  reverse revParent
    where separator = '/'


parentOfDirectory path = do
    makeRelative (path ++ "/..")


