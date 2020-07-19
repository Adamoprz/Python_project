import tkinter.filedialog
from tkinter import *
from tkinter import ttk
import sys

def oprog():
    aboutw = Toplevel(bg="white")
    aboutw.title("Informacje o programie")
    aboutw.geometry("400x100")
    tree = tkinter.ttk.Treeview(aboutw, height=50, columns=('#0', '#1', '#2'))
    tree.column('#0', width=70)
    tree.column('#1', width=70)
    tree.column('#2', width=70)
    tree.column('#3', width=70)
    tree.heading('#0', text='Wersja')
    tree.heading('#1', text='Data Utw.')
    tree.heading('#2', text='Autor')
    tree.heading('#3', text='Opis')
    tree.insert("", 0, text="1.0",
                values=("19/07/2020", "AdamO", "Kalkulator"))
    tree.pack()
    aboutw.bind('<Escape>', lambda event, closewin=aboutw: closew(event, closewin))
    aboutw.deiconify()
    aboutw.mainloop()


def zakoncz():
    sys.exit()

def reset1():
    global znak_L1, li1, li2, znak1, znak2, Memo, i,znak1_1, li1_wp
    znak_L1, li1, i, li2, Memo, znak1, znak2, znak1_1, li1_wp= 0, 0, 0, 0, 0, 0, 0, 0, 0
    Memo = ''
    Result_.config(text="Podaj pierwszą liczbę")

def reset():
    reset1()
    Res.config(text = '0')

def put_1(a):
    global Memo, li1, li2, i, znak_L1, znak2, li1_wp
    li1_wp = 1
    if a == '-' and znak_L1 == '-':
        Memo = a
    if (znak_L1 != 0):
        Memo = znak_L1
    else:
        if znak1 == 0:
            li1 = str(li1) + str(a)
        if znak1 != 0:
            li2 = str(li2) + str(a)
        if a == '.':
            Memo = str(Memo) + str('.')
        else:
            if Memo != '':
                Memo = str(Memo) + str(a)
            if Memo == '':
                Memo = a
    Res.config(text=Memo)
    i = i + 1


def put_3(d):
    global znak2, znak1_1, Memo
    a= 1
    if znak1_1 == '-':
        a = -1
    if znak2 == 'multi':
        Res.config(text = Memo + ' = ' + str(round(a*float(li1) * float(li2),10)))
    if znak2 == 'div':
        Res.config(text= Memo + ' = ' + str(round(a*float(li1) / float(li2),10)))
    if znak2 == 'plus':
        Res.config(text= Memo + ' = ' + str(round(a*float(li1) + float(li2),10)))
    if znak2 == '-':
        Res.config(text= Memo + ' = ' + str(round(a*float(li1) - float(li2),10)))
    reset1()
    Result_.config(text="Wynik: ")

def put_2(b):
    Result_.config(text="Podaj drugą liczbę. '=' poda wynik")
    global Memo, znak1, znak2, znak_L1, li1_wp
    if znak2 == 0:
        znak2 = b
        if znak1 != '1' and b != '-':
            znak1 = 1
            li1_wp = 1
            if b == 'multi':
                Memo = str(Memo) + str(' * ')
            if b == '-':
                Memo = str(Memo) + str(' - ')
            if b == 'plus':
                Memo = str(Memo) + str(' + ')
            if b == 'div':
                Memo = str(Memo) + str(' / ')
        else:
            if b == '-' and znak1 != '1':
                Memo = str(Memo) + str(' - ')
                znak_L1 = '-'
        Res.config(text=Memo)

def put_4():
    global Memo, znak2, znak1_1, znak1
    if li1_wp == 0:
        Memo = '-'
        znak1_1 = '-'
    else:
        if znak2 == 0:
            Memo = str(Memo) + ' - '
            znak2 = '-'
            znak1 = 1
    Res.config(text=Memo)

# Definicja głównego okna
main = tkinter.Tk()
main.wm_title("Kalulator")
main.geometry("240x260")
#main.geometry("500x500")
main.configure(bg='white')

li1, li2, li1_wp, znak1, znak2, i, znak_L1, znak1_1  = 0,0,0,0,0,0,0,0
Memo = ''
plotstr = ""
start = 0



frameinfo = tkinter.LabelFrame(main, text="Kalkulator", width=50, height=60, font=("Helvetica", 16),
                       background="white")
frameinfo.pack(fill="both")
Result_ = tkinter.Label(frameinfo, text="Podaj pierwszą liczbę: ", fg='#%02x%02x%02x' % (10, 10, 10), font=("Helvetica", 8, "bold"),
                    background="white")
Result_.pack()

Result_.place(x=2, y=2)

w1 = 1
w2 = 1
x1 = 40
y1 = 90
width_hor = 25
width_vert = 35


L1 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="1",
                    command=lambda:put_1(1), width=w1, height=w2)
L2 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="2",
                    command=lambda:put_1(2), width=w1, height=w2)
L3 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="3",
                    command=lambda:put_1(3), width=w1, height=w2)
L4 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="4",
                    command=lambda:put_1(4), width=w1, height=w2)
L5 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="5",
                    command=lambda:put_1(5), width=w1, height=w2)
L6 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="6",
                    command=lambda:put_1(6), width=w1, height=w2)
L7 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="7",
                    command=lambda:put_1(7), width=w1, height=w2)
L8 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="8",
                    command=lambda:put_1(8), width=w1, height=w2)
L9 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="9",
                    command=lambda:put_1(9), width=w1, height=w2)
L0 = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="0",
                    command=lambda:put_1(0), width=w1, height=w2)
L_multi = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="*",
                         command=lambda:put_2('multi'), width=w1, height=w2)
L_min = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="-",
                       command=lambda:put_4(), width=w1, height=w2)
L_plus = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="+",
                        command=lambda:put_2("plus"), width=w1, height=w2)
L_equal = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text="=",
                         command=lambda:put_3("equal"), width=w1, height=w2)
L_dot = tkinter.Button(main, background='white', font=("Helvetica", 12, 'bold'), text=".",
                       command=lambda:put_1("."), width=w1, height=w2)
L_div= tkinter.Button(main, background='white', font=("Helvetica", 12,'bold'), text="/",
                      command=lambda:put_2("div"), width=w1, height=w2)

Res = tkinter.Label(main, text="0", font=("Helvetica", 12,'bold'), justify='right')
Res.pack()
Res.place(x = 10, y= 60)

#t = tkinter.Text(main, height=5, width=40)
#t1 = tkinter.Text(main, height=5, width=40)
e = tkinter.Button(main, text = "Zakoncz",background='white', font=("Helvetica", 12, 'bold'), command = zakoncz, width=8*w1, height=w2)
cz = tkinter.Button(main, text = " Wyczyść ",background='white', font=("Helvetica", 12, 'bold'), command = lambda:reset(), width=8*w1, height=w2)
#t.pack()
# Boton About
aboutb = tkinter.Button(frameinfo, background='white', font=("Helvetica", 8, 'bold'), text="Info", command=oprog)
aboutb.pack()
aboutb.place(x=200, y=0)


#t1.pack()
e.pack()
cz.pack()
cz.place(x=x1 + 4*width_hor, y=y1+2*width_vert)
e.place(x=x1 + 4*width_hor, y=y1+3*width_vert)
L1.pack(side=tkinter.RIGHT)
L1.place(x=x1, y=y1)
L2.pack()
L2.place(x=x1+width_hor, y=y1)
L3.pack()
L3.place(x=x1 +2*width_hor, y=y1)
L4.pack()
L4.place(x=x1, y=y1+width_vert)
L5.pack()
L5.place(x=x1+width_hor, y=y1+width_vert)
L6.pack()
L6.place(x=x1 + 2*width_hor, y=y1+width_vert)
L7.pack()
L7.place(x=x1, y=y1+2*width_vert)
L8.pack()
L8.place(x=x1+width_hor, y=y1+2*width_vert)
L9.pack()
L9.place(x=x1+2*width_hor, y=y1+2*width_vert)
L0.pack()
L0.place(x=x1+width_hor, y=y1+3*width_vert)

L_div.pack()
L_multi.pack()
L_min.pack()
L_plus.pack()
L_equal.pack()
L_dot.pack()

L_div.place(x=x1 + 3*width_hor, y=y1+3*width_vert)
L_multi.place(x=x1 + 3*width_hor, y=y1)
L_min.place(x=x1 + 3*width_hor, y=y1+width_vert)
L_plus.place(x=x1 + 3*width_hor, y=y1+2*width_vert)
L_equal.place(x=x1 + 2*width_hor, y=y1+3*width_vert)
L_dot.place(x=x1, y=y1+3*width_vert)

main.mainloop()