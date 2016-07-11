--[[ TODO
blinkOnRemovalOrSkyTouching
]]

require("code.Vector")
require("code.Square")

FrozenSquares = {}
FrozenSquares.__index = FrozenSquares

local topRowIndex = 1

function FrozenSquares.new(nRows, nCols, grid)
    local t = 
        {
            nRows = (nRows or 12),
            nCols = (nCols or 20),
            grid = grid,
            squares = {}
        }
    local i, j
    for i = 1, nRows do
        local row = {}
        for j = 1, nCols do
            table.insert(row, false)    -- set default value to false because nil cannot be stored in lua arrays
        end
        table.insert(t.squares, row)
    end
    return setmetatable(t, FrozenSquares)
end

setmetatable(FrozenSquares, { __call = function (t, ...) return FrozenSquares.new(...) end })

function FrozenSquares:add(position, color)
    self[position.y][position.x] = color or { 40, 40, 40 }
end

function FrozenSquares:invalidCoords(x, y)
    return 1 > x or x > nCols
        or 1 > y or y > nRows
end

local function rowIsComplete(row)
    for _, sq in row do
        if not sq then
            return false
        end
    end
    return true
end

-- private
function FrozenSquares:filterIndexes(p)
    local result = {}
    for i, row in ipairs(self.squares) do
        if p(row) then
            table.insert(result, i)
        end
    end
    return result
end

-- private
function FrozenSquares:getCompletedRows()
    return self:filterIndexes(rowIsComplete)
end

function FrozenSquares:touchesTheSky()
    for _, sq in ipairs(self.squares[topRowIndex]) do
        if sq then
            return true
        end
    end
    return false
end

-- private
function FrozenSquares:duplicateRow(rowIndex, newRowIndex)
    for column, sq in ipairs(self.squares[rowIndex]) do
        self.squares[newRowIndex][column] = sq
    end
end

-- private
function FrozenSquares:eraseRow(rowIndex)
    for column, _ in ipairs(self.squares[rowIndex]) do
        self.squares[rowIndex][column] = false
    end
end

-- private
function FrozenSquares:moveRow(rowIndex, newRowIndex)
    self:duplicateRow(rowIndex, newRowIndex)
    self:eraseRow(rowIndex)
end

-- private
function FrozenSquares:removeRow(rowIndex)
    local down, up = directions.down.y, directions.up.y
    for i = rowIndex + up, topRowIndex, up do
        self:moveRow(i, i + down)
    end
end

-- private
function FrozenSquares:removeRows(rowIndexes)
    for _, rowIndex in ipairs(rowIndexes) do
        self:removeRow(rowIndex)
    end
end

function FrozenSquares:removeCompletedRows()
    local indexes = self:getCompletedRows()
    self:removeRows(indexes)
    return #indexes
end

local function drawSquare(location, color)
    love.graphics.setColor(color)
    love.graphics.rectangle("fill", location.x + Square.halfGap, location.y + Square.halfGap, Square.visibleLength, Square.visibleLength)
end

function FrozenSquares:draw()
    local offset = Vector(-1, -1)
    for i, row in ipairs(self.squares) do
        for j, color in ipairs(row) do
            drawSquare(self.grid.position + Square.length * (Vector(j, i) + offset), color)
        end
    end
end
