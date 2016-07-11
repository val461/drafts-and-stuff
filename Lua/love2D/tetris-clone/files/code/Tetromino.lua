require("code.Vector")
require("code.Square")

Tetromino = {}
Tetromino.__index = Tetromino
Tetromino.length = 8

function Tetromino.new(squares, extremities, shiftOnRotation, grid, color)
    return setmetatable(
        {
            squares = squares,
            extremities = extremities,  -- a couple of constituent squares, to determine the center
            shiftOnRotation = shiftOnRotation,
            grid = grid,
            color = color or { 40, 40, 40 }
        },
        Tetromino
    )
end

setmetatable(Tetromino, { __call = function (t, ...) return Tetromino.new(...) end })

-- private
function Tetromino:forEachSquare(f)
    for _, sq in ipairs(self.squares) do
        f(sq)
    end
end

-- private
function Tetromino:someSquare(p)
    for _, sq in ipairs(self.squares) do
        if p(sq) then
            return true
        end
    end
    return false
end

-- private
function Tetromino:allSquares(p)
    return not self:someSquare(not p)
end

function Tetromino:isBlocked(direction, frozenSquares)
    local function isBlocked(sq)
        return sq:isBlocked(direction, frozenSquares)
    end
    return self:someSquare(isBlocked)
end

function Tetromino:draw()
    local function drawSquare(sq)
        sq:draw(self.grid)
    end
    love.graphics.setColor(self.color)
    self:forEachSquare(drawSquare)
end

function Tetromino:translate(vector)
    local function translateSquare(sq)
        sq:translate(vector)
    end
    self:forEachSquare(translateSquare)
end

local halfLength = Square.length / 2
local fromCornerToCenterOfSquare = Vector(halfLength * directions.left, halfLength * directions.down)

function Tetromino:center()
    return (self.extremities[1].position + self.extremities[2].position) / 2
end

function Tetromino:rotate()
    local tetrominoCenter = self:center()
    local function rotateSquare(sq)
        local squareCenter = sq.position + fromCornerToCenterOfSquare
        local posRelativeToTetrominoCenter = squareCenter - tetrominoCenter
        local newPosRelativeToTetrominoCenter = Vector(-posRelativeToTetrominoCenter.y, posRelativeToTetrominoCenter.x)
        sq.position:assimilate(newPosRelativeToTetrominoCenter + tetrominoCenter - fromCornerToCenterOfSquare)
    end
    self:forEachSquare(rotateSquare)
    if self.shiftOnRotation then
        if math.random() < 1/2 then
            self:translate(directions.down / 2)
        else
            self:translate(directions.up / 2)
        end
    end
    --[[ DEBUGGING
    local function isInteger(coord)
        return coord == math.floor(coord)
    end
    local function hasIntegerCoords(sq)
        return sq.position:allCoordinates(isInteger) 
    end
    assert(self:allSquares(hasIntegerCoords))
    --]]
end

function Tetromino:freezeInto(frozenSquares)
    function freeze(sq)
        frozenSquares:add(sq.position, self.color)
    end
    self:forEachSquare(freeze)
end
