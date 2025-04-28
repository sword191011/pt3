def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(fan)
input.on_button_pressed(Button.B, on_button_pressed_b)

fan = 0
fan = 0

def on_forever():
    if fan == 1:
        servos.P0.run(100)
basic.forever(on_forever)

def on_forever2():
    if fan == 2:
        servos.P0.stop()
basic.forever(on_forever2)

def on_forever3():
    if fan == 0:
        servos.P0.stop()
basic.forever(on_forever3)

def on_forever4():
    global fan
    if input.temperature() > 35:
        fan = 1
basic.forever(on_forever4)

def on_forever5():
    global fan
    basic.pause(100)
    if input.temperature() < 35:
        fan = 2
basic.forever(on_forever5)
