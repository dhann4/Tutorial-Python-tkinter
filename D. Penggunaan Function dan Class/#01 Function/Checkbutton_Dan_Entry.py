from tkinter import *

# Function command untuk Checkbutton dan Entry
def check1():
    if var1.get() == 1:
        entry_button1.configure(state = NORMAL)
        entry_button1.focus()
        entry_button1.delete(0, END)
        pilihan1.set('')
    elif var1.get() == 0:
        entry_button1.configure(state = DISABLED)
        pilihan1.set('0')

def check2():
    if var2.get() == 1:
        entry_button2.configure(state = NORMAL)
        entry_button2.focus()
        entry_button2.delete(0, END)
        pilihan2.set('')
    elif var2.get() == 0:
        entry_button2.configure(state = DISABLED)
        pilihan2.set('0')


root = Tk()
root.geometry('500x100')

# Variable Integer
var1 = IntVar()
var2 = IntVar()

# Variable String
pilihan1 = StringVar()
pilihan2 = StringVar()

# Set Variable
pilihan1.set('0')
pilihan2.set('0')

# Checkbutton
check_button1 = Checkbutton(root, variable = var1, onvalue = 1, offvalue = 0,
                            fg = 'black', text = 'Check Button 1', command = check1)
check_button2 = Checkbutton(root, variable = var2, onvalue = 1, offvalue = 0,
                            fg = 'black', text = 'Check Button 2', command = check2)
# Entry
entry_button1 = Entry(root, textvariable = pilihan1, state = DISABLED,
                      fg = 'black', relief = RIDGE, bd = 5)
entry_button2 = Entry(root, textvariable = pilihan2, state = DISABLED,
                      fg = 'black', relief = RIDGE, bd = 5)

# Checkbutton place
check_button1.place(x = 0, y = 10)
check_button2.place(x = 0, y = 40)

# Entry place
entry_button1.place(x = 150, y = 10)
entry_button2.place(x = 150, y = 40)


root.mainloop()