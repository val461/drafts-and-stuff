debug = true

require("code.Vector")
require("code.Tetromino")
require("code.FrozenSquares")

currentTetromino = {}
tetrominoes = {}
squareUnit = {}
squares = {}

canMoveTimerDuration = 0.2
canMoveTimer = 0

function love.load(arg)
    gridWidth = nCols * Square.length
    player.x = math.floor((love.graphics.getWidth() - player.img:getWidth()) / 2)
    love.graphics.setBackgroundColor(70, 236, 22)
    love.graphics.setColor(40, 40, 40)
end

function love.update(dt)
    if love.keyboard.isDown('escape') then
        love.event.quit()
	end

	if love.keyboard.isDown('left','a') then
		player.x = player.x - (player.speed*dt)
	elseif love.keyboard.isDown('right','d') then
		player.x = player.x + (player.speed*dt)
	end

    if player.x < 0 then
        player.x = 0
    elseif player.x > love.graphics.getWidth() - player.img:getWidth() then
        player.x = love.graphics.getWidth() - player.img:getWidth()
    end

    if canShootTimer > 0 then
        canShootTimer = canShootTimer - dt
    elseif love.keyboard.isDown('space', 'rctrl', 'lctrl') then
        newBullet = { x = player.x + (player.img:getWidth() - bulletImg:getWidth()) / 2, y = player.y }
        table.insert(bullets, newBullet)
        canShootTimer = canShootTimerDuration
    end

    for i, bullet in ipairs(bullets) do
        bullet.y = bullet.y - bulletSpeed * dt

        if bullet.y < -bulletImg:getHeight() then
            table.remove(bullets, i)
        end
    end
end

function love.draw(dt)
    for _, bullet in ipairs(bullets) do
      love.graphics.rectangle("fill", bullet.x, bullet.y, length, length)
    end
end
