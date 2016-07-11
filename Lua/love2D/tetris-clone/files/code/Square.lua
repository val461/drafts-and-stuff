require("code.Vector")

Square = {}
Square.__index = Square
Square.halfGap = 1
Square.visibleLength = 6
Square.length = Square.visibleLength + Square.halfGap

function Square.new(position)
    return setmetatable(
        {
            position = position or Vector()    -- row and column in a grid
        },
        Square
    )
end

setmetatable(Square, { __call = function (t, ...) return Square.new(...) end })

local fromCornerToCenter = Vector(directions.right, directions.down) / 2
local fromCenterToCorner = -fromCornerToCenter

function Square:getCenter()
    return self.position + fromCornerToCenter
end

function Square:setCenter(position)
    self.position = position + fromCenterToCorner
end

function Square:isBlocked(direction, frozenSquares)
    local target = self.position + direction
    return frozenSquares.invalidCoords(target.x, target.y) or frozenSquares[target.y][target.x]
end

function Square:translate(vector)
    position:translate(vector)
end

function Square:realPosition(grid)
    return grid.position + (Square.length * self.position)
end

function Square:draw(grid)
    local location = self:realPosition(grid)
    love.graphics.rectangle("fill", location.x + Square.halfGap, location.y + Square.halfGap, Square.visibleLength, Square.visibleLength)
end

-- [[ DEBUGGING
local function pa(t, printKeys)  -- print an array shallowly
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

function Square:__tostring()
    return "{ position = " .. self.position .. ", color = " .. pa(self.color) .. " }"
end
--]]
