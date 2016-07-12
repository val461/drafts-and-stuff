--[[
self = Tetrominoes; index = 1
pt(copy(self.models[index].squares))
]]

function copy(a)    -- deep copy for values but shallow copy for keys and metatables
    if type(a) == "table" then
        local result = {}
        for k, v in pairs(a) do
            result[k] = copy(v)
        end
        return setmetatable(result, getmetatable(a))
    else
        return a
    end
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

function keys(t)
    local result = {}
    for k, _ in pairs(t) do
        table.insert(result, k)
    end
    return result
end
