input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(fan)
})
let fan = 0
fan = 0
basic.forever(function () {
    if (fan == 1) {
        servos.P0.run(100)
    }
})
basic.forever(function () {
    if (fan == 2) {
        servos.P0.stop()
    }
})
basic.forever(function () {
    if (fan == 0) {
        servos.P0.stop()
    }
})
basic.forever(function () {
    if (input.temperature() > 35) {
        fan = 1
    }
})
basic.forever(function () {
    basic.pause(100)
    if (input.temperature() < 35) {
        fan = 2
    }
})
