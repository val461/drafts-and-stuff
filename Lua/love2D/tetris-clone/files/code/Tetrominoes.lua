--[[
tetromino factory
    create a model for each of the seven one-sided tetrominoes
    deep copy of a model
    random selection among models
]]

require("code.Vector")
require("code.Tetromino")
math.randomseed(os.time())

Tetrominoes = { models = {} }

function Tetrominoes:newInstanceOfModel(index, grid, color)
    local new = Tetromino(
        copy(self.models[index]),
        2,
        grid,
        color
    )
    new:translate(grid.startingPosition - new.center.position)
    new:align()
    new:enforceRoof()
    return new
end

function Tetrominoes:newInstanceOfRandomModel(grid, color)
    return self:newInstanceOfModel(math.random(#Tetrominoes.models), grid, color)
end

local function add(squares, direction)
    table.insert(squares, Square(squares[#squares].position + direction))
end

-- I
local squares = { Square() }
add(squares, directions.down)
add(squares, directions.down)
add(squares, directions.down)
table.insert(Tetrominoes.models, squares)

-- O
local squares = { Square() }
add(squares, directions.down)
add(squares, directions.right)
add(squares, directions.up)
table.insert(Tetrominoes.models, squares)

-- T
local squares = { Square() }
add(squares, directions.right)
add(squares, directions.up)
add(squares, directions.down + directions.right)
table.insert(Tetrominoes.models, squares)

-- J
local squares = { Square() }
add(squares, directions.left)
add(squares, directions.down)
add(squares, directions.down)
table.insert(Tetrominoes.models, squares)

-- L
local squares = { Square() }
add(squares, directions.right)
add(squares, directions.down)
add(squares, directions.down)
table.insert(Tetrominoes.models, squares)

-- S
local squares = { Square() }
add(squares, directions.left)
add(squares, directions.down)
add(squares, directions.left)
table.insert(Tetrominoes.models, squares)

-- Z
local squares = { Square() }
add(squares, directions.right)
add(squares, directions.down)
add(squares, directions.right)
table.insert(Tetrominoes.models, squares)
