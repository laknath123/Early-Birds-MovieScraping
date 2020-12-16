# Importing Tkinter
from tkinter import *
root = Tk()





e = Entry(root, width=50, font=('Helvetica', 24))
e.pack()
e.insert(0, "Enter a movie title: ")

def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	e.delete(0, 'end')
	myLabel.pack()

myButton = Button(root, text="OK", command=myClick)
myButton.pack()

e1 = Entry(root, width=50, font=('Helvetica', 24))
e1.pack()
e1.insert(0, "Get Movie Plot Summary : ")

def myClick1():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	e.delete(0, 'end')
	myLabel.pack()

myButton1 = Button(root, text="Ok", command=myClick)
myButton1.pack()



Button(root, text="Quit", command=root.destroy).pack()


root.mainloop()