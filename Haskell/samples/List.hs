deleteAt _ [] = []
deleteAt 0 (x:xs) = xs
deleteAt i (x:xs) | i > 0 = x : deleteAt (i - 1) xs

deleteFromTo i j lst    | i < j =   let newLst = deleteAt i lst
                                    in  deleteFromTo i (j-1) newLst
                        | otherwise = lst

insertAt i new xs | i > 0 = begin ++ new ++ end
    where   (begin, end) = splitAt i xs
