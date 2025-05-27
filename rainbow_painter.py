#welcome to Rainbow Painter!
import turtle
from tkinter import *

#screen setup
root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = Canvas(master = root, width = screen_width, height = 700)
canvas.pack()
root_width = 1440
root_height = 800

#making the screen full screen
root_xcor = (screen_width/2)-(root_width/2)
root_ycor = (screen_height/2)-(root_height/2)

root.geometry('%dx%d+%d+%d'%(root_width, root_height, root_xcor, root_ycor))

#turtle setup 
t = turtle.RawTurtle(canvas)
t.color("purple")
t.speed(0)


#v below are the fractals ! v

#the basic beginner tree fractals that actually looks cool
#ref: https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6
def tree():
    t.shape("circle")  

    lv = 11
    l  = 100 
    s  = 17

    t.penup()
    t.back(l)                                             
    t.pendown()
    t.forward(l)

    def draw_tree(l, level):
        l = 3.0/4.0*l
        t.left(s)
        t.forward(l)
        level +=1
        if level<lv:
            draw_tree(l, level)

        t.back(l)
        t.right(2*s)
        t.forward(l)
        if level<=lv:
            draw_tree(l, level)
            t.stamp()

        t.back(l)
        t.left(s)
        level -=1

     
    draw_tree(l, 2)
    t.shape("classic")


#frozen let it go ft hatsune miku, pt 1
#ref: koch snowflake, https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6 (again)
def snowflake():
    def let_it_go(t, iterations, length, shortening_factor, angle):
        if iterations == 0:
            t.forward(length)
        else:
            iterations = iterations - 1
            length = length / shortening_factor
            let_it_go(t, iterations, length, shortening_factor, angle)
            t.left(angle)
            let_it_go(t, iterations, length, shortening_factor, angle)
            t.right(angle * 2)
            let_it_go(t, iterations, length, shortening_factor, angle)
            t.left(angle)
            let_it_go(t, iterations, length, shortening_factor, angle)
    for i in range(3):
      let_it_go(t, 3, 50, 3, 60)
      t.right(120)
    t.shape("classic")

#twinkle twinkle little star how i wonder have you any wool yes sir yes sir 3 bags full
#ref: https://pythonguides.com/fractal-python-turtle/#:~:text=Fractal%20python%20turtle%20is%20used,is%20not%20same%20in%20shape.
def stars():
    def star(turtle, size):
        if size <= 10:
            return
        else:
            for i in range(5):
            
                # moving turtle forward
                t.forward(size)
                star(turtle, size/3)
  
                # moving turtle left
                t.left(216)
    star(1, 45)
    t.shape("classic")

#illuninati? nah its just triangles
#ref: https://stackoverflow.com/questions/25772750/sierpinski-triangle-recursion-using-turtle-graphics
def triangle():            
    def illuninati(length,depth):
        if depth==0:
            for i in range(0,3):
                t.fd(length)
                t.left(120)
        else:
            illuninati(length/2,depth-1)
            t.fd(length/2)
            illuninati(length/2,depth-1)
            t.bk(length/2)
            t.left(60)
            t.fd(length/2)
            t.right(60)
            illuninati(length/2,depth-1)
            t.left(60)
            t.bk(length/2)
            t.right(60)

    illuninati(50,2)
    t.shape("classic")
#oOOOoooOOO funky circle made with squares
#ref: http://mathalope.co.uk/2015/04/22/udacity-programming-fundamentals-with-python-turtle-module-draw-a-circle-out-of-squares/
def square():
    def draw_square(n):
        for i in range(0,4):
            t.forward(n)        
            t.right(90)
        
    def squares():
        for i in range (0, 36):
            draw_square(100)
            t.right(10)
        for i in range (0, 18):
            draw_square(50)
            t.right(20)
    squares()
    t.shape("classic")
#frozen let it go ft flower, pt 2
#ref:https://projects.raspberrypi.org/en/projects/turtle-snowflakes/5
def vflower():
    for i in range(10):
        for i in range(2):
            t.forward(25)
            t.right(60)
            t.forward(25)
            t.right(120)
        t.right(36)
    for i in range(10):
        for i in range(2):
            t.forward(12.5)
            t.right(60)
            t.forward(12.5)
            t.right(120)
        t.right(36)
    t.shape("classic")
#everything gets detroyed (clear canvas)    
def clearall():
    t.clear()

#make turtle go to cursor
#ref:https://stackoverflow.com/questions/29211794/how-to-bind-a-click-event-to-a-canvas-in-tkinter
def callback(event):
    event.x = event.x - screen_width / 2
    event.y = -event.y + screen_height / 2
    t.penup()
    t.goto(event.x, event.y)
    t.pendown()

#set pen direction
def setheading():
   global entry_sh
   heading = entry_sh.get()
   heading  = float(heading)
   t.setheading(heading)

#set bg colour
def bg():
   global entry_bg
   bg = entry_bg.get()
   canvas.configure(bg=bg)

#set pen colour
def pc():
   global entry_pc
   pc = entry_pc.get()
   t.color(pc)

#buttons for the fractals!
#tree button
tree_b = Button(master = root, text = "Tree", command = tree, width = '9',\
                height = '3')
tree_b.pack(side = LEFT)

#snowflake button
snowflake = Button(master = root, text = "Snowflake", command = snowflake, \
              width = '9',height = '3')
snowflake.pack(side = LEFT)

#stars button
star = Button(master = root, text = "Stars", command = stars, \
              width = '9',height = '3')
star.pack(side = LEFT)

#triangles button
Triangle = Button(master = root, text = "Triangle", command = triangle, \
               width = '9',height = '3')
Triangle.pack(side = LEFT)

#trippy circle button
circle_illusion = Button(master = root, text = "Circle \n Illusion", command = square,\
               width = '9',height = '3')
circle_illusion.pack(side = LEFT)

#flower button
vflower = Button(master = root, text = "Flower", command = vflower,\
                 width = '9',height = '3')
vflower.pack(side = LEFT)

#clearall button
clearall = Button(master = root, text = "Clear All", command = clearall,\
                  width = '9',height = '3')
clearall.pack(side = LEFT)

#setheading GUI
confirm_sh = Button(root, text= "Confirm", command= setheading)
confirm_sh.pack(side = RIGHT)
entry_sh = Entry(root, bd =5,width=10)
entry_sh.pack(side = RIGHT)
label_sh = Label(root, text="Set Pen Direction")
label_sh.pack( side = RIGHT)

#setpencolour GUI
confirm_pc = Button(root, text= "Confirm", command= pc)
confirm_pc.pack(side = RIGHT)
entry_pc = Entry(root, bd =5,width=10)
entry_pc.pack(side = RIGHT)
label_pc = Label(root, text="Set Pen Colour")
label_pc.pack( side = RIGHT)

#bg GUI
confirm_bg = Button(root, text= "Confirm", command= bg)
confirm_bg.pack(side = RIGHT)
entry_bg = Entry(root, bd =5,width=10)
entry_bg.pack(side = RIGHT)
label_bg = Label(root, text="Set Background Color")
label_bg.pack( side = RIGHT)

#boring stuff
canvas.bind("<Button-1>", callback)
root.mainloop()


