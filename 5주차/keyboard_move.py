from cs1robots import *
create_world()
key=Robot(color="yellow", beepers=100)
scene = get_scene()
while True:
    e = scene.wait()
    if e==None:
        break
    print(e.getDescription())
    print(e.getButton(), e.getKey(), e.getMouseLocation(), e.getOldMouseLocation())
    if e.getDescription() == 'keyboard':
        k = e.getKey()
        if k == 'w':
            while not key.facing_north():
                key.turn_left()
            key.move()

        elif k == 'a':
            while not key.facing_north():
                key.turn_left()
            key.turn_left()
            key.move()

        elif k == 's':
            while not key.facing_north():
                key.turn_left()
            for i in range(2):
                key.turn_left()
            key.move()

        elif k == 'd':
            while not key.facing_north():
                key.turn_left()
            for i in range(3):
                key.turn_left()
            key.move()

        elif k == ' ':
            key.drop_beeper()

        elif k == 'x':
            if key.on_beeper:
                key.pick_beeper()