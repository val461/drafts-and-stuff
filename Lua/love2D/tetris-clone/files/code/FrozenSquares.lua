--[[ TODO
blinkOnRemovalOrSkyTouching
]]

require("code.Vector")
require("code.Square")

FrozenSquares = {}
FrozenSquares.__index = FrozenSquares

local topRowIndex = 0

function FrozenSquares.new(nRows, nCols, grid)
    local t = 
        {
            nRows = (nRows or 12),
            nCols = (nCols or 20),
            grid = grid
        }
    local i, j
    for i = 1, nRows do
        local row = {}
        for j = 1, nCols do
            table.insert(row, false)    -- set default value to false because nil cannot be stored in lua arrays
        end
        table.insert(t, row)
    end
    return setmetatable(t, FrozenSquares)
end

setmetatable(FrozenSquares, { __call = function (t, ...) return FrozenSquares.new(...) end })

function FrozenSquares:add(position, color)
    t[position.y][position.x] = color or { 40, 40, 40 }
end

local function rowIsComplete(row)
    for _, v in row do
        if not v then
            return false
        end
    end
    return true
end

local function filterIndexes(p)
    local result = {}
    for i, row in pairs(self) do
        if p(row) then
            table.insert(result, i)
        end
    end
    return result
end

function FrozenSquares:getCompletedRows()
    return filterIndexes(rowIsComplete)
end

function FrozenSquares:touchesTheSky()
    for _, sq in pairs(self[topRowIndex]) do
        if sq then
            return true
        end
    end
    return false
end

-- private
function FrozenSquares:duplicateRow(rowIndex, newRowIndex)
    for column, sq in pairs(self[rowIndex]) do
        self[newRowIndex][column] = sq
    end
end

-- private
function FrozenSquares:eraseRow(rowIndex)
    for column, _ in pairs(self[rowIndex]) do
        self[rowIndex][column] = false
    end
end

-- private
function FrozenSquares:moveRow(rowIndex, newRowIndex)
    self:duplicateRow(rowIndex, newRowIndex)
    self:eraseRow(rowIndex)
end

function FrozenSquares:removeRow(rowIndex)
    local down, up = directions.down.y, directions.up.y
    for i = rowIndex + up, topRowIndex, up do
        self:moveRow(i, i + down)
    end
end

local function drawSquare(location, color)
    love.graphics.setColor(color)
    love.graphics.rectangle("fill", location.x + Square.halfGap, location.y + Square.halfGap, Square.visibleLength, Square.visibleLength)
end

function FrozenSquares:draw()
    for i, row in pairs(self) do
        for j, color in pairs(row) do
            drawSquare(self.grid.position + Square.length * Vector(j, i), color)
        end
    end
end
