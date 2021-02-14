'''
2. title, hanya memunculkan title atau judul dari GUI di bagian atas widget.
geometry, berfungsi untuk mengatur tinggi dan lebar GUI serta sumbu x dan sumbu y nya.
'''

from tkinter import *

#1. Membuat GUI
root = Tk()

#2. Costumize GUI

#A. title widget
root.title('Menampilkan Title')

#B. geometry widget
# untuk mengatur panjang dan lebar GUI nya
# lalu untuk mengatur sudut x dan y pada GUI

# angka pertama untuk mengatur lebar, angka kedua untuk mengatur tinggi,
# angka ketiga untuk mengatur sumbu x, dan angka keempat untuk mengatur sumbu y
root.geometry('300x300+0+0')

#3. Menampilkan GUI
root.mainloop()

