from tkinter import *
from tkinter.filedialog import asksaveasfile
 
new = Tk()
new.geometry('640x300')
new.title('IoT4Beginners')
 
 
def check():
    a = text.get("1.0", END)
    file = asksaveasfile(defaultextension=".txt")
    file.write(a)
    file.close()
 
 
text = Text(new, font=('TimesNewRoman',20))
button = Button(new,text='Save as',font=('Courier',10), width=30,bd=10, command =check)
 
 
 
text.pack(side= TOP)
button.pack(side=BOTTOM)
mainloop()