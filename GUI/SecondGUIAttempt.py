__author__ = 'arif_'
from tkinter import *

root = Tk()  # Create a blank window

topFrame = Frame(root)  # Make a frame inside the root (main window)
topFrame.pack(side=TOP)  # To put it in and display in the topFrama
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)  # The bottom frame

button1 = Button(topFrame, text='Button 1', fg='red')  # fg is foreground color
button2 = Button(topFrame, text='Button 2', fg='blue')
button3 = Button(topFrame, text='Button 3', fg='green')
button4 = Button(bottomFrame, text='Button 4', fg='purple')
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()  # To make the window stay
