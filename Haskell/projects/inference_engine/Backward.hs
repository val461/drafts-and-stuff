-- Knowledge -> Pred -> Bool

import qualified Data.Map as Map
import qualified Data.Set as Set
import qualified Data.Tuple as Tuple
import Data.Map (Map)
import Data.Set (Set)


{-
allObjects :: Map Name Properties
type Object = (Name, Properties)
type Name = String
type Properties = Set Property
type Property = (String, [Name], Value)    -- String: the property, possibly with parameters ; [Name]: its arguments in order, if any ; Value: its value
type Value = String

prop1 = ("=y+2", ["y"], "True")
propSet1 = Set.fromList [prop1]
obj1 = ("x", propSet1)

prop2 = ("even", [], "True")
propSet2 = Set.fromList [prop2]
obj2 = ("y", propSet2)

allObjects = Map.fromList [obj1, obj2]

type Implication = (Set Properties, Set Properties)
-}

-- old idea:
-- knowledgeBase :: Map (String, [ArgumentName]) Image -- Map.fromList [Function]

type Function a = (String, [a], Image)   -- e.g., (("P(x,y)", ["A","B"]), "True") iff P(A,B) is true
type Image = String
type ConcreteFunction = Function String
type AbstractFunction = Function Int         -- each int is the index of an argument

prop1 = ("x=y+2", ["x","y"], "True")
prop2 = ("even(x)", ["x"], "True")
propSet1 = Set.fromList [prop1, prop2]

type Implication = ([AbstractFunction], [AbstractFunction])

absProp1 = ("x=y+2", [0,1], "True")
absProp2 = ("even(y)", [1], "True")
antecedents = [absProp1, absProp2]

absProp3 = ("even(x)", [0], "True")
consequents = [absProp3]

imp1 = (antecedents, consequents)

getIndexedArgs :: Function a -> Function b -> Map a b
getIndexedArgs (desc1, args1, image1) (desc2, args2, image2) = Map.fromList (zip args1 args2)

changeIndexingOneFunc :: Eq a => Map a b -> Function a -> Function b
changeIndexingOneFunc indexing (desc, is, image) =
    let new_is = foldr (replaceWithTable indexing) [] is
    in (desc, new_is, image)
    where
        replaceWithTable indexing old_i new_is =
            case lookup old_i indexing of
                Nothing -> error "bug: no replacement found for an index"
                Just new_i -> new_i:new_is

changeIndexing :: Eq a => Map a b -> [Function a] -> [Function b]
changeIndexing indexing funcs = map (changeIndexingOneFunc indexing) funcs

flipIndexing :: Map a b -> Map b a
flipIndexing is = map Tuple.swap . Map.

checkOne :: AbstractFunction -> AbstractFunction -> Bool
checkOne _ _ = undefined -- FIXME

checkAll :: [AbstractFunction] -> [AbstractFunction] -> Bool
checkAll _ _ = undefined -- FIXME

findMatchingCouple :: [Function a] -> [Function b] -> Maybe (Function a, Function b)
findMatchingCouple goals knownProps = undefined -- FIXME
{-
    | (desc1 /= desc2) = Nothing
    | (image1 /= image2) = Nothing
    | (length args1 /= length args2) = Nothing
-}

inferOne :: Implication -> [ConcreteFunction] -> [ConcreteFunction]
inferOne ([], potentialConsequences) props = []
inferOne (goals, potentialConsequences) knownProps =
    case findMatchingCouple knownProps goals of
        Nothing -> []
        Just (p, g) ->
            let indexing = getIndexedArgs p g
            in  if checkAll goals (changeIndexing indexing knownProps)
                then changeIndexing (flipIndexing indexing) potentialConsequences
                else []

{-
type Object = Map Key Value
type Key = String
type Value = Bool
data Prop = Prop Object String

type Ant = Prop
type Cons = Prop
type Imp = (Set Ant, Set Cons)

ask :: Key -> Object -> [Object] -> [Imp] -> Value
ask property object objects implications =
    case Map.lookup property object of
        (Just value) -> value
        Nothing -> undefined{-- calculate value
            -- lookup known implications for one whose consequent would answer our question
            -- ...
--}

x = Map.fromList
    [
        ("=y+2", True)
    ]

y = Map.fromList
    [
        ("even", True)
    ]

prop0a = "x=24"
prop0b = "y=22"
prop1 = "even(y)"
prop2 = "x=y+2"

--imp1 = (Set.fromList [Prop x "=y+2", Prop y "even"], Set.fromList [Prop x "even"])

{-infer2 :: Imp -> [Object] -> [Object]
infer2 (objectives, result) ants =
    if objectives `Set.isSubsetOf` ants
    then result
    else Map.insert result True ants
-}

--inferMany :: [Imp] -> [Ant] -> [Cons]

{-inferOne :: Imp -> Set Ant -> Set Cons
inferOne (objectives, results) ants =   if objectives `Set.isSubsetOf` ants
                                        then results
                                        else Set.empty

res = inferOne imp1 (Set.fromList [prop1, prop2])
-}
-}
