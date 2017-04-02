function f(max)
    local n1 = 1
    local n2 = 2
    local n3 = n1 + n2
    local sum = n2
    local i = 3
    while n3 <= max do
        if (i-2) % 3 == 0 then
            sum = sum + n3
        end
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        i=i+1
    end
    return sum
end

print(f(4*10^6))
