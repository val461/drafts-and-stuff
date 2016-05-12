import qualified System.Posix.Files as F

filterPaths :: (F.FileStatus -> Bool) -> [FilePath] -> IO [FilePath]
filterPaths p paths = filterH p paths []
    where
        filterH :: (F.FileStatus -> Bool) -> [FilePath] -> [FilePath] -> IO [FilePath]
        filterH p [] filtered = return filtered
        filterH p (path:paths) filtered = do
            status <- F.getFileStatus path
            if p status
            then filterH p paths (path : filtered)
            else filterH p paths filtered

takeDirectories = filterPaths F.isDirectory
takeFiles       = filterPaths F.isRegularFile


takeVisible files = filter isVisible files
    where isVisible filename = ((filename !! 0) /= '.')


decomposePath :: FilePath -> (Folder, RegularFile)
decomposePath path = let
                        (revBasename, revParent) = span (/= separator) (reverse path)
                        basename = reverse revBasename
                        parent = reverse revParent
                    in
                        (parent, basename)
    where separator = '/'


basename path = let revBasename = takeWhile (/= separator) (reverse path)
                in  reverse revBasename
    where separator = '/'


parentDirectory path =  let revParent = dropWhile (/= separator) (reverse path)
                        in  reverse revParent
    where separator = '/'
