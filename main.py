import turtle
import random
from turtle import Turtle as t, Screen
tim = t()
tim.speed("fastest")
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]




##################################          Draw any polygon          ##################################                
def draw_shape(num_of_sides):
    for _ in range(num_of_sides):
        tim.forward(50)
        tim.right(360/num_of_sides)

for _ in range (3,11):
    tim.color(random.choice(colours))
    draw_shape()




##################################          Random Walk          ##################################                



step_size = 30
step_number = 200
directions = [tim.right, tim.left, tim.forward ,tim.back]
tim.pensize(15)
for _ in range(step_number):
    tim.color(random_color())
    move_in_a_direction = random.choice(directions)

    if move_in_a_direction in [tim.forward, tim.back]:
        move_in_a_direction(step_size)  
    else:
        move_in_a_direction(90) 


##################################         Amazing piece of art       ##################################                

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        tim.color(c)
        tim.forward(steps)
        tim.right(30)


##################################          Draw Spirograph        ##################################                


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()