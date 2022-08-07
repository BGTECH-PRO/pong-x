import turtle as t
from playsound import playsound

# Score varibales

player_1_score = 0
player_2_score = 0

win = t.Screen()  # creating a window
win.title("Pong")  # name to the game
win.bgcolor('black')  # color for background
win.setup(width=800, height=600)  # game play area
win.tracer(0)  # speed up the game

# Creating left paddle for the game

paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('green')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Creating a right paddle for the game

paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color('blue')
paddle_right.penup()
paddle_right.goto(350, 0)

# Creating a pong ball for the game

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball_dx = 1.5   # Setting up the pixels for the ball movement.
ball_dy = 1.5

# Creating a pen for updating the Score

pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0                    Player 2: 0 ", align="center", font=(
    'Monaco', 24, "normal"))

# Moving the left Paddle using the keyboard


def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)

# Moving the left paddle down


def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)

# Moving the right paddle up


def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)

# Moving right paddle down


def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)

# Keyboard binding


win.listen()
win.onkeypress(paddle_left_up, "a")
win.onkeypress(paddle_left_down, "z")
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")

# Main Game Loop

while True:
    win.update()  # This methods is mandatory to run any game

    # Moving the ball

    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border

    if ball.ycor() > 290:   # Right top paddle Border
        ball.sety(290)
        ball_dy = ball_dy * -1
    if ball.ycor() < -290:  # Left top paddle Border
        ball.sety(-290)
        ball_dy = ball_dy * -1
    if ball.xcor() > 390:   # right width paddle Border
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_1_score = player_1_score + 1
        pen.clear()
        pen.write("Player 1: {}                    Player 2: {} ".format(
            player_1_score, player_2_score), align="center", font=(
                'Monaco', 24, "normal"))
        playsound('wallhit.wav')
    if(ball.xcor()) < -390:  # Left width paddle Border
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_2_score = player_2_score + 1
        pen.clear()
        pen.write("Player 1: {}                    Player 2: {} ".format(
            player_1_score, player_2_score), align="center", font=(
                'Monaco', 24, "normal"))
        playsound('wallhit.wav')

    # Handling the collisions with paddles.
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < paddle_right.ycor() + 40 and ball.ycor(
                ) > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        playsound('paddle.wav')
    if(ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < paddle_left.ycor() + 40 and ball.ycor(
                ) > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        playsound('paddle.wav')
