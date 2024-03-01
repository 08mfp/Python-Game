from tkinter import Canvas, TRUE, FALSE, Tk
import random
import time

"""
Mohamed Farid Patel
March 2024
"""

window = Tk()
window.title("Bing Bong Ping Pong")
window.resizable(FALSE,FALSE)
storyboard = Canvas(window,width=1000,height=580)
storyboard.config(background="#DCB2CD")
storyboard.pack()
window.update()

class Button_1:
    def __init__(self,storyboard,color):
        self.storyboard = storyboard
        self.id = self.storyboard.create_rectangle(0,250,30,360,fill=color)
        self.storyboard.bind_all("w",self.up)
        self.storyboard.bind_all("s",self.down)
        self.storyboardh=self.storyboard.winfo_height()
        self.storyboardw=self.storyboard.winfo_width()
        self.xvalue = 0
   

    def place_grid(self):
        self.storyboard.move(self.id,0,self.xvalue)
        position = self.storyboard.coords(self.id)
        if position[1] <= 0:
            self.xvalue = 0
        if position[3] >= 600:
            self.xvalue = -0

    def up(self,e):
        self.xvalue = -7.5

    def down(self,e):
        self.xvalue = 7.5

class Button_2:
    def __init__(self,storyboard,color):
        self.storyboard = storyboard
        self.id = self.storyboard.create_rectangle(970,250,1010,360,fill=color)
        self.storyboard.bind_all("<KeyPress-Up>",self.up)
        self.storyboard.bind_all("<KeyPress-Down>",self.down)
        self.storyboardh=self.storyboard.winfo_height()
        self.storyboardw=self.storyboard.winfo_width()
        self.xvalue = 0

    def place_grid(self):
        self.storyboard.move(self.id,0,self.xvalue)
        position = self.storyboard.coords(self.id)
        if position[1] <= 0:
            self.xvalue = 0
        if position[3] >= 600:
            self.xvalue = 0

    def up(self,e):
        self.xvalue = -7.5

    def down(self,e):
        self.xvalue = 7.5

class Main:
    def __init__(self,storyboard,button2,button1,color):
        self.storyboard = storyboard
        self.id = self.storyboard.create_oval(15,15,40,40,fill = color)
        self.storyboard.move(self.id,400,300)
        self.storyboardh=self.storyboard.winfo_height()
        self.storyboardw=self.storyboard.winfo_width()
        self.yvalue = random.choice([-5,5])
        self.xvalue = -5
        self.button1 = button1
        self.button2 = button2
        self.scoreplayer1 = 0
        self.displayscore1 = None
        self.scoreplayer2 = 0
        self.displayscore2 = None

    def place_grid(self):
        self.storyboard.move(self.id,self.yvalue,self.xvalue)
        position = self.storyboard.coords(self.id)
        if position[0] <= 0:
            self.yvalue = 5
            self.scoreplayer2 = self.scoreplayer2 + 1
            self.storyboard.move(self.id,400,300)
            self.checkscore2(self.scoreplayer2)
        if position[1] <= 0:
            self.xvalue = 5
        if position[2] >= self.storyboardw:
            self.yvalue = -5
            self.scoreplayer1 = self.scoreplayer1 + 1
            self.storyboard.move(self.id,-400,-300)
            self.checkscore1(self.scoreplayer1)
        if position[3] >= self.storyboardh:
            self.xvalue =-5
        if self.button1_collision(position):
            self.yvalue = 5
        if self.button2_collision(position):
            self.yvalue = -5

    def button1_collision(self,position):
        button1_position = self.storyboard.coords(self.button1.id)
        if position[0] <= button1_position[2] and position[2] >= button1_position[0]:
            if position[3] <= button1_position[3] and position[3] >= button1_position[1]:
                return TRUE 
            return FALSE

    def checkscore1(self,value):
        self.storyboard.delete(self.displayscore1)
        self.displayscore1 = self.storyboard.create_text(200,25, text= "Player 1 score: " + str(value), font=("Times Bold",30),fill="#36454F")

    def button2_collision(self,position):
        button1_position = self.storyboard.coords(self.button2.id)
        if position[0] <= button1_position[2] and position[2] >= button1_position[0]:
            if position[3] >= button1_position[1] and position[3] <= button1_position[3]:
                return TRUE
            return FALSE

    def checkscore2(self,value):
        self.storyboard.delete(self.displayscore2)
        self.displayscore2 = self.storyboard.create_text(800,25, text= "Player 2 score: " + str(value), font=("Times Bold",30),fill="#36454F")


def run_game():
    button1 = Button_1(storyboard,"#36454F")
    button2 = Button_2(storyboard,"#36454F")       
    pingpong = Main(storyboard,button2,button1,"#36454F")

    while True:
        button1.place_grid()
        button2.place_grid()
        pingpong.place_grid()
        window.update()
        time.sleep(0.005)

run_game()
window.mainloop()
