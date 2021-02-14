from tkinter import *

# Membuat Function command untuk Button
def click1():
    print("click 1")

def click2():
    print("click 2")

root = Tk()
root.title('Contoh Function untuk Button')
root.geometry('400x400')

# agar berfungsi maka di dalam Button() tambahkan argumen
# command lalu nama function nya yaitu click
# command= click
button1 = Button(root, text='click 1 here', command= click1, bg = 'yellow', fg = 'black',
                 font=('URW Gothic L' ,20 ,'bold'), relief = RIDGE, bd = 5)
button2 = Button(root, text='click 2 here', command= click2, bg = 'yellow', fg = 'black',
                 font=('URW Gothic L' ,20 ,'bold'), relief = RIDGE, bd = 5)

button1.pack()
button2.pack()

root.mainloop()