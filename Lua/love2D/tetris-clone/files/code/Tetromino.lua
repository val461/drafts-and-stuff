require("code.Vector")
require("code.Square")

centerIndex = 2

Tetromino = {}
Tetromino.__index = Tetromino

function Tetromino.new(squares, grid, color)
    return setmetatable(
        {
            squares = squares,
            grid = grid,
            color = color or { 40, 40, 40 }
        },
    Tetromino)
end

setmetatable(Tetromino, { __call = function (t, ...) return Tetromino.new(...) end })

-- private
function Tetromino:forEachSquare(f)
    for _, sq in ipairs(self.squares) do
        f(sq)
    end
end

-- private
function Tetromino:map(f)
    local result = {}
    for _, sq in ipairs(self.squares) do
        table.insert(result, f(sq))
    end
    return result
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

function Tetromino:canMove(direction, frozenSquares)
    return not self:isBlocked(direction, frozenSquares)
end

function Tetromino:move(direction, frozenSquares)
    if currentTetromino:isBlocked(direction, frozenSquares) then
        return false
    else
        currentTetromino:forceTranslation(direction)
        return true
    end
end

function Tetromino:draw()
    local function drawSquare(sq)
        sq:draw(self.grid)
    end
    love.graphics.setColor(self.color)
    self:forEachSquare(drawSquare)
end

-- private
function Tetromino:forceTranslation(vector)
    local function translateSquare(sq)
        sq:translate(vector)
    end
    self:forEachSquare(translateSquare)
end

--[[ DEPRECATED
local function notAnInteger(x)
    return x ~= math.floor(x)
end

function Tetromino:align()
    if(notAnInteger(self.squares[0].position.x)) then
        self:translate(directions.left / 2)
    end
end
]]

local function getSquareOrdinate(sq)
    return sq.position.y
end

-- private
function Tetromino:highest()
    return math.min(self:map(getSquareOrdinate))
end

function Tetromino:enforceRoof()
    local highest = new:highest()
    if highest < 0 then
        new:forceTranslation(math.abs(highest) * directions.down)
    end
end

-- private
function Tetromino:center()
    return self.squares[centerIndex]:getCenter()
end

-- private
function Tetromino:forceRotation()
    local tetrominoCenter = self:center()
    local function rotateSquare(sq)
        local posRelativeToTetrominoCenter = sq:getCenter() - tetrominoCenter
        posRelativeToTetrominoCenter:rotateCounterclockwise()
        sq:setCenter(posRelativeToTetrominoCenter + tetrominoCenter)
    end
    self:forEachSquare(rotateSquare)
end

-- [[ DEBUGGING
local function isInteger(coord)
    return coord == math.floor(coord)
end

local function hasIntegerCoords(sq)
    return sq.position:allCoordinates(isInteger) 
end

function Tetromino:hasIntegerCoords()
    assert(self:allSquares(hasIntegerCoords))
    print("Tetromino.lua:134: has integer coords.")
end

function Tetromino:__tostring()
    return pa(self.squares)
end
--]]

local function copy(a)
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

function Tetromino:rotate(frozenSquares)
    local new = Tetromino(copy(self.squares))
    new:forceRotation()
    if new:collidesWith(frozenSquares) then
        return false
    else
        self.squares = new.squares
        return true
    end
end

function Tetromino:collidesWith(frozenSquares)
    function collides(sq)
        return frozenSquares[sq.y][sq.x]
    end
    return self:someSquare(collides)
end

function Tetromino:freezeInto(frozenSquares)
    function freeze(sq)
        frozenSquares:add(sq.position, self.color)
    end
    self:forEachSquare(freeze)
end
