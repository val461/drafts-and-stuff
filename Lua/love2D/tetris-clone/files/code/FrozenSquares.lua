--[[ TODO
blinkOnRemovalOrSkyTouching
draw
]]

require("code.Vector")
require("code.Square")

FrozenSquares = {}
FrozenSquares.__index = FrozenSquares

local topRow = 0

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

function FrozenSquares:someRow(p)
    for i, row in ipairs(self) do
        if p(row) then
            return i
        end
    end
    return nil
end

local function rowIsComplete(row)
    for _, v in row do
        if not v then
            return false
        end
    end
    return true
end

function FrozenSquares:someRowIsComplete()
    return self:someRow(rowIsComplete)
end

function FrozenSquares:touchesTheSky()
    for _, sq in ipairs(self[topRow]) do
        if sq then
            return true
        end
    end
    return false
end

local function duplicateRow(t, rowIndex, newRowIndex)
    for column, sq in ipairs(t[rowIndex]) do
        t[newRowIndex][column] = sq
    end
end

local function eraseRow(t, rowIndex)
    for column, _ in ipairs(t[rowIndex]) do
        t[rowIndex][column] = false
    end
end

local function moveRow(t, rowIndex, newRowIndex)
    duplicateRow(t, rowIndex, newRowIndex)
    eraseRow(t, rowIndex)
end

function FrozenSquares:removeRow(rowIndex)
    local down, up = directions.down.y, directions.up.y
    for i = rowIndex + up, topRow, up do
        moveRow(self, i, i + down)
    end
end

local function drawSquare(location, color)
    love.graphics.setColor(color)
    love.graphics.rectangle("fill", location.x + Square.halfGap, location.y + Square.halfGap, Square.visibleLength, Square.visibleLength)
end

function FrozenSquares:draw()
    for i, row in ipairs(self) do
        for j, color in ipairs(row) do
            drawSquare(self.grid.position + Square.length * Vector(j, i), color)
        end
    end
end
