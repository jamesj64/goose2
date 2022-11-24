/*$(document).ready(function() {
});*/

function toggleBuzzer() {
    $.post("/", {
        buzzer: 1,
        moveForward: 0,
        stopMovement: 0
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
        stopMovement: 0
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
        stopMovement: 1
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("error");
        }
    });
}