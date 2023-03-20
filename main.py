from turtle import Turtle, Screen

tim= Turtle()
screen=Screen()

#move forward on click of W
def move_forwards():
    tim.forward(10)

#move backwards on click of S
def move_backwards():
    tim.backward(10)

#move left on click of A
def move_left():
    tim.left(10)
#move right on click of D
def move_right():
    tim.right(10)

#clear the screen and recenter the turtle
def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()

