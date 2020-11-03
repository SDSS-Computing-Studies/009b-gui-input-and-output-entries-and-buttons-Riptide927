"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""


import tkinter as tk
from tkinter import *
import math
Main = tk.Tk()

textvar = StringVar()
textvar.set("Answer will be here")

def toggle1():
    if button1["text"]== "+":
        button1["text"]= "-"
    else:
         button1["text"]="+"

def toggle2():
    if button2["text"]== "+":
        button2["text"]= "-"
    else:
         button2["text"]="+"


def quad():
    b = float(entryb.get())
    c = float(entryc.get())

    if button1["text"]== "-":
        b = b*-1
    if button2["text"]== "-":
        c = c*-1
 
    x1 = (-1*b + math.sqrt(b**2 - 4 * 1*c)) / (2*1)
    x2 = (-1*b - math.sqrt(b**2 - 4 * 1*c)) / (2*1)
    z=[x1,x2]
    entryAns.delete(0,END)
    entryAns.insert(0,z)


frameQ=tk.Frame()
frameA=tk.Frame()

intro = tk.Label(text = "Enter the b and c values for your trinomial. a is already set to one")

textlabel1 = Label(master = frameQ, text = "x^2")
button1 = Button(master = frameQ, command = toggle1, text = "+",)
entryb = Entry(master = frameQ, width = 5) 
textlabel2 =  Label(master = frameQ, text = "x")
button2 = Button(master = frameQ, command = toggle2, text = "+")
entryc = Entry(master = frameQ, width = 5)


entryAns = Entry(master = frameA,textvariable = textvar)
calc = tk.Button(text = "Press this to calculate", command = quad)
intro.pack()
frameQ.pack()
frameA.pack()
textlabel1.pack(side = LEFT)
button1.pack(side = LEFT)
entryb.pack(side = LEFT)
textlabel2.pack(side = LEFT)
button2.pack(side = LEFT)
entryc.pack(side = LEFT)
entryAns.pack(side = LEFT)


calc.pack()



Main.mainloop()