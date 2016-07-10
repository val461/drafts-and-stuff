debug = true

player = { x = 0, y = 710, speed = 150 }

canShootTimerDuration = 0.2
canShootTimer = 0

bulletImg = nil
bulletSpeed = 250
bullets = {}

function love.load(arg)
    bulletImg = love.graphics.newImage('assets/bullet.png')
    player.img = love.graphics.newImage('assets/plane.png')
    player.x = math.floor((love.graphics.getWidth() - player.img:getWidth()) / 2)
    love.graphics.setBackgroundColor(70, 236, 22)
    love.graphics.setColor(0, 0, 255) -- TO INQUIRE: why does this change the picture’s color?
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
    love.graphics.draw(player.img, player.x, player.y)

    for _, bullet in ipairs(bullets) do
      love.graphics.draw(bulletImg, bullet.x, bullet.y)
    end
end
