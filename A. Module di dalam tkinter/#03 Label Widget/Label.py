'''
3. Label adalah sebuah widget Tkinter
yang berfungsi untuk menampilkan teks untuk mendeskripsikan suatu section atau entry.
'''

from tkinter import *

#1. Membuat GUI

root = Tk()

#2. Costumize GUI

#A. label widget
# menampilkan teks di dalam GUI
label1 = Label(root, text='ini adalah label 1')
label2 = Label(root, text='ini adalah label 2')

label1.pack()
label2.pack()

#a. Untuk pack()
# label.pack(side=BOTTOM) untuk menempatkan label nya di bagian bawah
# label.pack(side=TOP) untuk menempatkan label nya di bagian atas
# label.pack(side=LEFT) untuk menempatkan label nya di bagian kiri
# label.pack(side=RIGHT)  untuk menempatkan label nya di bagian kanan

#b. Untuk grid()
# label1.grid(row=0, column=1)
# label2.grid(row=1, column=2)

#c. untuk place()
# label1.place(x=130, y=50, height=50, width=250)
# label2.place(x=130, y=120, height=50, width=250)

#3. Menampillkan GUI
root.mainloop()