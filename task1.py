"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
entry = []
label = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
libs = []


import tkinter as tk
from tkinter import *
Main = tk.Tk()
Main.geometry("400x700")
def madlibbing_it_up():
    for x in range(16):
        libs.append(entry[x].get())
        entry[x].pack_forget()
        label[x].pack_forget()
    button1.pack_forget()
    label1 = tk.Label(text = "Meet our hero "+ libs[0] +" , a spuer-intelligent " + libs[1]+".\n A run-in with the " + libs[2]+ " Military leads him to create his later-ego\n" + libs[3] + ", a " + libs[4] + " "+ libs[5] + " giant capable of great\n destruction. He "+ libs[6]+ " battles the military with his girlfriend\n" + libs[7]+ ". Eventually it is discovered that our hero's long-time\n colleague " + libs[8] + ". distingguished by his " + libs[9] + "is trying\n to turn " + libs[3] + "into a weapon, leading to a climactic(if pointless)\n battle in downtown "+ libs[10]+ "with an evil version of the\n same giant alter-ego called "+libs[11]+". Eventually the enemy is\n subdued by "+libs[12]+"ing him with a " + libs[13]+". In the finla reel.\n"+libs[14]+ " appears to propose joining him in a " + libs[15],font=("Comic Sans MS", 14))
    label1.pack()

label[0]= tk.Label(text= "A strange name")
label[1]= tk.Label(text = "A profession")
label[2]= tk.Label(text = "A Country")
label[3]= tk.Label(text= "Another strange name")
label[4]= tk.Label(text = "A color")
label[5]= tk.Label(text = "An Adjective")
label[6]= tk.Label(text = "An Adverb")
label[7]= tk.Label(text = "Yet another strange name")
label[8]= tk.Label(text = "Yet another strange name")
label[9]= tk.Label(text = "Facial Feature")
label[10]= tk.Label(text = "US City")
label[11]= tk.Label(text = "Last strange name")
label[12]= tk.Label(text = "A verb")
label[13]= tk.Label(text = "A noun")
label[14]= tk.Label(text = "Actor who sold out")
label[15]= tk.Label(text = "Noun")
for y in range(16):
    entry.append(tk.Entry())
button1= tk.Button(text = "Let's madlib", command= madlibbing_it_up)


for i in range(16):
    label[i].pack()
    entry[i].pack()
button1.pack()

Main.mainloop()