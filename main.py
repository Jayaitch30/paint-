import turtle
import os
import winsound


canvas = turtle.Screen()
pen = turtle.Turtle()

def init():
    canvas.setup(1000, 800)
    canvas.bgpic(os.path.join('resources_paint', 'paint_screen.gif'))
    canvas.title("Paint")
    pen.shape("circle")
    pen.shapesize(0.5)
    pen.speed('fastest')
    pen.pensize(4)
    winsound.PlaySound(os.path.join('resources_paint', 'oliver_twist'), winsound.SND_ASYNC)
    game()
def game():
    def dragging(x, y):
        if x > -100 and y < 245 and x < 465 and y > -270:
            pen.pendown()
            pen.ondrag(None)
            pen.setheading(pen.towards(x, y))
            pen.goto(x, y)
            pen.ondrag(dragging)
    def changepos(x, y):
        if x > -100 and y < 245 and x < 465 and y > -270:
            pen.penup()
            pen.onrelease(None)
            pen.goto(x, y)
    def check_event(x,y):
        if x > -100 and y < 245 and x < 465 and y > -270:
            changepos(x,y)
        if x > -432 and x < -377 and y > 137 and y < 192:
            pen.color("blue")
        if x > -432 and x < -377 and y > 67 and y < 122:
            pen.color("green")
        if x > -432 and x < -377 and y > -3 and y < 52:
            pen.color("red")
        if x > -432 and x < -377 and y > -73 and y < -18:
            pen.color("purple")
        if x > -320 and x < -265 and y > 137 and y < 192:
            pen.color("yellow")
        if x > -320 and x < -265 and y > 67 and y < 122:
            pen.color("magenta")
        if x > -320 and x < -265 and y > -3 and y < 52:
            pen.color("orange")
        if x > -320 and x < -265 and y > -73 and y < -18:
            pen.color("black")
        if x > -330 and x < -230 and y > -142 and y < -79:
            pen.color("white")
        if x > -440 and x < -350 and y > -138 and y < -80:
            pen.stamp()
        if x > -330 and x < -230 and y > -227 and y < -165:
            pen.clear()

    turtle.onscreenclick(check_event)
    pen.ondrag(dragging)
    canvas.listen()
init()
canvas.mainloop()
