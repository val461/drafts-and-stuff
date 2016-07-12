--~ debug = true

require("code.Grid")
require("code.Vector")
require("code.Colors")
require("code.Tetrominoes")
require("code.Strings")
--~ require("code.Square")
--~ require("code.Tetromino")
--~ require("code.FrozenSquares")

local function newTetromino()
    return Tetrominoes:newInstanceOfRandomModel(grid)
end

local function pointsForCompletedRows(n)
    return math.ceil(n * 100 * (1.2^n))
end

local function getNextStep()
    if score > 0 then
        local factor = 10 ^ #tostring(score)
        return factor * math.ceil(score / factor)
    else
        return 1000
    end
end

local function freeze()
    currentTetromino:freezeInto(grid.frozenSquares)
    score = score + pointsForCompletedRows(grid.frozenSquares:removeCompletedRows())
    currentTetromino = newTetromino()
    if currentTetromino:collidesWith(grid.frozenSquares) then
        currentTetromino = nil
        gameover = true
    elseif score > nextStep then
        level = level + 1
        nextStep = getNextStep()
    end
end

local function freezeOrFall()
    if not currentTetromino:move(directions.down, grid.frozenSquares) then
        freeze()
    end
end

local function updateCanFallTimerDuration()
    canFallTimerDuration = 0.96^level
end

paused = false
gameover = false
grid = Grid(Vector(10, 10), 20, 14)
currentTetromino = newTetromino()

level = 1
score = 0
nextStep = getNextStep()

messageHeight = 20
messageLocation = Vector(grid.outerPosition.x + grid.outerWidth + 10, messageHeight)
fontColor = colors.purple

updateCanFallTimerDuration()
canFallTimer = 0

canRotateTimerDuration = 0.28
canMoveTimerDuration = 0.08
canMoveTimer = 0

function love.load(arg)
    love.graphics.setBackgroundColor(70, 236, 22)
    love.graphics.setColor(40, 40, 40)
end

function love.keyreleased(key)
    if key == 'escape' then
        love.event.quit()
    elseif gameover then
        if key == 'n' then
            print("new game.")  --DEBUGGING
            if level > 1 then
                level = level - 1
            end
            score = 0
            nextStep = getNextStep()
            grid.frozenSquares:erase()
            currentTetromino = newTetromino()
            gameover = false
        end
    elseif key == 'tab' then
        paused = not paused
    elseif paused then
        return
    elseif key == 'space' then   -- fall all the way down
        while currentTetromino:canMove(directions.down, grid.frozenSquares) do
            currentTetromino:forceTranslation(directions.down)
        end
        freeze()
	end
end

function love.update(dt)
    if paused or gameover then
        return
    end

    if canFallTimer < canFallTimerDuration then
        canFallTimer = canFallTimer + dt
    else
        freezeOrFall()
        canFallTimer = 0
        if gameover then
            return
        end
    end

    if canMoveTimer < canMoveTimerDuration then
        canMoveTimer = canMoveTimer + dt
    else
        if canMoveTimer < canRotateTimerDuration then
            canMoveTimer = canMoveTimer + dt
        elseif love.keyboard.isDown('up','w') then
            currentTetromino:rotate(grid.frozenSquares)
            canMoveTimer = 0
        end
        if love.keyboard.isDown('left','a') then
            currentTetromino:move(directions.left, grid.frozenSquares)
            canMoveTimer = 0
        end
        if love.keyboard.isDown('right','d') then
            currentTetromino:move(directions.right, grid.frozenSquares)
            canMoveTimer = 0
        end
        if love.keyboard.isDown('down','s') then
            freezeOrFall()
            canMoveTimer = 0
            if gameover then
                return
            end
        end
    end
end

function love.draw()
    grid:draw()
    if currentTetromino then
        currentTetromino:draw()
    end
    love.graphics.setColor(fontColor)
    local paddedMessages = pad({ "level", "score", "objective" }, toStrings{ level, score, nextStep })
    love.graphics.print("level " .. level, messageLocation.x, messageLocation.y)
    love.graphics.print("score " .. score, messageLocation.x, messageLocation.y + messageHeight)
    if gameover then
        love.graphics.print("GAME OVER", messageLocation.x, messageLocation.y + 2 * messageHeight)
    else
        love.graphics.print("next step " .. nextStep, messageLocation.x, messageLocation.y + 2 * messageHeight)
    end
end
