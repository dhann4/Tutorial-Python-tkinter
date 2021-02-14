from tkinter import *

# Function command untuk Radiobutton
def check_list1():
    print("pilihan 1")

def check_list2():
    print("pilihan 2")

root = Tk()
root.geometry('200x200')

# Variable
pilihan1 = IntVar()
pilihan2 = IntVar()

pilihan1.set(1)
pilihan2.set(1)

# Radiobutton
radiobutton1 = Radiobutton(root, text="Pilihan 1", variable=pilihan1,
                           value=1, command=check_list1)
radiobutton2 = Radiobutton(root, text="Pilihan 2", variable=pilihan2,
                           value=2, command=check_list2)

radiobutton1.pack()
radiobutton2.pack()

root.mainloop()