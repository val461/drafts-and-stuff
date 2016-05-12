data Config =   Config { getFolder :: String, getLevel :: Int }

-----------------------
data ParameterType =    Folder | Level
                    deriving (Eq, Show)

data Parameter a = Parameter ParameterType a
                    deriving (Show)

dir = Parameter Folder "hello"
level = Parameter Level 3
--list = [dir,level]
theLevel = fetchLevel list
--theFolder = fetchFolder list



fetchLevel :: [Parameter] -> Int
fetchLevel [] = error "fetchLevel: none found"
fetchLevel (x:xs) = case x of
    Level level -> level
    _ -> fetchLevel xs

{-
fetchParameter :: (a -> Parameter) -> [Parameter] -> b
fetchParameter cons [] = error "fetchLevel: none found"
fetchParameter cons (x:xs) = case x of
    cons value -> value -- doesn't work
    _ -> fetchParameter cons xs
--}

