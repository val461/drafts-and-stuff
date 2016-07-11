require("code.Vector")
require("code.Square")

Tetromino = {}
Tetromino.__index = Tetromino
Tetromino.length = 8

function Tetromino.new(fallingSquares, center, shiftOnRotation, grid, color)
    return setmetatable(
        {
            squares = squares,
            center = center,
            shiftOnRotation = shiftOnRotation,
            grid = grid,
            color = color or { 40, 40, 40 }
        },
        Tetromino)
end

setmetatable(Tetromino, { __call = function (t, ...) return Tetromino.new(...) end })

-- private
function Tetromino:forEachSquare(f)
    for _, v in pairs(self) do
        f(v)
    end
end

-- private
function Tetromino:someSquare(p)
    for _, v in pairs(self) do
        if p(v) then
            return true
        end
    end
    return false
end

-- private
function Tetromino:allSquares(p)
    for _, v in pairs(self) do
        if not p(v) then
            return false
        end
    end
    return true
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
    self:forEachSquare(draw)
end

function Tetromino:translate(vector)
    local function translateSquare(sq)
        sq:translate(vector)
    end
    self:forEachSquare(translate)
end

local halfLength = Square.length / 2
local fromCornerToCenterOfSquare = Vector(halfLength * directions.left, halfLength * directions.down)

function Tetromino:rotate()
    local function rotateSquare(sq)
        local squareCenter = sq.position + fromCornerToCenterOfSquare
        local posRelativeToTetrominoCenter = squareCenter - self.center
        local newPosRelativeToTetrominoCenter = Vector(-posRelativeToTetrominoCenter.y, posRelativeToTetrominoCenter.x)
        sq.position:assimilate(newPosRelativeToTetrominoCenter + self.center - fromCornerToCenterOfSquare)
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

function Tetromino:freeze(frozenSquares)

end

--[[
tetromino factory
    create a model for each of the seven one-sided tetrominoes
    deep copy of a model
    random selection among models
]]
