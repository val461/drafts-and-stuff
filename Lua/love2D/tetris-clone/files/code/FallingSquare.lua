require("code.Vector")

Square = {}
Square.__index = Square
Square.length = 8

function Square.new(position, color)
    return setmetatable(
        {
            position = position or Vector(),    -- row and column in a grid
            color = color or { 255, 255, 0 }
        },
        Square)
end

setmetatable(Square, { __call = function (t, ...) return Square.new(...) end })

function Square:isBlocked(direction, frozenSquares)
    local target = self.position + direction
    return frozenSquares[target.x][target.y]
end

function Square:translate(vector)
    position:translate(vector)
end

function Square:realPosition(grid)
    return grid.position + self.position
end

function Square:draw(grid)
    local location = self:realPosition(grid)
    love.graphics.rectangle("fill", location.x, location.y, Square.length, Square.length)
end

-- [[ DEBUGGING
function Square:__tostring()
    return "{ position = " .. self.position .. ", color = " .. pa(self.color) .. " }"
end
--]]
