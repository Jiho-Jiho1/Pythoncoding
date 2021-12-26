from cs1robots import *
create_world()
hubo=Robot()
hubo.set_trace("red")
hubo.set_pause(0.1)
for i in range(4):
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()

def turn_right():
    for i in range(3):
        hubo.turn_left()

for i in range(9):
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
