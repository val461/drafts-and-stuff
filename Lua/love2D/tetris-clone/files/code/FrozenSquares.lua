require("code.FrozenSquare")

--[[ TODO
blinkOnRemovalOrSkyTouching

methods
    removeRow
    forEachSquare
    draw
]]

FrozenSquares = {}
FrozenSquares.__index = FrozenSquares

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

function frozenSquares:moveSquare(sq, newPosition)
    
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
    for _, sq in ipairs(self[0]) do
        if sq then
            return true
        end
    end
    return false
end

function FrozenSquares:removeRow(i)
    table.remove(self, i)
end

function FrozenSquares:draw()
    local function drawSquare(location, color)
        love.graphics.setColor(color)
        love.graphics.rectangle("fill", location.x + Square.halfGap, location.y + Square.halfGap, Square.visibleLength, Square.visibleLength)
    end

    local function from(...)

    end

    for i, row in ipairs(self) do
        for j, sq in ipairs(row) do
            drawSquare(from(self.grid, FrozenSquares:realCoordinates(i, j)))
        end
    end
end
