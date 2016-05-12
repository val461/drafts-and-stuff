import qualified System.Random as R
import System.Random (Random, RandomGen, StdGen)

--standardDeviation :: (Num a) => [a] -> a
standardDeviation xs = sqrt $ average (map sq xs) - (sq $ average xs)
    where
        sq = (^2)

average xs = (sum xs) / (fromIntegral $ length xs)

--group :: Int -> [a] -> [[a]]
-- divide list in groups of size n
group n [] = []
group n list =
    let
        (firsts, lasts) = splitAt n list
    in
        firsts : group n lasts

simulate :: (Floating b, Random b, RandomGen g) => Int -> Int -> b -> b -> g -> ([b] -> b) -> [b]
simulate nTimes nNumbers min max gen f =
    let
        infinityOfRands = R.randomRs (min, max) gen
        randomLists = (take nTimes . group nNumbers) infinityOfRands
    in
        map f randomLists

{-
avg = average result
stddev = standardDeviation result
-}
f = simulate 100 20 (500::Double) 1500
avg gen = f gen average
std gen = f gen standardDeviation

result = avg

main = do
    gen <- R.newStdGen
    let
        a = avg gen
        s = std gen
        aa = average a
        as = average s
        ss = standardDeviation s
    print $ ss
