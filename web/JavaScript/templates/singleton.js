var MODULE = (function (globalVariables) {
    "use strict";
    var singleton = {};

    // private fields
    var privateVariable = 3;

    // private methods
    function privateFunction(args) {
        
    }

    // public fields
    singleton.publicMember = 42;

    // privileged methods
    singleton.privilegedFunction = function (args) {
        
    };

    return singleton;
})(globalVariables);

// public methods
MODULE.publicFunction = function (args) {
    
};
