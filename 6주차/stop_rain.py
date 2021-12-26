from cs1robots import *
load_world("./worlds/rain1.wld")
stop_rain=Robot(avenue=2, street=6, beepers=51)
stop_rain.set_pause(0.1)
stop_rain.set_trace("blue")

def turn_right():
        for i in range(3):
            stop_rain.turn_left()

stop_rain.move()
stop_rain.drop_beeper()
turn_right()
stop_rain.move()
while not stop_rain.on_beeper():
    if stop_rain.right_is_clear():
        turn_right()
        stop_rain.move()
        if stop_rain.right_is_clear():
            for i in range(2):
                stop_rain.turn_left()
            stop_rain.move()
            stop_rain.drop_beeper()
            turn_right()
            stop_rain.move()
    elif stop_rain.front_is_clear():
        stop_rain.move()
    else:
        stop_rain.turn_left()