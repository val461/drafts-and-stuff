require("code.Tables")

colors =
    {
        black  = {  0,   0,   0},
        gray   = {100, 100, 100},
        blue   = {  0, 127, 255},
        purple = {  0, 255, 255},
        red    = {255,   0,   0},
        orange = {255, 127,   0},
        yellow = {255, 255,   0},
        green  = {  0, 255,   0},
        white  = {255, 255, 255}
    }

unnamedColors = Tables.values(colors)

function randomColor()
    return unnamedColors[math.random(#unnamedColors)]
end
