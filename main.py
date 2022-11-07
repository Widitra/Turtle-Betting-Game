from turtle import Turtle, Screen
import random

is_race_on = False
is_there_a_winner = False
screen = Screen()
screen.setup(width=600, height=500)
turtle_color = ["pink", "red", "orange", "yellow", "green", "blue", "purple", "black"]
y_position = [175, 125, 75, 25, -25, -75, -125, -175]
all_turtle = []
all_players_bet = []

for turtle_index in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-270, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

num_players = int(screen.textinput(title="Number of Players", prompt="How many players are playing? "))
for player in range(0, num_players):
    current_bet = screen.textinput(title="Player's bet", prompt=f"Input color bet for player {player+1}")
    all_players_bet.append(current_bet)

is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 260:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            for player in range(0, len(all_players_bet)):
                if all_players_bet[player] == winning_turtle:
                    print(f"the {winning_turtle} turtle got 1st place! The winner is player {player+1}!")
                    is_there_a_winner = True
            if not is_there_a_winner:
                print(f"the {winning_turtle} turtle got 1st place! None of the players won the match!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
