import turtle
turtle.speed(0)
turtle.hideturtle()
def draw_square(x,y):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y+50)
    turtle.goto(x+50,y+50)
    turtle.goto(x+50,y)
    turtle.goto(x,y)
    turtle.end_fill()


def draw_triangle(x,y):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x+30,y)
    turtle.pendown()
    turtle.goto(x+50,y+100)
    turtle.goto(x+70,y)
    turtle.goto(x+30,y)
    turtle.end_fill()



turtle.onscreenclick(draw_square, btn=1,add=True)
turtle.onscreenclick(draw_triangle, btn=3,add=True)

#switching colors
def switch_color1():
    turtle.color("red")
turtle.getscreen().onkeypress(switch_color1,"r")
turtle.getscreen().listen()

def switch_color2():
    turtle.color("pink")
turtle.getscreen().onkeypress(switch_color2,"p")
turtle.getscreen().listen()

def switch_color3():
    turtle.color("blue")
turtle.getscreen().onkeypress(switch_color3,"b")
turtle.getscreen().listen()


def switch_color4():
    turtle.color("orange")
turtle.getscreen().onkeypress(switch_color4,"o")
turtle.getscreen().listen()







turtle.mainloop()
