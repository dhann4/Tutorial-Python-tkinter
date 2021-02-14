'''
16. Border berguna untuk menjadikan tampilan dalam widget menjadi lebih hidup
'''

from tkinter import *

root = Tk()
root.geometry('200x200')

label1 = Label(root, text='label1', bg = 'powder blue', fg = 'black',
               font=('URW Gothic L',14,'bold'), relief = RIDGE, bd = 10)
label2 = Label(root, text='label2', bg = 'cadet blue', fg = 'black',
               font=('URW Gothic L',14,'bold'), relief = GROOVE, bd = 10)

label1.pack()
label2.pack()

button1 = Button(root, text='click 1 here', bg = 'powder blue', fg = 'black',
                 font=('URW Gothic L' ,14 ,'bold'), relief = RAISED, bd = 10)
button2 = Button(root, text='click 2 here', bg = 'cadet blue', fg = 'black',
                 font=('URW Gothic L' ,14 ,'bold'), relief = SOLID, bd = 10)

button1.pack()
button2.pack()

root.mainloop()

'''
masih ada 2 lagi selain RIDGE, GROOVE, RAISED, dan SOLID yaitu:
FLAT dan SUNKEN
'''