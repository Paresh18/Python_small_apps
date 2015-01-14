
#This is a small drawing app.

#importing the turtle module
import turtle
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.fd(100)
        some_turtle.rt(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    draw_square(brad)
    for i in range(1,36):
        draw_square(brad)
        brad.rt(10)
    angie =turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
    window.exitonclick()
	
#calling the function    
draw_art()
