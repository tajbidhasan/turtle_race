import random
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500,height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Makr your bet", prompt="which turtle wil win the race? Enter a color: ")
colors = ["red", "orange","yellow","blue","purple"]
all_turtle =[]

line = -100
for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=line)
    line += 45
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:

                print(f"You lost! The {winning_color} turtle is the winner!")



        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
