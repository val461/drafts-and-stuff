function sumIntegers(n)
    return n*(n+1)/2
end

--[[ sum the n first positive multiples of k
with ‘k’ and ‘n’ positive integers ]]
function sumMultiples(r, n)
    return r*sumIntegers(n)
end

--[[ like sumMultiples but stop at the biggest integer below max
with ‘max’ a positive real number ]]
function sumMultiplesWithLimit(r, max)
    return sumMultiples(r, (max-1)//r)
end

max = 1000
print(sumMultiplesWithLimit(3,max)+sumMultiplesWithLimit(5,max)-sumMultiplesWithLimit(3*5,max))
