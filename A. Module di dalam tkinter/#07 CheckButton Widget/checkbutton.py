'''
7. CheckBox adalah widget tkinter
yang fungsinya hampir sama seperti Radio Button
hanya saja tidak ada pilihan seperti radio button.
'''

from tkinter import *

#1. Membuat GUI widget
root = Tk()

#2. Costumize GUI widget

#A. label
label = Label(root, text='ini adalah label')
label.pack()

#B. button widget
button = Button(root, text='button')
button.pack()

#C. entry
entry = Entry(root)
entry.pack()

#D. radiobutton widget
v = IntVar()
v.set(1)

radiobutton1 = Radiobutton(root, text="Pilihan 1", variable=v, value=1)
radiobutton2 = Radiobutton(root, text="Pilihan 2", variable=v, value=2)

radiobutton1.pack()
radiobutton2.pack()

#E. checkbutton widget
checkbutton = Checkbutton(root, text="Check Me")
checkbutton.pack()

#3. Menampilkan GUI
root.mainloop()