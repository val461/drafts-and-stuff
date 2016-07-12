require("code.Tables")
require("code.Vector")
require("code.Tetromino")
require("code.Colors")
math.randomseed(os.time())

Tetrominoes = { models = {} }
--~ centerIndex = 2 --DEBUGGING

function Tetrominoes:newInstanceOfModel(index, grid)
    local new = Tetromino(
        copy(self.models[index].squares),
        grid,
        self.models[index].color
        --~ randomColor()
    )
    --~ print("Tetrominoes:17: "..new) --DEBUGGING
    new:forceTranslation(grid.startingPosition - new.squares[centerIndex].position)
    --[[ DEBUGGING
    new:hasIntegerCoords()
    --]]
    --~ print("Tetrominoes.lua:25: " .. new.squares[centerIndex].position)
    new:enforceRoof()
    --~ print("Tetrominoes.lua:27: " .. new.squares[centerIndex].position)
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
squares = { Square() }
add(squares, directions.down)
add(squares, directions.right)
add(squares, directions.up)
table.insert(Tetrominoes.models, { squares = squares, color = colors.white })

-- T
squares = { Square() }
add(squares, directions.right)
add(squares, directions.up)
add(squares, directions.down + directions.right)
table.insert(Tetrominoes.models, { squares = squares, color = colors.blue })

-- J
squares = { Square() }
add(squares, directions.left)
add(squares, directions.down)
add(squares, directions.down)
table.insert(Tetrominoes.models, { squares = squares, color = colors.red })

-- L
squares = { Square() }
add(squares, directions.right)
add(squares, directions.down)
add(squares, directions.down)
table.insert(Tetrominoes.models, { squares = squares, color = colors.green })

-- S
squares = { Square() }
add(squares, directions.left)
add(squares, directions.down)
add(squares, directions.left)
table.insert(Tetrominoes.models, { squares = squares, color = colors.yellow })

-- Z
squares = { Square() }
add(squares, directions.right)
add(squares, directions.down)
add(squares, directions.right)
table.insert(Tetrominoes.models, { squares = squares, color = colors.gray })
