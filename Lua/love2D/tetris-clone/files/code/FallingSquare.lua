require("code.Vector")

Square = {}
Square.__index = Square
Square.length = 8

function Square.new(position, color)
    return setmetatable(
        {
            position = position or Vector(),
            color = color or {255, 255, 0}
        },
        Square)
end

setmetatable(Square, { __call = function (t, ...) return Square.new(...) end })

function Square:canMove(direction, frozenSquares)
    local target = self.position + direction
    return not frozenSquares[target.x][target.y]
end

function Square:move(direction, frozenSquares)
    if frozenSquares and not self:canMove(direction, frozenSquares) then
        return false
    end
    self:
end

--[[

instance methods
    canMove(direction)
    move(direction)
    draw

]]
