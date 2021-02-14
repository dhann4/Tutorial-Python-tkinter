'''
4. Button adalah widget yang berfungsi untuk membuat tombol.
'''

from tkinter import *

#1. Membuat GUI
root = Tk()

#2. Costumize GUI

#A. label widget
label = Label(root, text='ini adalah label')
label.pack()

#B. button widget
button = Button(root, text='button')
button.pack()

#3. Menampilkan GUI
root.mainloop()