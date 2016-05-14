function makeInstance(args) {
    "use strict";
    var instance = {};

    // private methods
    var privateFunction = function (args) {
        
    };

    // privileged methods
    instance.privilegedFunction = function (args) {
        
    };
    
    // private fields
    var privateVariable = 3;

    // public fields
    instance.publicMember = 42;

    return instance;
}
