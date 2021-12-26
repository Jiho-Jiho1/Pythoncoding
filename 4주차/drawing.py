from cs1graphics import *
import time
canvas=Canvas(w=1600, h=1600, bgColor="light blue", title='Drawing Canvas')
square0=Square(size=100)


canvas.add(square0)
square0.setFillColor("red")
square0.moveTo(200, 200)
for i in range(60):
    square0.move(10, 0)
    time.sleep(0.1)
square0.rotate(45)
for i in range(80):
    time.sleep(0.1)
    square0.scale(0.95)
canvas.remove(square0)

circle0=Circle(100)
canvas.add(circle0)
circle0.setFillColor("yellow")
circle0.moveTo(200, 200)
for i in range(60):
    circle0.move(10, 0)
    time.sleep(0.1)
circle0.rotate(45)
for i in range(80):
    time.sleep(0.1)
    circle0.scale(0.95)
canvas.remove(circle0)
text0=Text(message='Hello -> Bye Bye', fontsize=12)
canvas.add(text0)
text0.setFontColor('purple')
text0.moveTo(0,0)