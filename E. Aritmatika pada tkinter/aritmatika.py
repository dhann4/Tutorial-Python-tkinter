from tkinter import *

def penjumlahan():
    a = int(entry1.get())
    b = int(entry2.get())

    sum = a + b
    sum_entry.delete(0, END) # untuk menghapus angka yang sudah di jumlah, jika tidak memakai ini angka akan menumpuk
    sum_entry.insert(0, sum) # untuk menampilkan hasil penjumlahan ke sum_entry lalu saat melakukan penjumlahan lagi, angka sebelum nya akan di reset ulang


root = Tk()
root.title('Aritmatika')

entry1 = Entry(root,bg = 'white', fg = 'black')
entry1.pack(side=LEFT)

label = Label(root, text='+')
label.pack(side=LEFT)

entry2 = Entry(root,bg = 'white', fg = 'black')
entry2.pack(side=LEFT)

btn_equals = Button(root, text= '=', command = penjumlahan)
btn_equals.pack(side=LEFT)

sum_entry = Entry(root,bg = 'white', fg = 'black')
sum_entry.pack(side=LEFT)

root.mainloop()