--[[
tetromino factory
    create a model for each of the seven one-sided tetrominoes
    deep copy of a model
    random selection among models
]]

require("code.Tetromino")

Tetrominoes = { models = {} }

function Tetrominoes:newInstanceOfModel(index, grid, color)
    return Tetromino(
        self.models[index].squares,
        self.models[index].extremities,
        self.models[index].shiftOnRotation,
        grid,
        color
    )
end

squares = {}
extremities = { squares[], squares[] }
tetromino = { squares = squares, extremities = extremities, shiftOnRotation =  }
table.insert(Tetrominoes.models, tetromino)
