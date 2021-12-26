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

for i in range(9):
    jiho.move()
    dad.move()
    mom.move()
#turn_right(mom)