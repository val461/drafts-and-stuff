--[[
tetromino factory
    create a model for each of the seven one-sided tetrominoes
    deep copy of a model
    random selection among models
]]

require("code.Vector")
require("code.Tetromino")
require("code.Colors")
math.randomseed(os.time())

Tetrominoes = { models = {} }

function Tetrominoes:newInstanceOfModel(index, grid)
    local new = Tetromino(
        copy(self.models[index].squares),
        grid,
--        self.models[index].color
        colors[math.random(#colors)]
    )
    new:translate(grid.startingPosition - new.squares[centerIndex].position)
    -- [[ DEBUGGING
    new:hasIntegerCoords()
    --]]
    print("Tetrominoes.lua:25: " .. new.squares[centerIndex].position)
    new:enforceRoof()
    print("Tetrominoes.lua:27: " .. new.squares[centerIndex].position)
    return new
end

function Tetrominoes:newInstanceOfRandomModel(grid)
    return self:newInstanceOfModel(math.random(#Tetrominoes.models), grid)
end

local function add(squares, direction)
    table.insert(squares, Square(squares[#squares].position + direction))
end

-- I
local squares = { Square() }
add(squares, directions.down)
add(squares, directions.down)
add(squares, directions.down)
table.insert(Tetrominoes.models, { squares = squares, color = colors.purple })

-- O
local squares = { Square() }
add(squares, directions.down)
add(squares, directions.right)
add(squares, directions.up)
table.insert(Tetrominoes.models, { squares = squares, color = colors.white })

-- T
local squares = { Square() }
add(squares, directions.right)
add(squares, directions.up)
add(squares, directions.down + directions.right)
table.insert(Tetrominoes.models, { squares = squares, color = colors.blue })

-- J
local squares = { Square() }
add(squares, directions.left)
add(squares, directions.down)
add(squares, directions.down)
table.insert(Tetrominoes.models, { squares = squares, color = colors.red })

-- L
local squares = { Square() }
add(squares, directions.right)
add(squares, directions.down)
add(squares, directions.down)
table.insert(Tetrominoes.models, { squares = squares, color = colors.green })

-- S
local squares = { Square() }
add(squares, directions.left)
add(squares, directions.down)
add(squares, directions.left)
table.insert(Tetrominoes.models, { squares = squares, color = colors.yellow })

-- Z
local squares = { Square() }
add(squares, directions.right)
add(squares, directions.down)
add(squares, directions.right)
table.insert(Tetrominoes.models, { squares = squares, color = colors.gray })
