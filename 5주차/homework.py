from cs1robots import *
load_world("./worlds/rain1.wld")
stop_rain=Robot(avenue=2, street=6, beepers=50)
stop_rain.set_pause(0.1)
stop_rain.set_trace("blue")

def turn_right():
        for i in range(3):
            stop_rain.turn_left()

def first_and_second_windows():
    for i in range(2):
        stop_rain.move()

    stop_rain.turn_left()

    for i in range(2):
        stop_rain.move()

    stop_rain.drop_beeper()


    turn_right()

    for i in range(2):
        stop_rain.move()

    stop_rain.drop_beeper()

first_and_second_windows()

def third_window():
    for i in range(2):
        stop_rain.move()

    turn_right()

    stop_rain.move()

    stop_rain.drop_beeper()

third_window()

stop_rain.move()

def fourth_and_fifth_windows():

    for i in range(2):
        stop_rain.move()

    turn_right()

    stop_rain.move()

    stop_rain.drop_beeper()

    turn_right()

fourth_and_fifth_windows()

stop_rain.turn_left()

for i in range(2):
    stop_rain.move()

stop_rain.drop_beeper()