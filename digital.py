

# importing whole module
from tkinter import * 
from tkinter.ttk import *
  
# importing strftime function to
# retrieve system's time
from time import strftime
  
# creating tkinter window
root = Tk()
root.title('Lavkush Vishwakarma')
  
# This function is used to 
# display time on the label
def time():
    lavkush = strftime('%H:%M:%S %p')
    lbl.config(text = lavkush)
    lbl.after(200, time)
  
# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 140, 'bold'),
            background = 'black',
            foreground = 'pink')
  
# Placing clock at the centre
# of the tkinter window
lbl.pack()
time()
  
root.mainloop()
