# menu = Menu(master, **options)
'''
Popup menus are context menus that appear on user interaction. 
This menu can be shown anywhere on the client window. 
below is the python code to create a popup menu using Tkinter library.
'''
#creating popup menu in tkinter
import tkinter

class A:
	#creates parent window
	def __init__(self):
			
		self.root = tkinter.Tk()
		self.root.geometry('500x500')

		self.frame1 = tkinter.Label(self.root,
									width = 400,
									height = 400,
									bg = '#AAAAAA')
		self.frame1.pack()

	#create menu
	def popup(self):
		self.popup_menu = tkinter.Menu(self.root,
									tearoff = 0)
		
		self.popup_menu.add_command(label = "say hi",
									command = lambda:self.hey("hi"))
		
		self.popup_menu.add_command(label = "say hello",
									command = lambda:self.hey("hello"))
		self.popup_menu.add_separator()
		self.popup_menu.add_command(label= "say bye", command= lambda: self.hey("bye"))
        

	#display menu on right click
	def do_popup(self,event):
		try:
			self.popup_menu.tk_popup(event.x_root,
									event.y_root)
		finally:
			self.popup_menu.grab_release()

	def hey(self,s):
		self.frame1.configure(text = s)
		
	def run(self):
		self.popup()
		self.root.bind("<Button-3>",self.do_popup)
		tkinter.mainloop()

a = A()
a.run()

#function tk_popup(X,Y) use to post the menu at position X,Y with entry ENTRY.
'''Functions

Menu(root): creates the menu.
add_command(label, command): adds the commands on the menu, the command argument calls the function hey() when that option is clicked.
add_separator(): adds a separator.
tk_popup(x, y): posts the menu at the position given as arguments
grab_release(): releases the event grab
bind(key, event): binds the mouse event.'''