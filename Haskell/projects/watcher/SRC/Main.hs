import qualified SRC.Log as Log

main = do
    files <- F.filesIn Folder
    callProcess "/usr/bin/env" ("vlc" : files)

-- boilerplate for logging

filename = "Main.hs"

fatal :: Show a => String -> a -> b
fatal msg line = Log.reportFatal filename msg line

fixme, bug, err :: Show a => a -> b
fixme = fatal L.fixMe
bug = fatal L.bug
err = fatal L.err
