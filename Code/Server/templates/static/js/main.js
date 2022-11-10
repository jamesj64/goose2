let buzzerState = 0;

$(document).ready(function() {
    console.log("HII");
    /*$.post("/", {
        kittens: 123456789
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("FUCK THIS");
        }
    });*/
});

function toggleBuzzer() {
    buzzerState = buzzerState == 0 ? 1 : 0;
    $.post("/", {
        buzzer: buzzerState
    }, function(err, req, resp) {
        if (req == "success") {
            console.log("what the?! it works!");
        } else {
            console.log("FUCK THIS");
        }
    });
}