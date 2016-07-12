require("code.Grid")
require("code.Vector")
require("code.Colors")
require("code.Tetrominoes")
--~ require("code.Square")
--~ require("code.Tetromino")
--~ require("code.FrozenSquares")

local function newTetromino()
    return Tetrominoes:newInstanceOfRandomModel(grid)
end

local function pointsForCompletedRows(n)
    return math.ceil(n * 100 * (1.2^n))
end

local function freezeOrFall()
    if not currentTetromino:move(directions.down, grid.frozenSquares) then
        freeze()
    end
end

local function freeze()
    currentTetromino:freezeInto(grid.frozenSquares)
    score = score + pointsForCompletedRows(grid.frozenSquares:removeCompletedRows())
    currentTetromino = newTetromino()
    if currentTetromino:collidesWith(grid.frozenSquares) then
        currentTetromino = nil
        gameover = true
    end
end

function updateCanFallTimerDuration()
    canFallTimerDuration = 0.96^level
end

paused = false
gameover = false
grid = Grid(Vector(10, 10), 20, 14, colors.black)
currentTetromino = newTetromino()

level = 1
score = 0

updateCanFallTimerDuration()
canFallTimer = 0

canMoveTimerDuration = 0.2
canMoveTimer = 0

function love.load(arg)
    love.graphics.setBackgroundColor(70, 236, 22)
    love.graphics.setColor(40, 40, 40)
end

function love.update(dt)
    if love.keyboard.isDown('escape') then
        print("exiting.")  --DEBUGGING
        love.event.quit()
	end

    if gameover then
        if love.keyboard.isDown('return', 'n') then
            print("new game.")  --DEBUGGING
            --TODO
            level = level + 1
            score = 0
            grid.frozenSquares:erase()
            currentTetromino = newTetromino()
            canFallTimer = 0
            gameover = false
        end
        return
    end

    if love.keyboard.isDown('tab') then
        if paused then
            if canMoveTimer > canMoveTimerDuration then
                paused = false
            else
                canMoveTimer = canMoveTimer + dt
            end
        else
            paused = true
            canMoveTimer = 0
        end
        print("paused: " .. paused)  --DEBUGGING
	end

    if paused then
        return
    end

    if canFallTimer < canFallTimerDuration then
        canFallTimer = canFallTimer + dt
    else
        freezeOrFall()
        if gameover then
            return
        end
        canFallTimer = 0
    end

    if canMoveTimer < canMoveTimerDuration then
        canMoveTimer = canMoveTimer + dt
    else
        if love.keyboard.isDown('up','w') then
            currentTetromino:rotate(grid.frozenSquares)
        end
        if love.keyboard.isDown('left','a') then
            currentTetromino:move(directions.left, grid.frozenSquares)
        end
        if love.keyboard.isDown('right','d') then
            currentTetromino:move(directions.right, grid.frozenSquares)
        end
        if love.keyboard.isDown('down','s') then
            freezeOrFall()
            if gameover then
                return
            end
        end
        canMoveTimer = 0
    end

	if love.keyboard.isDown('space') then   -- fall all the way down
        while currentTetromino:canMove(directions.down, grid.frozenSquares) do
            currentTetromino:forceTranslation(directions.down)
        end
        freeze()
	end
end

function love.draw()
    grid:draw()
    currentTetromino:draw()
    love.graphics.print(score, 0, 0)
end
