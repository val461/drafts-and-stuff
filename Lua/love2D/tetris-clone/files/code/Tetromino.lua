local function forEachSquare(f)
    error("TODO")
end

--[[
instance fields
    fallingSquares
    color
    center    -- its "main" square (for rotations)

instance methods
    canMove(direction)
    move(direction)
    rotate()
    freeze()
    translate(vector)
    draw()

tetromino factory
    create a model for each of the seven one-sided tetrominoes
    deep copy of a model
    random selection among models
]]
