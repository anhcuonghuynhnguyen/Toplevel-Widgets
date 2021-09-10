'''While working with GUI one may need to open files and read data from it or may require to write data in that particular file. 
One can achieve this with the help of open() function (python built-in) but one may not be able to select any required file unless provides a path to that particular file in code.
With the help of GUI, you may not require to specify the path of any file but you can directly open a file and read it’s content.

In order to use askopenfile() function you may require to follow these steps:'''
# import tkinter
# from tkinter.filedialog import askopenfile ## Now you can use this function
# file = askopenfile( mode= 'r', filetypes = [("any name you want to display", "extension of file type")])


# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import * 
from tkinter.ttk import *
# importing askopeenfile function
# from class filedialog
from tkinter.filedialog import askopenfile 

main = Tk()
main.geometry("600x600")

#This function will be used to open
# file in read mode and only Python files will be opened
def open_file():
    file = askopenfile( mode= 'r', filetypes= [("Text", "*")]) 
    content = file.read()
    #insert 
    inputtxt.delete('1.0', END)
    inputtxt.insert(END, content)

#creating a scroll
scr = Scrollbar(main, orient= 'vertical')
scr.pack(side = RIGHT, fill= Y)    

#creating a button
but  = Button(main, text= "Open", command= lambda: open_file())
but.pack()

#create Text
inputtxt = Text(main, height = 500,
				width = 500,
				bg = "light yellow")
inputtxt.pack(side= BOTTOM, fill= 'none')

# attaching scroll and text
inputtxt.config( yscrollcommand= scr.set)
scr.config( command= inputtxt.yview)

mainloop()