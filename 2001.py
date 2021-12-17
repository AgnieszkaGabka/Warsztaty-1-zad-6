import random
import math

def rzuty1(): # tura gracza - dwa rzuty, każdy po wciśnięciu enter, wynik dodawany do listy punkty_gracza i zwracany jako suma_punktów
    punkty_gracza = []
    for _ in range(2):
        text = input("Naciśnij enter, aby rzucić kostką")
        if text == "":
            x = random.randint(1,7)
            punkty_gracza.append(x)
            suma_punktow = sum(punkty_gracza)
        else:
            print("you typed some text before pressing enter")
    print(f"Masz obecnie {suma_punktow} punktów")
    return(suma_punktow)

def rzuty2(): # tura komputera - dwa rzuty, automatyczne losowanie numerów, dodawanych do listy punkty_komp
    punkty_komp = []
    for _ in range(2):
        x = random.randint(1,7)
        punkty_komp.append(x)
        suma_punktow = sum(punkty_komp)
    print(f"Punkty komputera: {suma_punktow}")
    return(suma_punktow)


def gra(): #funkcja wywołująca wymagane podczas gry polecenia
    lista_gracz = []  #lista kolejnych losowań gracza
    lista_komp = [] #lista kolejnych losowań komputera
    b = rzuty1() #wywołanie pierwszej tury gracza
    lista_gracz.append(b) #dodanie sumy wyników pierwszej tury gracza do listy
    c = rzuty2() #wywołanie pierwszej tury komputera
    lista_komp.append(c) #dodanie sumy wyników pierwszej tury komputera do listy
    x = sum(lista_gracz) #sumowanie wyników gracza
    y = sum(lista_komp) #sumowanie wynik≤óœ komputera
    while x < 2001 or y < 2001:
        d = rzuty1() #wywołanie drugiej i kolejnych tur gracza
        if d == 7:
            a = math.floor(x / 7)
            x = a #jeśli wylosowana zostanie siódemka, podziel sumę punktów gracza przez 7 i zamień punkty w liście na wynik dzielenia
            lista_gracz.clear()
            lista_gracz.append(x)
        elif d == 11:
            a = x * 11
            x = a #jeśli wylosowana zostanie 11, pomnóż sumę punktów razy 11 i zamień punkty w liście na wynik mnożenia
            lista_gracz.clear()
            lista_gracz.append(x)
        else:
            lista_gracz.append(d) #jeśli nie będzie 7 albo 11, dodaj wynik tury do listy z punktami
            x = sum(lista_gracz)
        print(f"Masz obecnie {x} punktów")
        e = rzuty2() #wywołanie drugiej i kolejnych tur komputera
        if e == 7:
            a = math.floor(y / 7)
            y = a #jeśli wylosowana zostanie siódemka, podziel sumę punktów gracza przez 7 i zamień punkty w liście na wynik dzielenia
            lista_komp.clear()
            lista_komp.append(y)
        elif e == 11:
            a = y * 11
            y = a #jeśli wylosowana zostanie 11, pomnóż sumę punktów razy 11 i zamień punkty w liście na wynik mnożenia
            lista_komp.clear()
            lista_komp.append(y)
        else:
            lista_komp.append(e) #jeśli nie będzie 7 albo 11, dodaj wynik tury do listy z punktami
            y = sum(lista_komp)
        print(f"Komputer ma obecnie {y} punktów")
        if x == 2001:
            return "Wygrałeś! Masz 2001 punktów!" #koniec gry gdy gracz wylosuje w sumie 2001 punktów
        elif y == 2001:
            return "Komputer wygrał, ma 2001 punktów!" #koniec gry gdy komputer wylosuje w sumie 2001 punktów
        elif x > 2001:
            return "Gra przerwana, masz ponad 2001 punktów" #koniec gry, gdy gracz przekroczy sumę 2001 punktów
        elif y > 2001:
            return "Gra przerwana, komputer ma ponad 2001 punktów" #koniec gry, gdy komputer przekroczy sumę 2001 punktów
        else:
            pass


print(gra())