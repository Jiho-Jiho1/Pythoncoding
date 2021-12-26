from cs1robots import *
load_world("./worlds/count_beepers.wld")
count_beeper_robot=Robot(avenue=6, street=1)
count_beeper_robot.set_pause(0.1)
count_beeper_robot.set_trace("blue")

def turn_right():
    for i in range(3):
        count_beeper_robot.turn_left()

count=0

def move_then_if_on_beeper_pick_beeper():
    count_beeper_robot.move()
    if count_beeper_robot.on_beeper():
        count_beeper_robot.pick_beeper()
        global count
        count += 1

count_beeper_robot.pick_beeper()

for i in range(8):
    move_then_if_on_beeper_pick_beeper()


count_beeper_robot.turn_left()
move_then_if_on_beeper_pick_beeper()
count_beeper_robot.turn_left()

move_then_if_on_beeper_pick_beeper()

for i in range(7):
    move_then_if_on_beeper_pick_beeper()

turn_right()

move_then_if_on_beeper_pick_beeper()
turn_right()
move_then_if_on_beeper_pick_beeper()

for i in range(7):
    move_then_if_on_beeper_pick_beeper()

count_beeper_robot.turn_left()
move_then_if_on_beeper_pick_beeper()
count_beeper_robot.turn_left()
move_then_if_on_beeper_pick_beeper()

for i in range(7):
    move_then_if_on_beeper_pick_beeper()

turn_right()

move_then_if_on_beeper_pick_beeper()
turn_right()
move_then_if_on_beeper_pick_beeper()

for i in range(7):
    move_then_if_on_beeper_pick_beeper()

count_beeper_robot.turn_left()
move_then_if_on_beeper_pick_beeper()
count_beeper_robot.turn_left()
move_then_if_on_beeper_pick_beeper()

for i in range(7):
    move_then_if_on_beeper_pick_beeper()

turn_right()

move_then_if_on_beeper_pick_beeper()
turn_right()
move_then_if_on_beeper_pick_beeper()

for i in range(7):
    move_then_if_on_beeper_pick_beeper()

for i in range(2):
    count_beeper_robot.turn_left()

for i in range(4):
    count_beeper_robot.move()

turn_right()

for i in range(10):
    move_then_if_on_beeper_pick_beeper()

for i in range(2):
    count_beeper_robot.turn_left()

for i in range(2):
    count_beeper_robot.move()

turn_right()

for i in range(5):
    move_then_if_on_beeper_pick_beeper()

for i in range(2):
    count_beeper_robot.turn_left()

for i in range(10):
    move_then_if_on_beeper_pick_beeper()

print(count)
