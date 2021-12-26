from cs1robots import *
load_world("./worlds/harvest1.wld")
hubo=Robot(avenue=1, street=6)
hubo.set_trace("purple")
hubo.set_pause(0.1)

while hubo.front_is_clear():
    hubo.move()
    hubo.pick_beeper()

def turn_right():
    for i in range(3):
        hubo.turn_left()

turn_right()

while hubo.front_is_clear():
    hubo.move()
    hubo.pick_beeper()

turn_right()

for i in range(5):
    hubo.move()
    hubo.pick_beeper()

turn_right()

for i in range(4):
    hubo.move()
    hubo.pick_beeper()

turn_right()

for i in range(4):
    hubo.move()
    hubo.pick_beeper()

turn_right()

for i in range(3):
    hubo.move()
    hubo.pick_beeper()

turn_right()

for i in range(3):
    hubo.move()
    hubo.pick_beeper()

turn_right()

for i in range(2):
    hubo.move()
    hubo.pick_beeper()

turn_right()

for i in range(2):
    hubo.move()
    hubo.pick_beeper()

turn_right()

hubo.move()
hubo.pick_beeper()

turn_right()

hubo.move()
hubo.pick_beeper()