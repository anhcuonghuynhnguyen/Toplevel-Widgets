'''
askokcancel(title=None, message=None, **options)# Ask if operation should proceed; 
# return true if the answer is ok.

askquestion(title=None, message=None, **options)# Ask a question.

askretrycancel(title=None, message=None, **options)# Ask if operation should be retried;
# return true if the answer is yes.

askyesno(title=None, message=None, **options)# Ask a question; return true
# if the answer is yes.

askyesnocancel(title=None, message=None, **options)# Ask a question; return true
# if the answer is yes, None if cancelled.

showerror(title=None, message=None, **options)# Show an error message.

showinfo(title=None, message=None, **options)# Show an info message.

showwarning(title=None, message=None, **options)# Show a warning message.
'''

# In order to use this class one must import this class as shown below:
from tkinter.messagebox import *

# Showing various messaes

print(askokcancel( "askocancel", "Ok or cancel"))

print(askquestion( 'askquestion', 'Quétion'))

print(askretrycancel("askretrycancel", "Retry or Cancel"))
  
print(askyesno("askyesno", "Yes or No"))
  
print(askyesnocancel("askyesnocancel", "Yes or No or Cancel"))
  
print(showerror("showerror", "Error"))
  
print(showinfo("showinfo", "Information"))
  
print(showwarning("showwarning", "Warning"))
  
# print statement is used so that we can
# print the returned value by the function