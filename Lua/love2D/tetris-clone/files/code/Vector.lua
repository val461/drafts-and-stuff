Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
    return setmetatable(
        {
            x = x or 0,
            y = y or 0
        },
        Vector)
end

setmetatable(Vector, { __call = function (t, ...) return Vector.new(...) end })

function Vector.__add(t1, t2)
    return Vector(t1.x + t2.x, t1.y + t2.y)
end

function Vector.__eq(t1, t2)
    return t1.x == t2.x and t1.y == t2.y
end

function Vector:__tostring()
    return "{ x = " .. self.x .. ", y = " .. self.y .. " }"
end

function Vector:assimilate(t)
    self.x = t.x
    self.y = t.y
end

function Vector:translate(t)
    self:assimilate(self + t)
end

directions =
    {
        left = Vector(-1, 0),
        up = Vector(0, -1),
        right = Vector(1, 0),
        down = Vector(0, 1)
    }
