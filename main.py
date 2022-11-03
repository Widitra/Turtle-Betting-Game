from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=400)
turtle_color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [125, 75, 25, -25, -75, -125]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-270, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 260:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won the bet! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost the bet! The {winning_turtle} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
