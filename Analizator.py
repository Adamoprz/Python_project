import tkinter, collections
from tkinter import *
import tkinter.filedialog
from tkinter import ttk

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
                values=("21/07/2020", "AdamO", "Analiza tekstu/ liczb"))
    tree.pack()
    aboutw.bind('<Escape>', lambda event, closewin=aboutw: closew(event, closewin))
    aboutw.deiconify()
    aboutw.mainloop()


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def Czysc():
    text1.delete("1.0", tkinter.END)
    text2.delete("1.0", tkinter.END)

def liczby_pierwsze():
    text = text1.get("1.0", tkinter.END)
    text2.delete("1.0", tkinter.END)
    if RepresentsInt(text):
        #print(text)
        if int(text) >= 1:
            ile_liczb_pierwszych = int(text)
            niepodzielna = True
            lista = []
            a = 1
            licznik = 0
            ilosc = ile_liczb_pierwszych

            while licznik < ilosc:
                b = True
                for x1 in range(2, a):
                    if a % x1 == 0:
                        b = False
                if a == 1:
                    b = False
                if b == True:
                    lista.append(str(a))
                    licznik = licznik + 1
                a = a + 1
                #print(lista)
                ts = ','.join(lista)
        text2.delete("1.0", tkinter.END)
        text2.insert(tkinter.END, "liczby pierwsze to: \n" + str(ts))
    else:
        ts = "Ile liczb pierwszych chcesz wygenerować?. \nWpisz poprawną liczbę całkowitą dodatnią"
        text2.delete("1.0", tkinter.END)
        text2.insert(tkinter.END, str(ts))

def liczba_znakow():
    text = text1.get("1.0", tkinter.END)
    # splitlines usuwa znak nowej linii (\n)
    #text = text.split('\n')
    #text = text.splitlines()
    text = text.replace('\n', '').replace('\r', '')
    text_ = len(text)
    text2.delete("1.0", tkinter.END)
    text2.insert(tkinter.END,"Liczba wprowadzonych znakow: " + str(text_))

def liczba_slow():
    text = text1.get("1.0", tkinter.END)
    # splitlines usuwa znak nowej linii (\n)
    text = text
    liczba_sl = collections.Counter(text)
    print(liczba_sl)
    text2.delete("1.0", tkinter.END)
    text2.insert(tkinter.END,"Liczba wprowadzonych znakow: " + str(liczba_sl))

def Duze_male():
    text = text1.get("1.0", tkinter.END)
    text_ = text.lower()
    text2.delete("1.0", tkinter.END)
    text2.insert(tkinter.END,text_)

def male_Duze():
    text = text1.get("1.0", tkinter.END)
    text_ = text.upper()
    text2.delete("1.0", tkinter.END)
    text2.insert(tkinter.END,text_)


def liczba_pierwsza():
    text = text1.get("1.0", tkinter.END)
    text2.delete("1.0", tkinter.END)
    niepodzielna = True
    if RepresentsInt(text):
        liczba = int(text)
        for i in range(2, liczba):
            if liczba % i == 0:
                niepodzielna = False
        if niepodzielna == True and liczba > 1:
            text2.insert(tkinter.END, str(liczba) + " - Jest liczbą pierwsza")
        else:
            text2.insert(tkinter.END, str(liczba) + " - Nie jest liczbą pierwsza")
    else:
        text2.insert(tkinter.END," Wpisz poprawną liczbę całkowitą dodatnią")


main = tkinter.Tk()
Title = main.title("Analizator")
main.geometry("500x500")
main.configure(bg='white')

x1 = 10
y1 = 10
width1 = 20
height1 = 1

width2 = 30
height2 = 4

pos_button_cl_x = 130
pos_button_cl_y = 100

pos_button_x = 10
pos_button_y = 200
button_width = 25

text_pos_x = 15
text_pos_y = 15


text_width = 50
text_height = 4

text1 = tkinter.Text(main, width=text_width, height=text_height)
text1.pack(padx=5, pady=5)
text1.insert(tkinter.END, "Wpisz swój tekst lub liczbę którą chcesz sprawdzić")
text1.place(x = text_pos_x, y = text_pos_y)

text2 = tkinter.Text(main, width=text_width, height=text_height)
text2.pack()
text2.insert(tkinter.END, "")
text2.place(x = text_pos_x, y = text_pos_y+120)
#funkcja czysc

cl=tkinter.Button(main, text="Wyczyść", height=height1, width=width1, command = Czysc )
cl.pack
cl.place(x = pos_button_cl_x,y= pos_button_cl_y)


lp=tkinter.Button(main, text="Czy to liczba pierwsza?", height=height1, width=width1, command = liczba_pierwsza)
lp.pack()
lp.place(x = pos_button_x,y= pos_button_y + button_width )

dm=tkinter.Button(main, text="Duże na małe", height=height1, width=width1, command = Duze_male)
dm.pack()
dm.place(x = pos_button_x,y= pos_button_y + 2*button_width )

md=tkinter.Button(main, text="małe na Duże", height=height1, width=width1, command = male_Duze)
md.pack()
md.place(x = pos_button_x,y= pos_button_y + 3*button_width)


lz=tkinter.Button(main, text="Liczba znaków", height=height1, width=width1, command = liczba_znakow)
lz.pack()
lz.place(x = pos_button_x,y= pos_button_y + 4*button_width)

ls=tkinter.Button(main, text="Liczba określonych znaków", height=height1, width=width1, command = liczba_slow)
ls.pack()
ls.place(x = pos_button_x,y= pos_button_y + 5*button_width)

lps=tkinter.Button(main, text="Generuj liczby pierwsze", height=height1, width=width1, command = liczby_pierwsze)
lps.pack()
lps.place(x = pos_button_x,y= pos_button_y + 6*button_width)

# Button About
aboutb = tkinter.Button(main, background='white', font=("Helvetica", 8, 'bold'), text="Info", command=oprog)
aboutb.pack()
aboutb.place(x=435, y=0)

#input = text1.get("1.0", tkinter.END)

main.mainloop()