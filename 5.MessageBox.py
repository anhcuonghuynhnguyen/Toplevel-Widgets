#messagebox.Function_Name(title, message [, options]) 
''''
Function_Name: This parameter is used to represents an appropriate message box function.
title: This parameter is a string which is shown as a title of a message box.
message: This parameter is the string to be displayed as a message on the message box.
options: There are two options that can be used are:
    default: This option is used to specify the default button like ABORT, RETRY, or IGNORE in the message box.
    parent: This option is used to specify the window on top of which the message box is to be displayed.
'''
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")

w = Label(root, text ='GeeksForGeeks', font = "50")
w.pack()

messagebox.showinfo("showinfo", "Information")

messagebox.showwarning("showwarning", "Warning")

messagebox.showerror("showerror", "Error")

messagebox.askquestion("askquestion", "Are you sure?")

messagebox.askokcancel("askokcancel", "Want to continue?", )

messagebox.askyesno("askyesno", "Find the value?")


messagebox.askretrycancel("askretrycancel", "Try again?")

root.mainloop()
