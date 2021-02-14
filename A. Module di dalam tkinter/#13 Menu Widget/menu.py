'''
13. Menu adalah widget tkinter yang berfungsi untuk membuat menu bar.
'''

from tkinter import *

#1. Membuat GUI
root = Tk()

#2. Costumize GUI

#K. menu widget
menu_widget = Menu(root)
submenu_widget1 = Menu(menu_widget, tearoff = False)
submenu_widget2 = Menu(menu_widget, tearoff = False)
submenu_widget3 = Menu(menu_widget, tearoff = False)

menu_widget.add_cascade(label="File", menu=submenu_widget1)
menu_widget.add_cascade(label="Edit", menu=submenu_widget2)
menu_widget.add_cascade(label="View", menu=submenu_widget3)

submenu_widget1.add_command(label="Open...")
submenu_widget1.add_command(label="Save As...")
submenu_widget1.add_separator()
submenu_widget1.add_command(label="Exit")

submenu_widget2.add_command(label="Cut")
submenu_widget2.add_command(label="Copy")
submenu_widget2.add_command(label="Paste")

submenu_widget3.add_command(label="Tool Windows")
submenu_widget3.add_command(label="Apperance")
submenu_widget3.add_separator()
submenu_widget3.add_command(label="Recent")

root.config(menu=menu_widget)


#3. Menampilkan GUI
root.mainloop()