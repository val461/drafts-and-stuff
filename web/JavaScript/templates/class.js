function makeInstance(args) {
    "use strict";
    var instance = {};

    // private fields
    var privateVariable = 3;

    // private methods
    function privateFunction(args) {
        
    }

    // public fields
    instance.publicMember = 42;

    // privileged methods
    instance.privilegedFunction = function (args) {
        
    };
    
    return instance;
}
