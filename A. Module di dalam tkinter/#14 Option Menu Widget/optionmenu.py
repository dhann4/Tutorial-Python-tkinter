'''
14. Option Menu adalah widget tkinter yang berfungsi
untuk membuat menu yang didalam menu tersebut
terdapat beberapa pilihan yang dapat dipilih oleh user.
'''

from tkinter import *

#1. Membuat GUI
root = Tk()

#2. Costumize GUI

#L. option menu widget
control_variable = StringVar(root)
OPTION_TUPLE = ("Option 1", "Option 2", "Option 3")
optionmenu = OptionMenu(root, control_variable, *OPTION_TUPLE)
optionmenu.pack()

#3. Menampilkan GUI
root.mainloop()