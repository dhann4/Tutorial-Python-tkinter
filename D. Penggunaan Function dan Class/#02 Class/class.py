from tkinter import *

def main():
    root = Tk()
    app = window1(root)

class window1:
    def __init__(self, master):
        self.master = master
        self.master.title('Penggunaan Class')
        self.master.geometry('300x300')

        frame = LabelFrame(self.master, text = 'Label Frame', fg = 'black', bg = 'white',
                           relief = RIDGE, bd = 10)
        frame.pack(ipadx = 130, ipady = 130)

        label = Label(frame, text='ini label frame', bg='yellow', fg='black',
                      font=('URW Gothic L',16,'bold'),relief = RIDGE, bd = 5)
        label.place(x = 0, y = 0, relwidth = 1)

        frame_btn = Frame(frame, bg = 'blue',relief = RIDGE, bd = 5)
        frame_btn.place(x = 0, y = 50, relwidth = 1, height = 170)

        label = Label(frame_btn, text='ini frame', bg='blue', fg='black',
                      font=('URW Gothic L', 16, 'bold'))
        label.place(x=0, y=0)

        button = Button(frame_btn, text = 'Button', bg = 'green', fg = 'black',
                        font=('URW Gothic L',16,'bold'), relief = RIDGE, bd = 10)
        button.place(x = 50, y = 50, height = 50, width = 110)

main()
mainloop()