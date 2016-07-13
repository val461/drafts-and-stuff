function pt(t)  -- print a table shallowly
    local str = "{ "
    for k, v in pairs(t) do
        if (type(k) == "string") then
            if (k:find("^[_%a]+[_%w]*$")) then  -- valid variable name
                str = str .. k
            else
                str = str .. "[\"" .. k .. "\"]"
            end
        else
            str = str .. "[" .. tostring(k) .. "]"
        end
        str = str .. " = " .. tostring(v) .. ", "
    end
    if #str > 2 then
        str = str:sub(1, -3)   -- remove last comma
    end
    return str .. " }"
end

function pa(t, printKeys)  -- print an array shallowly
    local str = "{ "
    for i, v in ipairs(t) do
        if (printKeys) then
            str = str .. "[" .. i .. "] = "
        end
        str = str .. tostring(v) .. ", "
    end
    if #str > 2 then
        str = str:sub(1, -3)   -- remove last comma
    end
    return str .. " }"
end

function pk(t)  -- print a table’s keys shallowly
    local str = ""
    for k, _ in pairs(t) do
        if (type(k) == "string") then
            str = str .. k
        else
            str = str .. "[" .. tostring(k) .. "]"
        end
        str = str .. ", "
    end
    if #str > 2 then
        str = str:sub(1, -3)   -- remove last comma
    end
    return str .. " }"
end

function map(f, t)
    local result = {}
    for k, v in ipairs(t) do
        result[k] = f(v)
    end
    return result
end

function newArray(getNewElement, width, height)
    local result = {}
    if height and 1 <= height then
        for i = 1, width do
            table.insert(
                result,
                newArray(
                    function (j) return getNewElement(i, j) end,
                    height
                )
            )
        end
    else
        for i = 1, width do
            table.insert(result, getNewElement(i))    -- set default value to false because nil cannot be stored in lua arrays
        end
    end
    return result
end

function rep(str, n)
    local result = ""
    local i = 0
    while i < n do
        result = result..str
        i = i + 1
    end
    return result
end

function pad(left, right)
    local result = {}
    --~ (waiting for monospace font before aligning to the right)
    --~ local leftColumnSize = sizeOfLongest(left)
    --~ local rightColumnSize = sizeOfLongest(right)
    for i, prefix in ipairs(left) do
        --~ result[prefix] = prefix .. rep(" ", leftColumnSize - #prefix) .. rep(" ", rightColumnSize - #right[i]) .. right[i]
        result[prefix] = prefix .. "  " .. right[i]
    end
    return result
end

local function length(str)
    return #str
end

local function sizeOfLongest(strings)
    return Tables.max(map(length, strings))
end
