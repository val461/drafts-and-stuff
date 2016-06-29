require("code.Vector")

Grid = {}
Grid.__index = Grid
Grid.length = 8

function Grid.new(position, width, height, bgColor)
    return setmetatable(
        {
            position = position or Vector(),
            width = width or 100,
            height = height or 100,
            bgColor = bgColor or {0, 0, 0}
        },
        Grid)
end

setmetatable(Grid, { __call = function (t, ...) return Grid.new(...) end })

--[[
function Grid:toRealCoordinates(gridPosition)
    return gridPosition + self.position
end


function Grid:toGridCoordinates(realPosition)
    return realPosition - self.position
end
]]

--[[
instance methods
    draw
    toRealCoordinates
    toGridCoordinates

todo
    colored edges?

]]
