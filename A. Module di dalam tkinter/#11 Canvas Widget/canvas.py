'''
11. Canvas adalah widget tkinter yang berfungsi sebagai media output.
'''

from tkinter import *

#1. Membuat GUI
root = Tk()

#2. Costumize GUI

#I. canvas widget
canvas_widget = Canvas(root, bg="blue", width=100, height= 50)
canvas_widget.pack()

#3. Menampilkan GUI
root.mainloop()