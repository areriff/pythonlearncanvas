__author__ = 'arif_'
from tkinter import *

root = Tk()  # Create a blank window


##########Frame
# topFrame = Frame(root)  # Make a frame inside the root (main window)
# topFrame.pack(side=TOP)  # To put it in and display in the topFrama
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)  # The bottom frame
#
# button1 = Button(topFrame, text='Button 1', fg='red')  # fg is foreground color
# button2 = Button(topFrame, text='Button 2', fg='blue')
# button3 = Button(topFrame, text='Button 3', fg='green')
# button4 = Button(bottomFrame, text='Button 4', fg='purple')
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)
##############Put label
# one = Label(root, text='One', bg='grey', fg='yellow')
# one.pack()
# two = Label(root, text='Two', bg='green', fg='black')
# two.pack(fill=X)
# three = Label(root, text='three', bg='blue', fg='white')
# three.pack(side=LEFT, fill=Y)
##############Grid

# label_1 = Label(root, text='name')
# label_2 = Label(root, text='password')
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# label_1.grid(row=1, column=1, sticky=E) # sticky use North South East and West terminology
# label_2.grid(row=2, column=1, sticky=E)
# entry_1.grid(row=1, column=2)
# entry_2.grid(row=2, column=2)
#
# c = Checkbutton(root, text='Keep me logged in')
# c.grid(columnspan=2)

##############Bind function to widget

# def printName():
def printName(event):
    print('Hello, my name is Arif')


# button_1 = Button(root, text='Print Name', command=printName)
button_1 = Button(root, text='Print Name')
button_1.bind('<Button-1>', printName)  # <Button-1> is left mouse button
button_1.pack()


##############
root.mainloop()  # To make the window stay
