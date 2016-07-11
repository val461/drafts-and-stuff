function copy(a)
    if type(a) == "table" then
        result = {}
        for k, v in pairs(a) do
            result[k] = copy(v)
        end
        return result
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
