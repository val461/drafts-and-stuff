Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
    return setmetatable(
        {
            x = x or 0,
            y = y or 0
        },
        Vector
    )
end

setmetatable(Vector, { __call = function (t, ...) return Vector.new(...) end })

function Vector.__add(t1, t2)
    return Vector(t1.x + t2.x, t1.y + t2.y)
end

function Vector.__mul(a, t)
--    assert(type(a) == "number" and type(t) == "table", "wrong arguments")
    return Vector(a * t.x, a * t.y)
end

function Vector.__sub(t1, t2)
    return t1 + (-1 * t2)
end

function Vector.__div(t, a)
--    assert(type(a) == "number" and type(t) == "table", "wrong arguments")
    return (1/a) * t
end

function Vector.__eq(t1, t2)
    return t1.x == t2.x and t1.y == t2.y
end

function Vector.__tostring(t)
    return "{ x = " .. t.x .. ", y = " .. t.y .. " }"
end

function Vector:assimilate(t)
    self.x = t.x
    self.y = t.y
end

function Vector:translate(t)
    self:assimilate(self + t)
end

function Vector:rotateCounterclockwise()
    self:assimilate(Vector(-self.y, self.x))
end

function Vector:rotateClockwise()
    self:assimilate(Vector(self.y, -self.x))
end

function Vector:allCoordinates(p)
    return p(self.x) and p(self.y)
end

directions =
    {
        left = Vector(-1, 0),
        up = Vector(0, -1),
        right = Vector(1, 0),
        down = Vector(0, 1)
    }