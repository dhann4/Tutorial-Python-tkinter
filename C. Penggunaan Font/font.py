from tkinter import *

root = Tk()
root.geometry('200x200')

label1 = Label(root, text='label1', bg = 'white', fg = 'black',
               font=('URW Gothic L',20,'bold'))
label2 = Label(root, text='label2', bg = 'white', fg = 'black',
               font=('URW Gothic L',20,'bold'))

label1.pack()
label2.pack()

button1 = Button(root, text='click 1 here', bg = 'white', fg = 'black',
                 font=('URW Gothic L' ,20 ,'bold'))
button2 = Button(root, text='click 2 here', bg = 'white', fg = 'black',
                 font=('URW Gothic L' ,20 ,'bold'))

button1.pack()
button2.pack()

root.mainloop()

'''
font bisa di ganti dengan font yang tersedia di masing - masing operasi sistem,
jika misal font nya tidak berubah walau sudah di ganti, artinya font belum terinstall di operasi sistem

setelah font ada ukuran font dan style

font=('URW Gothic L', 20, 'bold)
'''