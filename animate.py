import random
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=250)
tk.title("cool")
canvas.pack()

class Ball:
    def __init__(self):
        self.ball =canvas.create_oval(10, 10, 60, 60, fill="orange")
        self.xspeed = 1
        self.yspeed = 2
        self.shape = "circle"
        

    def move(self):
        pos = canvas.coords(self.shape)
        if pos[3] >= 250 or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= 500 or pos[0] <= 0:
            self.xspeed = -self.xspeed

newball = Ball()
    
while True:
    newball.move()
    tk.update()
    time.sleep(0.01)
    
tk.mainloop()
