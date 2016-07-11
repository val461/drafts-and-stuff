--[[
tetromino factory
    create a model for each of the seven one-sided tetrominoes
    deep copy of a model
    random selection among models
]]

require("code.Tetromino")
math.randomseed(os.time())

Tetrominoes = { models = {} }

function Tetrominoes:newInstanceOfModel(index, grid, color)
    local new = Tetromino(
        self.models[index].squares,
        self.models[index].center,
        grid,
        color
    )
    --TODO
    new:translate(grid.startingPosition - new.center.position)
    new:align()
    --check not over the top
    local highest = new:highest()
    if highest < 0 then
        new:translate(Vector(0, highest))
    end
    return new
end

function Tetrominoes:newInstanceOfRandomModel(grid, color)
    return self:newInstanceOfModel(math.random(#Tetrominoes.models), grid, color)
end

-- I
local squares = {}
table.insert(Tetrominoes.models, { squares = squares, center = squares[?])
