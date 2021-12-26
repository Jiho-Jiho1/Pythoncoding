from cs1robots import *
load_world("./worlds/maze2.wld")
me=Robot()
me.set_trace("blue")
me.set_pause(0.1)
def turn_right():
    for i in range(3):
        me.turn_left()
while me.front_is_clear():
    me.move()
me.turn_left()

while not me.on_beeper():
    if me.right_is_clear():
        turn_right()
        me.move()

    elif me.front_is_clear():
        me.move()
    else:
        me.turn_left()