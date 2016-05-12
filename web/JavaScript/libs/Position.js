if (typeof loadedFiles === "undefined") { throw new Error("module required"); }
if (!loadedFiles.hasOwnProperty("Math.js")) { throw new Error("module required"); }
if (!loadedFiles.hasOwnProperty("Timer.js")) { throw new Error("module required"); }

function make2DPosition(x0 = 0, y0 = 0) {
    "use strict";
    var instance = {};

    // private fields
    var timer = makeTimer();

    // private methods
    function computeModulus(x, y) {
        return Math.sqrt(x*x+y*y);
    }

    function computeArgument(x, y) {
        return Math.atan2(y, x);
    };

    function computeChange(v, t) {
        return v * t;
    }
    
    function updateCoordinates(p, t) {
        p.x += computeChange(p.v.x, t);
        p.y += computeChange(p.v.y, t);
    }
    
    // public fields
    instance.x = x0;
    instance.y = y0;
    instance.v = {
        x: 0,
        y: 0,
        v: {
            x: 0,
            y: 0
        }
    };
    instance.a = v.v;

    // public methods
    instance.actualize = function () {
        var t = timer.elapsed();
        updateCoordinates(that, t);
        updateCoordinates(that.v, t);
    };

    instance.setDirection = function (angle) {
        var modulus = MATH.modulus(instance.v.x, instance.v.y);
        instance.v.x = modulus * Math.cos(angle);
        instance.v.y = modulus * Math.sin(angle);
    };

    instance.getDirection = function () {
        return MATH.argument(instance.v.x, instance.v.y);
    };

    return instance;
}

loadedFiles["Position.js"] = true;
