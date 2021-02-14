from tkinter import *

root = Tk()
root.geometry('100x100')

label1 = Label(root, text='label1', bg = 'white', fg = 'black')
label2 = Label(root, text='label2', bg = 'white', fg = 'black')

label1.pack()
label2.pack()

button1 = Button(root, text='click 1 here', bg = 'white', fg = 'black')
button2 = Button(root, text='click 2 here', bg = 'white', fg = 'black')

button1.pack()
button2.pack()

root.mainloop()

'''
Penggunaan warna biasanya di lakukan untuk mempercantik tampilan GUI.
Selain mengetikan nama color, kita juga bisa mengetikan code color

Berikut adalah beberapa warna yang bisa di gunakan beserta nama dan code color :
(untuk lebih lengkap nya silahkan cari di google Color Pallete)

background yang di singkat menjadi bg
================================================
bg          Name Color              Code Color
================================================
bg =        'black'         =       '#000000'
bg =        'white'         =       '#FFFFFF'
bg =        'green'         =       '#73D216'
bg =        'yellow'        =       '#EDD400'
bg =        'red'           =       '#EF2929'
bg =        'silver'        =       '#C0C0C0'
bg =        'pink'          =       '#FFC0CB'
bg =        'cadet blue'    =       '#5F9EA0'
bg =        'powder blue'   =       '#B0E0E6'
================================================


foreground yang di singkat menjadi fg
================================================
fg          Name Color              Code Color
================================================
fg =        'black'         =       '#000000'
fg =        'white'         =       '#FFFFFF'
fg =        'green'         =       '#73D216'
fg =        'yellow'        =       '#EDD400'
fg =        'red'           =       '#EF2929'
fg =        'silver'        =       '#C0C0C0'
fg =        'pink'          =       '#FFC0CB'
fg =        'cadet blue'    =       '#5F9EA0'
fg =        'powder blue'   =       '#B0E0E6'
================================================


'''