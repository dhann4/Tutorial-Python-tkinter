'''
12. Listbox adalah widget tkinter
yang berfungsi sebagai media input user dengan cara
user harus memilih beberapa pilihan dari sebuah list yang terdapat pada sebuah box.
'''

from tkinter import *

#1. Membuat GUI
root = Tk()

#2. Costumize GUI

#J. listbox widget
listbox_entries = ["Entry 1", "Entry 2", "Entry 3", "Entry 4"]
listbox_widget = Listbox(root)

for entry in listbox_entries:
   listbox_widget.insert(END, entry)

listbox_widget.pack()

#3. Menampilkan GUI
root.mainloop()