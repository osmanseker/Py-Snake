from tkinter import *
import random

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
    pass

class Food: 
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

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





window.mainloop()