'''
By default, the size of the message box is Fix. We can’t change the size of that Message Box. 
Different Boxes have different sizes. However, we can use Different alternative methods for this purpose  

    1.Message Widget
    2.By Changing ReadMe File
'''

'''1. Message Widget 
MessageBox library doesn’t provide the functions to change the configuration of the box. 
We can use the other function. 
The message can also be used to display the information. 
The size of the message is the size of the window so that we can set the size of the message by geometry, pack.  
'''

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
main = Tk()

str_var = StringVar()
#Message function
mes = Message(main, textvariable= str_var, relief= RAISED)
#the size of the text determines
#the size of the messagebox
str_var.set("You can't change your profile picture")
mes.pack()

'''
This is another alternative option of the Message Box. 
In this, We are Opening the file readme.txt the length of the content of the readme file determines 
the size of the messagebox.
'''
def lesson():
    with open("Học phần cntt.txt") as f:
        readme = f.read()
        #display whole message
        messagebox.showinfo("Học phần", str(readme))
#create button
but = Button(main, text= "Học phần", command= lesson)
but.pack()

mainloop()




