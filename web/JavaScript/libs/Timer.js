if (typeof loadedFiles === "undefined") { var loadedFiles = {}; }

function makeTimer() {
    "use strict";
    var instance = {};

    // private fields
    var then = Date.now();
    var unit = 1;   // ‘unit’ is specified in milliseconds

    /* restart timer. return how much time elapsed. */
    instance.elapsedReset = function () {
        var now = Date.now();
        var duration = now - then;
        then = now;
        return duration / unit;
    };

    /* return how much time elapsed. */
    instance.elapsedNoReset = function () {
        var now = Date.now();
        var duration = now - then;
        return duration / unit;
    };

    /* restart timer */
    instance.reset = function () {
        then = Date.now();
    };

    instance.getUnit = function () {
        return unit;
    };

    instance.setUnit = function (newValue) {
        if (newValue <= 0) {
            throw new RangeError("setUnit(newValue): newValue must be bigger than zero");
        }
        unit = newValue;
    };
 
    return instance;
}

loadedFiles["Timer.js"] = true;
