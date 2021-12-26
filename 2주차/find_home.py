from tkinter.constants import E
from cs1robots import *
create_world()
jiho=Robot(avenue=9, street=5, orientation="W")
jiho.set_trace("blue")
jiho.set_pause(0.1)

jiho.facing_north()

def find_home():
    while not jiho.facing_north():
        jiho.turn_left()
    for i in range(2):
        jiho.turn_left()

        while jiho.front_is_clear():
            jiho.move()

find_home()