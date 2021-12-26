from cs1robots import *
create_world()
jiho=Robot(avenue=1, street=1, beepers=5, color="yellow")
jiho.set_trace("blue")
jiho.set_pause(0.1)

dad=Robot(avenue=1, street=2, beepers=100, color="purple")
dad.set_trace("blue")
dad.set_pause(0.1)

mom=Robot(avenue=1, street=3, beepers=5, color="light_blue")
mom.set_trace("blue")
mom.set_pause(0.1)


def turn_right(robot):
    for i in range(3):
        robot.turn_left()

def move_n(n,robot):
    for i in range(n):
        robot.move()

move_n(8,mom)