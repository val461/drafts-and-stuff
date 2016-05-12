{- DOC: Paste all the following commented lines in the file importing this module (don’t forget to update constant ‘filename’).
import qualified SRC.Log as Log

-- write code here


-- logging boilerplate

filename = "-.hs"

fatal :: Show a => String -> a -> b
fatal msg line = Log.reportFatal filename msg line

fixme, bug, err :: Show a => a -> b
fixme = fatal L.fixMe
bug = fatal L.bug
err = fatal L.err
-}

module SRC.Log
( reportFatal
, fixMe
, bug
, err
) where

reportFatal :: Show a => String -> String -> a -> b
reportFatal filename msg line = let message = filename ++ ":" ++ (show line) ++ ": " ++ msg
                                in  error message

fixMe = "FixMe"
bug = "BUG"
err = "error"
