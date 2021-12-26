from cs1robots import *
#load_world("C:/Users/jihoi/OneDrive/Desktop/파이썬 공부 - Visual Studio Code/worlds/newspaper.wld")
load_world("./worlds/fairy_tale.wld")
hubo=Robot(avenue=1, street=6, beepers=30)

hubo.set_trace("blue")
hubo.set_pause(0.1)

for i in range(3):
    hubo.move()

def turn_right():
    for i in range(3):
        hubo.turn_left()

turn_right()

for i in range(5):
    hubo.move()
    hubo.drop_beeper()

hubo.turn_left()

for i in range(3):
    hubo.drop_beeper()

hubo.pick_beeper()

for i in range(2):
    turn_right()

hubo.move()


