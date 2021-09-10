# Python program to create
# yes/no message box


import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb


def call():
	res = mb.askquestion('Exit Application',
						'Do you really want to exit')
	print(res)
	if res == 'yes' :
		root.destroy()
		
	else :
		mb.showinfo('Return', 'Returning to main application')

# Driver's code
root = tk.Tk()
can = tk.Canvas(root,
				width = 200,
				height = 200)

can.pack()
but = Button(root,
		text ='Quit Application',
		command = call)

can.create_window( 100, 100, window= but)

root.mainloop()
