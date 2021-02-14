'''
10. Label Frame adalah widget tkinter yang berfungsi
untuk mengorganisir atau mengelompokan beberapa section dalam sebuah aplikasi.
'''

from tkinter import *

#1. Membuat GUI
root = Tk()

#2. Costumize GUI

#H.label frame text widget
labelframe_widget = LabelFrame(root, text="Label Frame") # Judul
label_widget= Label(labelframe_widget, text="widget kecil dari Label Frame") # Teks di dalam Judul
labelframe_widget.pack(padx=10, pady=10)
label_widget.pack()

#3. Menampilkan GUI
root.mainloop()