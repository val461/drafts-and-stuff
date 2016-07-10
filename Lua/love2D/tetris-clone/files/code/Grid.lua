require("code.Vector")
require("code.Square")
require("code.FrozenSquares")

Grid = {}
Grid.__index = Grid
Grid.length = 8

function Grid.new(position, nRows, nCols, bgColor)
    local t = {}
    t.position = position or Vector()
    t.frozenSquares = FrozenSquares(nRows, nCols)
    t.height = t.frozenSquares.nRows * Square.length
    t.width = t.frozenSquares.nCols * Square.length
    t.bgColor = bgColor or {0, 0, 0}
    return setmetatable(t, Grid)
end

setmetatable(Grid, { __call = function (t, ...) return Grid.new(...) end })

function Grid:draw()
    love.graphics.setColor(self.bgColor)
    -- todo: edge
    love.graphics.rectangle("fill", self.position.x, self.position.y, self.width, self.height)
end

--[[ useless?
function Grid:toRealCoordinates(gridPosition)
    return gridPosition + self.position
end


function Grid:toGridCoordinates(realPosition)
    return realPosition - self.position
end
]]
