import turtle
import time
import random


# Screen setup

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)


# Snake head

head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# Snake food

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(0, 100)


# Scoreboard

score = 0
high_score = 0

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(
    "Score: 0  High Score: 0",
    align="center",
    font=("Courier", 18, "normal")
)


# Snake body segments

segments = []


# Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

def reset_game():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    score = 0
    scoreboard.clear()
    scoreboard.write(
        f"Score: {score}  High Score: {high_score}",
        align="center",
        font=("Courier", 18, "normal")
    )


# Keyboard bindings

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


# Main game loop

delay = 0.1

while True:
    screen.update()

    # Wall collision
    if (
        head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290
    ):
        reset_game()

    # Food collision
    if head.distance(food) < 20:
        food.goto(
            random.randint(-280, 280),
            random.randint(-280, 280)
        )

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        scoreboard.clear()
        scoreboard.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Courier", 18, "normal")
        )

    # Move body
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(
            segments[i - 1].xcor(),
            segments[i - 1].ycor()
        )

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    time.sleep(delay)
