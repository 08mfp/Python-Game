# MARCH 2024
# MOHAMED FARID PATEL
# PING PONG STYLE GAME
# TESTED FOR MAC OS

from tkinter import Tk, Canvas, Button, Label, FALSE, TRUE, LEFT, RIGHT, BOTTOM
import random, time
window = Tk()
window.geometry("1000x580")
window.resizable(FALSE,FALSE)

def outerloop():
    """Outer Loop used to start game when user presses 'start' button
    """

    def innerloop():
        """Inner loop used to return to welcome page every time function is called
        Returns:
            Canvas: Returns User to previous page
        """

        #destroy() function ensures test is not duplicated when returning to that window
        welcomemessage.destroy()
        startbutton.destroy()
        aboutsection1.destroy() 
        aboutsection2.destroy()
        aboutsection3.destroy()
        window = Tk()
        window.title("Bing Bong Ping Pong")
        window.resizable(FALSE,FALSE)
        storyboard = Canvas(window,width=1000,height=580)
        storyboard.config(background="#DCB2CD")
        #used to create dashed line to create appearance of ping pong table. Multiple lines created to add with. 2 colours used for depth effect.
        storyboard.create_line(498, 0, 498, 578, dash=(35, 25), tags="splitDistance", fill="#36454F")
        storyboard.create_line(499, 0, 499, 579, dash=(35, 25), tags="splitDistance", fill="#000000")
        storyboard.create_line(500, 0, 500, 580, dash=(35, 25), tags="splitDistance", fill="#36454F")
        storyboard.create_line(501, 0, 501, 581, dash=(35, 25), tags="splitDistance", fill="#000000")
        storyboard.create_line(502, 0, 502, 582, dash=(35, 25), tags="splitDistance", fill="#36454F")
        storyboard.pack()
        #update window to ensure that all functions are correctly recalled/executed
        window.update()


        class Button_1:

            def __init__(self,storyboard,color):
                """Sets required variables and dimensions to configure object
                Args:
                    storyboard (Canvas): Main Canvas specifications stored here
                    color (variable): Allows code store color, for future use in objects (fill function)
                """
                self.storyboard = storyboard
                self.id = self.storyboard.create_rectangle(0,250,30,360,fill=color)
                self.storyboard.bind_all("w",self.up)
                self.storyboard.bind_all("s",self.down)
                self.storyboardh=self.storyboard.winfo_height()
                self.storyboardw=self.storyboard.winfo_width()
                self.xvalue = 0

            def place_grid(self):
                """Places left button onto canvas
                """

                #ensure objects are placed within dimensions of canvas
                self.storyboard.move(self.id,0,self.xvalue)
                position = self.storyboard.coords(self.id)
                if position[1] <= 0:
                    self.xvalue = 0
                if position[3] >= 600:
                    self.xvalue = -0

            def up(self,e):
                """used to define movement of object when key is pressed
                """

                self.xvalue = -7.5

            def down(self,e):
                """used to define movement of object when key is pressed
                """

                self.xvalue = 7.5


        class Button_2:

            def __init__(self,storyboard,color):
                """Sets required variables and dimensions to configure object
                Args:
                    storyboard (Canvas): Main Canvas specifications stored here
                    color (variable): Allows code store color, for future use in objects (fill function)
                """

                self.storyboard = storyboard
                self.id = self.storyboard.create_rectangle(970,250,1010,360,fill=color)
                self.storyboard.bind_all("<KeyPress-Up>",self.up)
                self.storyboard.bind_all("<KeyPress-Down>",self.down)
                self.storyboardh=self.storyboard.winfo_height()
                self.storyboardw=self.storyboard.winfo_width()
                self.xvalue = 0

            def place_grid(self):
                """Places right button onto canvas
                """

                #ensure objects are placed within dimensions of canvas
                self.storyboard.move(self.id,0,self.xvalue)
                position = self.storyboard.coords(self.id)
                if position[1] <= 0:
                    self.xvalue = 0
                if position[3] >= 600:
                    self.xvalue = 0

            def up(self,e):
                """used to define movement of object when key is pressed
                """

                self.xvalue = -7.5

            def down(self,e):
                """used to define movement of object when key is pressed
                """

                self.xvalue = 7.5


        class Main:

            def __init__(self,storyboard,button2,button1,color):
                """Sets required variables and dimensions to configure moving obkect (ball)
                Args:
                    storyboard (Canvas): Main Canvas specifications stored here
                    button2 (Object): Used by user to control right button
                    button1 (Object): Used by user to control left button
                    color (Variable): Allows code store color, for future use in objects (fill function)
                """

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
                """Used to place ball on grid
                """

                self.storyboard.move(self.id,self.yvalue,self.xvalue)
                position = self.storyboard.coords(self.id)

                #define all ball collisions
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
                """Used to configure collision detection for object
                Args:
                    position (coordinate): If the ball has exact/similar coordinates as button(means that button will hit ball)
                Returns:
                    Boolean: Whether object bounces or not
                """

                button1_position = self.storyboard.coords(self.button1.id)
                #define when ball, bounces off button
                if position[0] <= button1_position[2] and position[2] >= button1_position[0]:
                    if position[3] <= button1_position[3] and position[3] >= button1_position[1]:
                        return TRUE 
                    return FALSE

            def checkscore1(self,value):
                """Deletes previous score for user and updates with new value that is stored in variable
                Args:
                    value (integer): Stores user score
                """

                self.storyboard.delete(self.displayscore1)
                self.displayscore1 = self.storyboard.create_text(200,25, text= "Player 1 score: " + str(value), font=("Times Bold",30),fill="#36454F")

            def button2_collision(self,position):
                """Used to configure collision detection for object

                Args:
                    position (coordinate): If the ball has exact/similar coordinates as button(means that button will hit ball)

                Returns:
                    Boolean: Whether object bounces or not
                """

                button1_position = self.storyboard.coords(self.button2.id)
                #define when ball, bounces off button
                if position[0] <= button1_position[2] and position[2] >= button1_position[0]:
                    if position[3] >= button1_position[1] and position[3] <= button1_position[3]:
                        return TRUE
                    return FALSE

            def checkscore2(self,value):
                """Deletes previous score for user and updates with new value that is stored in variable
                Args:
                    value (integer): Stores user score
                """

                self.storyboard.delete(self.displayscore2)
                self.displayscore2 = self.storyboard.create_text(800,25, text= "Player 2 score: " + str(value), font=("Times Bold",30),fill="#36454F")

        def run_game():
            """Function used to place all previously configured objecrs on grid, and continue running loop to allow objects to continue moving
            """

            button1 = Button_1(storyboard,"#36454F")
            button2 = Button_2(storyboard,"#36454F")       
            pingpong = Main(storyboard,button2,button1,"#36454F")
            #loop ensures funcions dont run in an endless frenzy
            while True:
                button1.place_grid()
                button2.place_grid()
                pingpong.place_grid()
                window.update()
                time.sleep(0.005)

        def back():
            """used to destroy buttons when returning to main window
            """

            exitbutton.destroy()
            window.destroy()
            outerloop()

        exitbutton = Button(window, text="Exit Game", font=("Times Bold", 25), command=back, fg="#FF0000")
        exitbutton.pack()
        run_game()
        window.mainloop()

    window.title("Welcome!")
    welcomemessage = Label(window, text="Welcome to Ping Pong", font=("Times Bold", 50))
    welcomemessage.pack()
    aboutsection1 = Label(window, text="Player 1 (Left) will use 'W' and 'S'", font=("Times Bold", 25), fg="#DCB2CD")
    aboutsection1.pack(side=LEFT)
    aboutsection2 = Label(window, text="Player 2 (Right) will use '↑' and '↓'", font=("Times Bold", 25), fg="#DCB2CD")
    aboutsection2.pack(side=RIGHT)
    aboutsection3 = Label(window, text="Enjoy!", font=("Times Bold", 25), fg="#FF0000")
    aboutsection3.pack()
    startbutton = Button(window, text="Start Game", font=("Times Bold", 30), command=innerloop, fg="#00A300")
    startbutton.pack(side=BOTTOM )
 
outerloop()
window.mainloop()

# END OF CODE 
