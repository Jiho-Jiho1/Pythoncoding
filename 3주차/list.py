from cs1robots import *
create_world()
jiho=Robot(avenue=1, street=1, beepers=5, color="yellow")
jiho.set_trace("blue")
jiho.set_pause(0.3)

dad=Robot(avenue=1, street=2, beepers=100, color="purple")
dad.set_trace("blue")
dad.set_pause(0.3)

mom=Robot(avenue=1, street=3, beepers=5, color="light_blue")
mom.set_trace("blue")
mom.set_pause(0.3)
 
list1=[]
list1.append(jiho)
list1.append(mom)
list1.append(dad)
for i in range(9):
    for n in list1:
        n.move()