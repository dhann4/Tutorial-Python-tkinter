'''
8. Scale adalah widget tkinter
yang berfungsi sebagai input berupa ‘saklar / tombol’
yang dapat digeser dan nilai nya akan berubah-ubah setiap kali digeser.
Terdapat 2 jenis scale yaitu scale horizintal dan vertical
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

#E. checkbutton widget
checkbutton = Checkbutton(root, text="Check Me")
checkbutton.pack()

#F. scale widget
#a. scale horizontal
scale = Scale(root, from_=0, to=100, orien=HORIZONTAL)
scale.set(0)
scale.pack()

#b. scale vertical
scale = Scale(root, from_=0, to=100, orien=VERTICAL)
scale.set(0)
scale.pack()

#3. Menampilkan GUI
root.mainloop()