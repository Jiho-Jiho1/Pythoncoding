from cs1robots import *
load_world("./worlds/harvest3.wld")
jiho=Robot(avenue=1, street=1, beepers=100)
jiho.set_pause(0.1)

def move_and_drop():
    jiho.move()
    if not jiho.on_beeper():
        jiho.drop_beeper()

jiho.drop_beeper()

while jiho.front_is_clear():
    move_and_drop()

def turn_right():
    for i in range(3):
        jiho.turn_left()



jiho.turn_left()

while jiho.front_is_clear():
    move_and_drop()
for i in range(3):
    jiho.turn_left()

    for i in range(1):
        move_and_drop()

    jiho.turn_left()


    for i in range(5):
        move_and_drop()

    turn_right()
    jiho.move()

    turn_right()
    if not jiho.on_beeper():
        jiho.drop_beeper()

    for i in range(5):
        move_and_drop()

