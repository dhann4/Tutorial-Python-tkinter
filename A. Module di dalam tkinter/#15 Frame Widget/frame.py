'''
15. Frame Widget adalah yang fungsi nya sebagai wadah untuk meletakkan
Label, Button, Radiobutton, Checkbutton, dan lain sebagainya.

Frame sendiri juga bisa di buat sebanyak mungkin di dalam Widget,
tergantung pemakaian dari user
'''

from tkinter import *

#1. Membuat GUI
root = Tk()
root.geometry('300x300')

#2. Costumize GUI

#M. frame widget
frame1 = Frame(root,bg = 'green')
frame1.place(x=0, y=0, height = 150, width = 150)

label1 = Label(frame1, text='ini adalah label\ndi dalam frame 1', bg= 'green', fg = 'black')
label1.pack()

button1 = Button(frame1, text='button1', bg= 'yellow', fg = 'black')
button1.pack()
#=====================================================================================================

frame2 = Frame(root,bg = 'blue')
frame2.place(x=0, y=150, height = 150, width = 150)

label2 = Label(frame2, text='ini adalah label\ndi dalam frame 2', bg= 'blue', fg = 'black')
label2.pack()

button2 = Button(frame2, text='button2', bg= 'red', fg = 'black')
button2.pack()
#=====================================================================================================

frame3 = Frame(root,bg = 'red')
frame3.place(x=150, y=0, height = 150, width = 150)

label3 = Label(frame3, text='ini adalah label\ndi dalam frame 3', bg= 'red', fg = 'black')
label3.pack()

button3 = Button(frame3, text='button3', bg= 'blue', fg = 'black')
button3.pack()
#=====================================================================================================

frame4 = Frame(root,bg = 'yellow')
frame4.place(x=150, y=150, height = 150, width = 150)

label4 = Label(frame4, text='ini adalah label\ndi dalam frame 4', bg= 'yellow', fg = 'black')
label4.pack()

button4 = Button(frame4, text='button4', bg= 'green', fg = 'black')
button4.pack()
#=====================================================================================================

#3. Menampilkan GUI
root.mainloop()