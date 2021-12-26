from cs1robots import *
load_world("./Jiho's worlds/Jiho's_self_made_world3.wld")
hubo=Robot(avenue=1, street=13)
hubo.set_trace("blue")
hubo.set_pause(0.1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

turn_right()
hubo.move()

for i in range(50):
    hubo.pick_beeper()