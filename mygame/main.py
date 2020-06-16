import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
import time as t
import tkinter.font as tkFont


root = tk.Tk()

length_1 = root.winfo_screenheight()
width_1 = root.winfo_screenwidth()


m = Canvas(root, width=width_1, height=length_1)
m.pack()

# rectangle
r1 = m.create_rectangle(0, 0, width_1, (length_1/4), fill='#40b0b5', width=0)
r2 = m.create_rectangle(0, (length_1/4), width_1,
                        length_1, fill='#a8e1d3', width=0)


# oval
x = -100
for i in range(15):
    x += 100
    c = m.create_oval(15+x, length_1/4-50, 115+x,
                      length_1/4+50, fill='#e3b6af', width=0)


# ball
ph2 = Image.open("sport.png")
ph2 = ph2.resize((70, 70), Image.ANTIALIAS)
ig2 = ImageTk.PhotoImage(ph2)
c1 = m.create_image(width_1/2-3, length_1/4, image=ig2)

# player name
fontStyle1 = tkFont.Font(family="Lucida Grande", size=40)
player1 = tk.Label(root, text="PLAYER 1", font=fontStyle1, bg='#a8e1d3')
m.create_window(width_1/5, length_1/2-80, window=player1)
player2 = tk.Label(root, text="PLAYER 2", font=fontStyle1, bg='#a8e1d3')
m.create_window(width_1-300, length_1/2-80, window=player2)

# point ellipsee
poi1 = Image.open("Ellipse 11.png")
poi1 = poi1.resize((100, 100), Image.ANTIALIAS)
poin1 = ImageTk.PhotoImage(poi1)
m.create_image(width_1/5, length_1/2+20, image=poin1)
poi2 = Image.open("Ellipse 11.png")
poi2 = poi2.resize((100, 100), Image.ANTIALIAS)
poin2 = ImageTk.PhotoImage(poi2)
m.create_image(width_1-300, length_1/2+20, image=poin2)


# point Label
fontStyle3 = tkFont.Font(family="Lucida Grande", size=40)
pnum1 = tk.Label(root, text="0", font=fontStyle3, bg='#a8e1d3')
m.create_window(width_1/5, length_1/2+20, window=pnum1)
pnum2 = tk.Label(root, text="0", font=fontStyle3, bg='#a8e1d3')
m.create_window(width_1-300, length_1/2+20, window=pnum2)

cup1 = Image.open("goal.png")
cup1 = cup1.resize((220, 220), Image.ANTIALIAS)
cup11 = ImageTk.PhotoImage(cup1)


p1 = 0
p2 = 0
y = 0


def Toleft():
    global p1
    global p2
    y = -100
    m.move(c1, y, 0)
    p1 += 1
    pnum1.config(text=p1)
    p2 -= 1
    pnum2.config(text=p2)
    if(p1 == 7):
        m.create_image(width_1/5, length_1/2+200, image=cup11)
        for i in range(len(bu)):
            bu[i].config(state="disabled")
    print(p1)


def toright():
    global p2
    global p1
    y = +100
    m.move(c1, y, 0)
    p2 += 1
    pnum2.config(text=p2)
    p1 -= 1
    pnum1.config(text=p1)
    if(p2 == 7):
        m.create_image(width_1-300, length_1/2+200, image=cup11)
        for i in range(len(bu)):
            bu[i].config(state="disabled")
    print(p2)


images = ['burger.png', 'child.png', 'flower.png', 'food.png', 'money.png', 'sun.png', 'umbrella.png', 'burger.png',
          'child.png', 'flower.png', 'food.png', 'money.png', 'sun.png', 'umbrella.png', 'heart.png', 'heart.png']


# arrimages
arr = []


def rand():

    random.shuffle(images)
    c = -1
    x = -100
    for i in range(4):
        x += 100
        y = 250
        for j in range(4):
            c += 1
            y -= 100
            photo = Image.open(images[c])
            print(c)
            print(images[c])
            photo = photo.resize((50, 50), Image.ANTIALIAS)
            arr.append(ImageTk.PhotoImage(photo))


rand()
bu = []
num = []

photo1 = Image.open("question.png")
photo1 = photo1.resize((20, 20), Image.ANTIALIAS)
f = ImageTk.PhotoImage(photo1)
e = 0
p = 0


def changimage(k):
    print(k)
    global p
    bu[k].config(image=arr[k], state="disabled")
    num.append(k)
    if(len(num) == 2):

        p += 1
        if(images[num[0]] == images[num[1]]):
            global e
            e += 1
            print(p % 2)
            if(p % 2 == 0):
                toright()
                num.clear()
            else:
                Toleft()
                num.clear()
                print("yes")
            if(e == 8):
                e = 0
                arr.clear()
                rand()
                for i in range(len(bu)):
                    bu[i].config(image=f, state="normal")

        else:
            bu[num[0]].config(image=f, state="normal")
            bu[num[1]].config(image=f, state="normal")
            num.clear()
            print("No")


c = -1
x = -100
for i in range(4):
    x += 100
    y = 250
    for j in range(4):
        c += 1
        y -= 100
        bu.append(tk.Button(root, text="?", width=int(width_1/18),
                            height=int(length_1/18), image=f, command=lambda k=c: changimage(k)))
        m.create_window(width_1/2+(y), length_1/2.3+(x),  window=bu[c])

root.mainloop()
