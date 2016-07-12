require("code.Vector")
require("code.Square")
require("code.FrozenSquares")
require("code.Colors")

Grid = {}
Grid.__index = Grid
Grid.innerMargin = 40

function Grid.new(position, nRows, nCols, bgColor, edgeColor)
    local t = {}
    t.outerPosition = position or Vector()
    t.position = t.outerPosition + Vector(Grid.innerMargin, Grid.innerMargin)
    t.frozenSquares = FrozenSquares(nRows, nCols, t)
    t.height = nRows * Square.length + Square.halfGap
    t.width = nCols * Square.length + Square.halfGap
    t.startingPosition = Vector(math.floor(nCols / 2), 0)
    t.bgColor = bgColor or colors.black
    t.edgeColor = edgeColor or colors.gray
    return setmetatable(t, Grid)
end

setmetatable(Grid, { __call = function (t, ...) return Grid.new(...) end })

function Grid:draw()
    love.graphics.setColor(self.edgeColor)
    love.graphics.rectangle("fill", self.outerPosition.x, self.outerPosition.y, self.width + 2 * Grid.innerMargin, self.height + 2 * Grid.innerMargin)

    love.graphics.setColor(self.bgColor)
    love.graphics.rectangle("fill", self.position.x, self.position.y, self.width, self.height)

    self.frozenSquares:draw()
end
