/*$(document).ready(function() {
});*/

function toggleBuzzer() {
    $.post("/", {
        buzzer: 1,
        moveForward: 0,
        stopMovement: 0,
        moveBackward: 0,
        moveRight: 0,
        moveLeft: 0,
        getDistance: 0
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("error");
        }
    });
}

function moveForward() {
    $.post("/", {
        buzzer: 0,
        moveForward: 1,
        stopMovement: 0,
        moveBackward: 0,
        moveRight: 0,
        moveLeft: 0,
        getDistance: 0
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("error");
        }
    });
}

function stopMovement() {
    $.post("/", {
        buzzer: 0,
        moveForward: 0,
        stopMovement: 1,
        moveBackward: 0,
        moveRight: 0,
        moveLeft: 0,
        getDistance: 0
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("error");
        }
    });
}

function moveRight() {
    $.post("/", {
        buzzer: 0,
        moveForward: 0,
        stopMovement: 0,
        moveBackward: 0,
        moveRight: 1,
        moveLeft: 0,
        getDistance: 0
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("error");
        }
    });
}

function moveBackward() {
    $.post("/", {
        buzzer: 0,
        moveForward: 0,
        stopMovement: 0,
        moveBackward: 1,
        moveRight: 0,
        moveLeft: 0,
        getDistance: 0
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("error");
        }
    });
}

function moveLeft() {
    $.post("/", {
        buzzer: 0,
        moveForward: 0,
        stopMovement: 0,
        moveBackward: 0,
        moveRight: 0,
        moveLeft: 1,
        getDistance: 0
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("error");
        }
    });
}

function getDistance() {
    $.post("/", {
        buzzer: 0,
        moveForward: 0,
        stopMovement: 0,
        moveBackward: 0,
        moveRight: 0,
        moveLeft: 0,
        getDistance: 1
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("error");
        }
    });
}
