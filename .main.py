from Tkinter import *

# main window create with root widget
root = Tk()
# Whatever you want to do in tkinter you have to 
# 1. define it and 2. put it on screen


def myCLick1():
    lb1 = Label(root, text = 'I clicked a button '+ e.get())
    # lb1.grid(row=50, column=50)
    # lb1.pack()

def buttn_add():
    return

button1 = Button(root, text = '1', command = buttn_add, padx=40,pady=40)
button1.grid(row = 500,column=200) # place button
# mybutton.pack()
# event loop is like refresh 

#Create input fields
e = Entry (root,width = 50, bg="black",fg ="white")
e.grid(row=0, column=0,columnspan=5,padx = 10,pady = 10)
e.insert(0, "Enter your name")
# e.get() to catch input 






root.mainloop()