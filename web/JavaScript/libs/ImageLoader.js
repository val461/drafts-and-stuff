if (typeof loadedFiles === "undefined") { var loadedFiles = {}; }

function Img(URI) {
/* ‘URIs’: string */

    "use strict";

    // private fields
    var img;
    var ready = false;  // image fully loaded?

    // load image
    img = document.createElement("img");
    img.onload = function () {
        ready = true;
    };
    img.src = URI;

    /* return value: true iff loaded */
    this.isReady = function () {
        return ready;
    };

    /* return value: image if loaded, otherwise null */
    this.loaded = function () {
        return ready
            ? img
            : null;
    };
}

function ImageLoader(URIs) {
/* ‘URIs’: array of strings */

    "use strict";

    // private fields
    var imgs = [];
    var ready = false;

    // fill ‘imgs’
    URIs.forEach(function (uri, i) {
        imgs[i] = new Img(uri);
    });

    this.isReady = function () {
        var i = 0;
        if (!ready) {
            while (i < imgs.length && imgs[i].isReady()) {
                i += 1; // seek an unready image
            }
            if (i >= ready.length) {
                ready = true;   // unready image not found
            }
        }
        return ready;
    };

    this.loaded = function () {
        return ready
            ? imgs
            : null;
    };
}

loadedFiles["ImageLoader.js"] = true;
