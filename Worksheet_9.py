
from tkinter import *
import math

print("Q1")
r=Tk()
r.title("Robot Control Panel")
r.geometry("500x400")
r.configure(bg="yellow")
r.mainloop()

print("Q2")
r=Tk()
c=Canvas(r,width=300,height=300)
c.pack()
c.create_oval(98,98,102,102,fill="black")
r.mainloop()

print("Q3")
r=Tk()
c=Canvas(r,width=300,height=300)
c.pack()
pts=[20,50,100,120,180,90,250,150]
c.create_line(pts,fill="blue",width=3)
r.mainloop()

print("Q4")
r=Tk()
c=Canvas(r,width=400,height=200)
c.pack()
x=10
p=c.create_oval(x,90,x+10,100,fill="black")
def move():
    global x
    x+=5
    c.move(p,5,0)
    if x<380:
        r.after(50,move)
move()
r.mainloop()

print("Q5")
r=Tk()
c=Canvas(r,width=400,height=300)
c.pack()
c.create_rectangle(150,150,250,220,fill="gray")
c.create_oval(140,220,180,260,fill="black")
c.create_oval(220,220,260,260,fill="black")
r.mainloop()

print("Q6")
r=Tk()
c=Canvas(r,width=400,height=300)
c.pack()
bot=c.create_oval(190,140,210,160,fill="red")
def mv(dx,dy):
    c.move(bot,dx,dy)
Button(r,text="Up",command=lambda:mv(0,-10)).pack()
Button(r,text="Down",command=lambda:mv(0,10)).pack()
Button(r,text="Left",command=lambda:mv(-10,0)).pack()
Button(r,text="Right",command=lambda:mv(10,0)).pack()
r.mainloop()

print("Q7")
r=Tk()
c=Canvas(r,width=400,height=300)
c.pack()
dx=3
dy=3
b=c.create_oval(185,135,215,165,fill="blue")
def bounce():
    global dx,dy
    c.move(b,dx,dy)
    x1,y1,x2,y2=c.coords(b)
    if x1<=0 or x2>=400:
        dx=-dx
    if y1<=0 or y2>=300:
        dy=-dy
    r.after(30,bounce)
bounce()
r.mainloop()

print("Q8")
r=Tk()
c=Canvas(r,width=500,height=300)
c.pack()
x=50
bot=c.create_oval(x-10,190,x+10,210,fill="green")
def line():
    global x
    if x<450:
        c.move(bot,5,0)
        x+=5
        r.after(50,line)
line()
r.mainloop()

print("Q9")
r=Tk()
c=Canvas(r,width=600,height=500)
c.pack()
A=(150,300)
D=(400,300)
theta=math.radians(30)
B=(A[0]+120*math.cos(theta),A[1]-120*math.sin(theta))
c.create_line(A,B,fill="red",width=3)
c.create_line(B,D,fill="green",width=3)
c.create_line(A,D,fill="black",width=3)
r.mainloop()

print("Q10")
r=Tk()
c=Canvas(r,width=400,height=300)
c.pack()
x=200
y=150
bot=c.create_oval(x-10,y-10,x+10,y+10,fill="orange")
def move(e):
    global x,y
    dx=dy=0
    if e.keysym=="Up": dy=-5
    if e.keysym=="Down": dy=5
    if e.keysym=="Left": dx=-5
    if e.keysym=="Right": dx=5
    c.create_line(x,y,x+dx,y+dy)
    c.move(bot,dx,dy)
    x+=dx
    y+=dy
def reset():
    c.delete("all")
    global bot,x,y
    x=200
    y=150
    bot=c.create_oval(x-10,y-10,x+10,y+10,fill="orange")
r.bind("<Key>",move)
Button(r,text="RESET",command=reset).pack()
r.mainloop()
