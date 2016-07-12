require("code.Tables")

local function repeatString(str, n)
    local result = ""
    local i = 0
    while i < n do
        result = result..str
        i = i + 1
    end
    return result
end

function toStrings(t)
    return map(tostring, t)
end

local function length(str)
    return #str
end

local function sizeOfLongest(strings)
    return Tables.max(map(length, strings))
end

function pad(left, right)
    local result = {}
    local leftColumnSize = sizeOfLongest(left) + 1
    local rightColumnSize = sizeOfLongest(right)
    for i, prefix in ipairs(left) do
        result[v] = prefix .. repeatString(" ", leftColumnSize - #v) .. repeatString(" ", rightColumnSize - #right[i]) .. right[i]
    end
    return result
end
