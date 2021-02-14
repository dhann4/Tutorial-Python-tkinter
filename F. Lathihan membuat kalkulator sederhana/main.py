'''
sekarang kita akan membuat apliaksi kalkulator sederhana dengan menggunakan
pengetahuan dari tutorial sebelum nya, sebelum itu kita membuat aplikasi nya dengan model yang
biasa tanpa menggunakan class hanya menggunakan function.
'''

from tkinter import *

def button_click(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def equals():
    global operator
    sumup = str(eval(operator))
    txt_input.set(sumup)
    operator = ''

def clear():
    global operator
    operator = ''
    txt_input.set('0')

root = Tk()
root.title('Kalkulator')
root.geometry('430x415')

txt_input = StringVar()
operator = ''

# LabelFrame dan Frame
frame = LabelFrame(root, relief = RIDGE, bg = 'powder blue',fg = 'black', text='KALKULATOR',bd = 7,
                   font=('URW Gothic L', 16, 'bold'))
frame.pack(ipady = 208, ipadx = 215)

frame_btn = Frame(frame, relief = RIDGE, bg = 'cadet blue', bd = 5)
frame_btn.place(x = 0, y = 60, height = 320, width = 415)

# Entry
entry = Entry(frame, bg = 'white', fg = 'black', relief =RIDGE, bd = 5,
              font=('DS-Digital',30,'bold'), justify = RIGHT, state = 'readonly', textvariable = txt_input)
entry.place(x = 0, y = 0, width = 415)
entry.insert(0,'0')


# Button 1-equal(=)
btn_1 = Button(frame_btn, text = '1', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('1'))
btn_1.place(x=10, y=10)

btn_4 = Button(frame_btn, text = '4', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('4'))
btn_4.place(x=10, y=85)

btn_7 = Button(frame_btn, text = '7', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('7'))
btn_7.place(x=10, y=160)

btn_equal = Button(frame_btn, text = '=', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = equals)
btn_equal.place(x=10, y=235)


# Button 2-0
btn_2 = Button(frame_btn, text = '2', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('2'))
btn_2.place(x=110, y=10)

btn_5 = Button(frame_btn, text = '5', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('5'))
btn_5.place(x=110, y=85)

btn_8 = Button(frame_btn, text = '8', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('8'))
btn_8.place(x=110, y=160)

btn_0 = Button(frame_btn, text = '0', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('0'))
btn_0.place(x=110, y=235)


# Button 3-C
btn_3 = Button(frame_btn, text = '3', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('3'))
btn_3.place(x=210, y=10)

btn_6 = Button(frame_btn, text = '6', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('6'))
btn_6.place(x=210, y=85)

btn_9 = Button(frame_btn, text = '9', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('9'))
btn_9.place(x=210, y=160)

btn_C = Button(frame_btn, text = 'C', pady = 10, padx = 28, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = clear)
btn_C.place(x=210, y=235)


# Button tambah - bagi
btn_Tmbh = Button(frame_btn, text = '+', pady = 10, padx = 29, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('+'))
btn_Tmbh.place(x=310, y=10)

btn_Krng = Button(frame_btn, text = '-', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('-'))
btn_Krng.place(x=310, y=85)

btn_Kli = Button(frame_btn, text = 'x', pady = 10, padx = 29, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('*'))
btn_Kli.place(x=310, y=160)

btn_Bgi = Button(frame_btn, text = '/', pady = 10, padx = 30, bg = 'cadet blue', fg = 'black',
               relief = RAISED, bd = 5, font = ('URW Gothic L',16,'bold'),
               command = lambda :button_click('/'))
btn_Bgi.place(x=310, y=235)


root.mainloop()

'''
oke, sekarang tutorial nya berakhir sampai disini tidak ada lagi yang bisa saya
jelaskan.

kalian bebas berkreasi dengan imajinasi masing - masing
membuat aplikasi apapun itu selama kalian tau dasar - dasar nya dan kalian paham
tentang penggunaan function dan class.

Bisa sih jika tanpa class, biasanya class di butuhkan agar tampilan nya lebih rapi lagi
dan untuk penggunaan sistem aplikasi login biasanya menggunakan class sebagai tampilan awal
atau yang kita tau adalah widget.
(adalah tampilan utama sebelum kita memutuskan mau masuk ke tampilan yang mana, seperti jika kita klik login
maka di arahkan ke tampilan ke 2 khusus bagi user yang sudah login,
jika kita klik register maka akan di arahkan ke tampilan ke 3 khusus untuk yang ingin register, dan sebagainya)

Lalu subclass nya adalah tampilan khusus untuk pengguna atau user yang sudah login
(adalah misal untuk login system saat kita klik login kita akan di arahkan ke tampilan khusus bagi yang sudah login
seperti contoh nya, facebook, instagram, twitter, dan lain sebagainya)

ada lagi, tampilan khusus saat di klik maka akan di arahkan ke tampilan lain nya sesuai apa yang user klik
(di dalam tampilan khusus pengguna yang login, kan ada tampilan menu untuk
pesan lalu pengaturan, profil, dan lain sebagainya.
Saat kita klik pesan, kita di arahkan ke tampilan khusus untuk mengirim atau menerima pesan dari user lain
saat kita klik pengaturan, kita di arahkan ke tampilan khusus pengaturan untuk mengatur profil kita
saat kita klik profil, kita di arahkan ke tampilan khusus untuk profil kita)

Tampilan khusus untuk register
(jika tampilan login system kan ada register, nah saat kalian klik register
pada umum nya kalian akan di arahkan ke tampilan register, kita asumsikan saja seperti kita
mendaftar akun Gmail, Instagram, dan lain sebagainya)

dan sampai akhir, tergantung berapa tampilan yang kalian buat.

sebenarnya masih banyak lagi module yang ada di dalam tkinter,
seperti ImageTk untuk menampilkan gambar sebagai background nya
atau juga bisa untuk menambahkan gambar seperti logo user dan logo kunci
yang biasanya di gunakan untuk login

silahkan cari di dokumentasi nya python lalu search aja tkinter
untuk link website python tulis aja

python.org

jangan carinya di Nekopoi gan bahaya, bagi yg gk tau Nekopoi itu apa
mending jangan tau yah, apalagi jika ada yang masih di bawah umur:v
'''