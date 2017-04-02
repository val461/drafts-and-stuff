max = 2
lengths = {[1] = 0}

function nextValidAncestor(v, max)
    --~ assert(1 <= math.tointeger(v))
    local r = v % 3
    local n
    if r == 0 then
        if v >= max then return end
            
        if 
            
        end
    elseif r == 1 then
    elseif r == 2 then
    else
        error("r == "..r)
    end
end

function nextOldestValidAncestor(v, max)
    
end

function trySeq(v0)
    local v = v0
    local i = 0
    local n
    while true do
        --~ print(v)
        r = v % 3

        if r == 0 then
            if v > max then
                return
            else
                v = 2*v
            end
        elseif r == 1 then
            n = math.tointeger((v - 1) / 3)
            assert(n)
            if lengths[n] then return end
            if n >= 1 and not lengths[n] then
                v = n
            else
                v = 2*v
            end
        elseif r == 2 then
            v = 2*v
        else
            error("r == "..r)
        end

        i = i + 1
        if v <= max and not lengths[v] then
            lengths[v] = lengths[v0] + i
        end
    end
end

function fill()
    v0 = 1
    while #lengths <= max do
        assert(v0 <= max)
        trySeq(v0)
        v0 = v0 + 1
    end
    pt(lengths)
end
