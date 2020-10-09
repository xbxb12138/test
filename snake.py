from turtle import *
from gamebase import square
from random import randrange

snake=[[0,0],[10,0],[20,0]]
apple_x=randrange(-20,18)*10
apple_y=randrange(-19,19)*10
aim_x=10
aim_y=0

def change(x,y):
    global aim_x,aim_y
    aim_x=x
    aim_y=y

def inside_snake():
    for n in range(len(snake)-1):
        if snake[-1][0]==snake[n][0] and snake[-1][1]==snake[n][1]:
            return True
    return False

def inside_map():
    if -200<=snake[-1][0]<=180 and -190<=snake[-1][1]<=190:
        return True
    else:
        return False

def gameLoop():
    global apple_x,apple_y
    snake.append([snake[-1][0]+aim_x,snake[-1][1]+aim_y])
    if (not inside_map()) or inside_snake():
        square(snake[-1][0],snake[-1][1],10,"gray")
        return
    if snake[-1][0]!=apple_x or snake[-1][1]!=apple_y:
        snake.pop(0)
    else :
        apple_x=randrange(-20,18)*10
        apple_y=randrange(-19,19)*10
    clear()
    square(-210,-200,410,"green")
    square(-200,-190,390,"white")
    square(apple_x,apple_y,10,"pink")
    for n in range(len(snake)):
        square(snake[n][0],snake[n][1],10,"orange")
    ontimer(gameLoop,100)
    update()

setup(420,420,0,0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(0,10),"w")
onkey(lambda: change(-10,0),"a")
onkey(lambda: change(0,-10),"s")
onkey(lambda: change(10,0),"d")
gameLoop()
done()