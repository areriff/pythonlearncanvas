__author__ = 'arif_'
from tkinter import *

##########Frame
# root = Tk()  # Create a blank window

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

#
##############Put label
# root = Tk()  # Create a blank window

# one = Label(root, text='One', bg='grey', fg='yellow')
# one.pack()
# two = Label(root, text='Two', bg='green', fg='black')
# two.pack(fill=X)
# three = Label(root, text='three', bg='blue', fg='white')
# three.pack(side=LEFT, fill=Y)

# root.mainloop()  # To make the window stay
##############Grid
# root = Tk()  # Create a blank window

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

# root.mainloop()  # To make the window stay
##############Bind function to widget
# root = Tk()  # Create a blank window

# # def printName():
# def printName(event): # event is something user do / can do
#     print('Hello, my name is Arif')
#
#
# # button_1 = Button(root, text='Print Name', command=printName)
# button_1 = Button(root, text='Print Name')
# button_1.bind('<Button-1>', printName)  # <Button-1> is left mouse button
# button_1.pack()
#
# root.mainloop()  # To make the window stay
##############one widget does multiple thing
# root = Tk()  # Create a blank window

# def leftClick(event):
#     print('Left')
#
# def middleClick(event):
#     print('Middle')
#
# def rightClick(event):
#     print('Right')
#
# frame = Frame(root, width=300, height=250)
# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-2>", middleClick)
# frame.bind("<Button-3>", rightClick)
# frame.pack()

# root.mainloop()  # To make the window stay
##############how to use class
# class BuckyButtons:
#     def __init__(self, master): # __init__ initialize itself whenever I create object/something
#         frame = Frame(master)
#         frame.pack()
#
#         self.printButton = Button(frame, text='Print Message', command=self.printMessage)
#         self.printButton.pack(side=LEFT)
#
#         self.quitButton = Button(frame, text='Quit', command=frame.quit)
#         self.quitButton.pack(side=LEFT)
#     def printMessage(self):
#         print('Wow, this actually worked!')
#
# root = Tk()  # Create a blank window
# b = BuckyButtons(root)
# root.mainloop()  # To make the window stay

##############Creating drop down menu

# def doNothing():
#     print('ok ok I won\'t')
#
#
# root = Tk()  # Create a blank window
#
# menu = Menu(root)
# root.config(menu=menu)
#
# subMenu = Menu(menu)  # This is adding the item
# menu.add_cascade(label='File', menu=subMenu)  # This is how I want it to behave
# subMenu.add_command(label='New Project...', command=doNothing)
# subMenu.add_command(label='New...', command=doNothing)
# subMenu.add_separator()
# subMenu.add_command(label='Exit', command=quit)
#
# editMenu = Menu(menu)
# menu.add_cascade(label='Edit', menu=editMenu)
# editMenu.add_command(label='Redo', command=doNothing)
#
# # ENd of menu, Starts of toolbar
#
# toolbar = Frame(root, bg='blue')  # create basic toolbar
# insertButton = Button(toolbar, text='Insert Image', command=doNothing)  # put the button in toolbar
# insertButton.pack(side=LEFT, padx=2, pady=2)
# printButton = Button(toolbar, text='print', command=doNothing())
# printButton.pack(side=LEFT, padx=2, pady=2)
#
# toolbar.pack(side=TOP, fill=X)
#
# # ENd of toolbar, starts of status bar
#
# status = Label(root, text='Preparing to do nothing...', bd=1, relief=SUNKEN, anchor=W, bg='white')
# status.pack(side=BOTTOM, fill=X)
#
# root.mainloop()  # To make the window stay

##############Message Box

# import tkinter.messagebox
#
# root = Tk()
#
# tkinter.messagebox.showinfo('Window Title', 'Mondkey can live up to three hundred years')
# answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')
#
# if answer == 'yes':
#     print(' ;-) ')
# elif answer == 'no':
#     quit()
# else:
#     quit()
#
# root.mainloop()

##############Shapes and Graphics

# root = Tk()
#
# canvas = Canvas(root, width=600, height=300)
# canvas.pack()
#
# blackLine = canvas.create_line(10,10,300,200, fill='black')
# redLine = canvas.create_line(10,290,300,200, fill='red')
# blueLine = canvas.create_line(590,10,300,200, fill='blue')
# greenBox = canvas.create_rectangle(60,30,400,180, fill='green')
#
# canvas.delete(greenBox, redLine, blueLine)
# canvas.delete(ALL)
#
# root.mainloop()

############ Images and Icons

root = Tk()

photo = PhotoImage( file="add1.png" )
label = Label( root, image=photo )
label.pack( )

root.mainloop()
