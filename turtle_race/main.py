from turtle import Turtle, Screen
import random

# Constants
WIDTH, HEIGHT = 500, 400
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [-70, -40, -10, 20, 50, 80]

def setup_race():
    """
    Sets up the race environment and initializes turtles.
    """
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    
    if user_bet in COLORS:
        race_in_progress = True
    else:
        race_in_progress = False
        print("Invalid input or no bet made. Exiting.")
        screen.bye()
        return
    
    all_turtles = []
    for index, color in enumerate(COLORS):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=-230, y=Y_POSITIONS[index])
        all_turtles.append(new_turtle)
    
    run_race(all_turtles, user_bet, screen)

def run_race(turtles, user_bet, screen):
    """
    Runs the race until one turtle reaches the finish line.
    """
    while True:
        for turtle in turtles:
            if turtle.xcor() > (WIDTH // 2 - 30):
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                screen.bye()
                return
            
            turtle.forward(random.randint(0, 10))

setup_race()
