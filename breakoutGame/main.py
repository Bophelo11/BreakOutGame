import turtle as tr
from paddle import Paddle
from ball import Ball
from Tjovitjo import Bricks
import time
from graphicalUserInter import GUI
from scoreboard import Scoreboard


screen = tr.Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("white")
screen.title("Brehhhkahhhhht")
screen.tracer(0)

gui = GUI()
gui.header()

paddle = Paddle()
bricks = Bricks()
ball = Ball()
scoreboard = Scoreboard(lives=5)

game_paused = False
game_is_on = True

def pause():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True

screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)

def Wall_cont_Det():
    #Both Left & right walls
    global ball
    if ball.xcor() < -500 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
    #topsided wall
    if ball.ycor() < 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return
    #bottomsided wall
    if ball.ycor() < -280:
        ball.reset()
        return

def paddle_cont_det():
    global ball, paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    #if Paddle is on the Right of the screen

    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        if paddle_x > 0:
            ball.bounce(x_bounce=True, y_bounce=True)
            return
        else:
            ball.bounce(x_bounce=False,y_bounce=True)
            return

    elif paddle_x < 0:
        if ball_x < paddle_x:
            ball.bounce(x_bounce=False, y_bounce=True)
            return
        else:
            ball.bounce(x_bounce=False, y_bounce=True)
            return
    else:
        if ball_x > paddle_x:
            ball.bounce(x_bounce=True, y_bounce=True)
            return
        elif ball_x < paddle_x:
            ball.bounce(x_bounce=True, y_bounce=True)
            return
        else:
            ball.bounce(x_bounce=False, y_bounce=True)
            return



def brick_cont_det():
    global ball,bricks

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000,3000)
                bricks.bricks.remove(brick)

            if ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False,y_bounce=True)

            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)



while game_is_on:
    if not game_paused:
        screen.update()
        time.sleep(0.01)
        ball.move()

        Wall_cont_Det()
        paddle_cont_det()
        brick_cont_det()
        if len(bricks.bricks) == 0:
            gui.chaile(win=True)
            break

        else:
            gui.game_paused()



tr.mainloop()