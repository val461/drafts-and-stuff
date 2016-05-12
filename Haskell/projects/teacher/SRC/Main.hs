import qualified System.Directory as D
import Control.Monad (when)
import System.Random (StdGen, getStdGen)
import System.IO.Error (isDoesNotExistError, ioeGetFileName, catchIOError)

import qualified SRC.File as F
import qualified SRC.Interaction as I
import qualified SRC.Game as G


handler :: IOError -> IO ()
handler e
    | isDoesNotExistError e = case ioeGetFileName e of
        Just path -> putStrLn $ "error: file does not exist: “" ++ path ++ "”"
        Nothing -> putStrLn "error: file does not exist"
    | otherwise = ioError e


determineGamesFolder = do
        defaultIsValid <- D.doesDirectoryExist defaultFolder
        when defaultIsValid
            (D.setCurrentDirectory defaultFolder)
        return "."
    where
        defaultFolder :: F.Folder
        defaultFolder = "correspondences"

main = do
    putStrLn ""
    putStrLn I.newSection
    putStrLn "Hello!\n"
    gamesFolder <- determineGamesFolder
    gen <- getStdGen
    (G.launch gamesFolder gen) `catchIOError` handler

