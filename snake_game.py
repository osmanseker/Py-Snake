from tkinter import *
import random
from turtle import window_height, window_width

#constants
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"




class Snake:
    def __init__(self) -> None:
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0,])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food: 
    def __init__(self):
        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x,y,x+SPACE_SIZE, y +SPACE_SIZE, fill = FOOD_COLOR, tag="food")

def next_turn(snake, food):
    
    x,y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -=SPACE_SIZE
    elif direction == "right":
        x +=SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE,fill=SNAKE_COLOR)
    
    snake.squares.insert(0,square)
    del snake.coordinates[-1]  
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]


    window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions():
    pass

def game_over():
    pass


window = Tk()
window.title("Python Snake Game")

score = 0
direction = 'down'

label = Label(window, text="Score:{}". format(score), font=("courier", 40))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()
next_turn(snake, food)


window.mainloop()