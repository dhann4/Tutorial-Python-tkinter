'''
9. Text adalah widget tkinter yang berfungsi untuk menampilkan teks.
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
entry = Entry(root, bg = 'white', fg = 'black')
entry.pack()

#D. radiobutton widget
v = IntVar()
v.set(1)

radiobutton1 = Radiobutton(root, text="Pilihan 1", variable=v, value=1,fg = 'black')
radiobutton2 = Radiobutton(root, text="Pilihan 2", variable=v, value=2,fg = 'black')

radiobutton1.pack()
radiobutton2.pack()

#E. checkbutton widget
checkbutton = Checkbutton(root, text="Check Me",fg = 'black')
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

#G. text widget
text_widget = Text(root, width=20, height=3, bg = 'white', fg = 'black')
text_widget.insert(END, "ini adalah text")
text_widget.pack()

#3. Menampilkan GUI
root.mainloop()