require("code.Vector")

Square = {}
Square.__index = Square
Square.halfGap = 1
Square.visibleLength = 6
Square.length = Square.visibleLength + Square.halfGap

function Square.new(position)
    return setmetatable(
        {
            position = position or Vector(),    -- row and column in a grid
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
    return grid.position + (Square.length * self.position)
end

function Square:draw(grid)
    local location = self:realPosition(grid)
    love.graphics.rectangle("fill", location.x + Square.halfGap, location.y + Square.halfGap, Square.visibleLength, Square.visibleLength)
end

-- [[ DEBUGGING
function Square:__tostring()
    return "{ position = " .. self.position .. ", color = " .. pa(self.color) .. " }"
end
--]]
