'''While working with files one may need to open files, 
do operations on files and after that to save file. asksaveasfile() is 
the function which is used to save user’s file (extension can be set explicitly or you can set default extensions also). 
This function comes under the class filedialog.'''

# from tkinter.filedialog import asksavesfile (now you san use fuction)
# files = [("any name of file 1 ", "*.type1 "), ("any name of file 2 ", "*.type2 "), etc...]
# file = asksaveasfile( filetypes = files, defaultextension = files)

# importing all files from tkinter
from tkinter import *
from tkinter import ttk

# import only asksaveasfile from filedialog
# which is used to save file in any extension
from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry('600x600')

# function to call when user press
# the save button, a filedialog will
# open and ask to save file
def save():
	a = text.get("1.0", END)
	files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt')]
	file = asksaveasfile(filetypes = files, defaultextension = files)
	file.write(a)

btn = ttk.Button(root, text = 'Save', command = lambda : save())
btn.pack( side= BOTTOM)

text = Text(root, height = 500,
				width = 500,
				bg = "light yellow")
text.pack(side= TOP, fill= 'none')


mainloop()
