'''
using the message box library we can show serval Information, Error, 
Warning, Cancelation ETC in the form of Message-Box.
 It has a Different message box for a different purpose. 
 '''

"""
showinfo() – To display some important information .
showwarning() – To display some type of Warning.
showerror() –To display some Error Message.
askquestion() – To display a dialog box that asks with two options YES or NO.
askokcancel() – To display a dialog box that asks with two options OK or CANCEL.
askretrycancel() – To display a dialog box that asks with two options RETRY or CANCEL.
askyesnocancel() – To display a dialog box that asks with three options YES or NO or CANCEL.
"""

#  messagebox.name_of_function(Title, Message, [, options])
'''
name_of_function – Function name that which we want to use .
Title – Message Box’s Title.
Message – Message that you want to show in the dialog.
Options –To configure the options.
'''

from tkinter import *
from tkinter import messagebox

main =Tk()

#fuction to use the asquestion() function
def Submit():
    messagebox.askquestion("Form",
                                            "Do you want to Submit ?",
                                            icon = 'error')

main.geometry("100x100")
 
b1 = Button(main, text= "Submit", command= Submit)
b1.pack()

mainloop()