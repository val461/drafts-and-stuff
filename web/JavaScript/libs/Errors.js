if (typeof loadedFiles === "undefined") { var loadedFiles = {}; }


/* input errors */
function InputError(message) {
  this.message = message;
  this.stack = (new Error()).stack;
}
InputError.prototype = Object.create(Error.prototype);
InputError.prototype.name = "InputError";


/* assertions */
function AssertionFailed(message) {
  this.message = message;
  this.stack = (new Error()).stack;
}
AssertionFailed.prototype = Object.create(Error.prototype);
AssertionFailed.prototype.name = "AssertionFailed";

function assert(test, message) {
  if (!test)
    throw new AssertionFailed(typeof message === "undefined" ? "" : message);
}


loadedFiles["Errors.js"] = true;
