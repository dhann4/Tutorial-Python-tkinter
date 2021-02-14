'''
6. Radio Button widget adalah widget tkinter
yang berfungsi untuk memilih input dari radio button yang tersedia
dengan cara men-check / click radio button yang dipilih tersebut..
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

#D. radiobutton widget
v = IntVar()
v.set(1)

radiobutton1 = Radiobutton(root, text="Pilihan 1", variable=v, value=1)
radiobutton2 = Radiobutton(root, text="Pilihan 2", variable=v, value=2)

radiobutton1.pack()
radiobutton2.pack()

#3. Menampilkan GUI
root.mainloop()