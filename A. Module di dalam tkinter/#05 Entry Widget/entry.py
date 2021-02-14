'''
5. Entry adalah sebuah kolom teks
yang berfungsi untuk memasukan input berupa teks, angka atau tanda baca lainya.
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

#C. entry widget
entry = Entry(root)
entry.pack()

#3. Menampilkan GUI
root.mainloop()