from turtle import *

bgcolor('white')
penup()
goto(-80, 80)
pendown()

speed(0)
pencolor('#3DDC84')


def cir():
    begin_fill()
    fillcolor('white')
    circle(7)
    end_fill()


# Drawing the head


def draw_head():
    begin_fill()
    fillcolor('#3DDC84')
    forward(150)
    left(90)

    for i in range(238):
        left(0.76)
        forward(1)
    end_fill()

    # drawing eyes
    # left eye
    penup()
    goto(-46, 120)
    pendown()
    cir()

    # right eye
    penup()
    goto(24, 120)
    pendown()
    cir()

    # drawing ears
    # left ear
    penup()
    goto(-40, 140)
    pendown()

    pensize(4)
    right(140)
    forward(50)

    # right ear
    penup()
    goto(34, 144)
    pendown()

    pensize(4)
    right(80)
    forward(46)


# Drawing the middle body


def draw_middlebody():
    begin_fill()
    fillcolor('#3DDC84')
    pensize(1)

    right(141)
    forward(100)

    for _ in range(20):
        forward(1)
        left(5)
    right(9.5)
    forward(127)

    for _ in range(20):
        forward(1)
        left(5)
    right(9.5)
    forward(100)
    end_fill()

# hand


def draw_hand():
    begin_fill()
    fillcolor('#3DDC84')
    for _ in range(45):
        right(4)
        forward(1)
    forward(70)
    for _ in range(45):
        right(4)
        forward(1)
    forward(70)
    end_fill()

# legs


def draw_legs():
    begin_fill()
    fillcolor('#3DDC84')
    right(91)
    forward(30)
    right(90)
    forward(50)

    for _ in range(45):
        right(4)
        forward(1)
    end_fill()


draw_head()

penup()
goto(-80, 68)
pendown()

draw_middlebody()

penup()
goto(80, 68)
pendown()

draw_hand()

penup()
goto(-124, 70)
pendown()

draw_hand()

penup()
goto(-50, -50)
pendown()

draw_legs()

penup()
goto(14, -50)
pendown()
left(1.7)
draw_legs()

hideturtle()
exitonclick()
