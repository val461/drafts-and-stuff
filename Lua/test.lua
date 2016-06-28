#!/usr/bin/env lua

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
    return str:sub(1, -3) .. " }"   -- remove last comma
end
