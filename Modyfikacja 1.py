import random
import math

scianki = [3, 4, 6, 8, 10, 12, 20, 100]
def wybor():
    wybor = input("Wybierz dwie kości z zestawu: D3, D4, D6, D8, D10, D12, D20, D100. \
    Swój wybór wpisz w formie: aDbD, gdzie a to liczba ścianek pierwszej kości, a b to liczba ścianek drugiej kości ")
    rzuty = list(wybor)
    return(rzuty) #funkcja zwraca ciąg znaków wpisanych przez gracza w formie listy

def spacje(): #funckja usuwa spacje z listy, jeśli użytkownik je wpisał
    dane = wybor()
    dane = [x.strip(' ') for x in dane]
    delete = [ele for ele in dane if ele.strip()]
    return (delete)

def merge(): #funckja łączy liczby, jeśli wpisane zostały w formie znaków, np. z pozycji na liście "1", "0", "0" tworzy pozycję "100"
    dane = spacje()
    index = 1
    while index < len(dane):
        if dane[index].isdigit() and dane[index - 1].isdigit():
            dane[index - 1] += dane.pop(index)
        else:
            index += 1
    return (dane)

def convert(): #funckja zamienia liczby wpisane przez użytkownika na formę int i zwraca wszystkie znaki w formie listy, np. [2, "D", 3, "D"]
    newdane = merge()
    for i in range(0, len(newdane)):
        try:
            newdane[i] = int(newdane[i])
        except (ValueError, TypeError):
            pass
    return (newdane)

def rzuty1(): #rzuty gracza - pobieranie danych funkcji convert
    punkty_gracza = []
    dane = convert()
    text = input("Naciśnij enter, aby rzucić kostką")
    if text == "": #po wciśnięciu przez gracza enter funkcja zwraca lsowo wybran liczby z zakresu wprowadzonego przez gracza
        for index, i in enumerate(dane):
            if index == 0:
                if i in scianki:
                    x = random.randint(1, i)
                    punkty_gracza.append(x) # dodwanie losowej liczby do listy z łącznnymi punktami
                else:
                    print("Podaj poprawne dane") #jeśli gracz coś wpisze, zamiast wcisnąć enter, program zwraca informację o niepoprawnych danych
                    break
            if index == 2:
                if i in scianki:
                    x = random.randint(1, i)
                    punkty_gracza.append(x) # dodwanie losowej liczby do listy z łącznnymi punktami - drugi rzut kostką w turze
                else:
                    print("Podaj poprawne dane") #jeśli gracz coś wpisze, zamiast wcisnąć enter, program zwraca informację o niepoprawnych danych
                    break
            if index == 1:
                if i == "D": #sprawdzanie, czy gracz wpisał odpowiedni ciąg znaków
                    pass
                else:
                    print("Podaj poprawne dane") #jeśli gracz coś wpisze, zamiast wcisnąć enter, program zwraca informację o niepoprawnych danych
                    break
            if index == 3:
                if i == "D": #sprawdzanie, czy gracz wpisał odpowiedni ciąg znaków
                    pass
                else:
                    print("Podaj poprawne dane") #jeśli gracz coś wpisze, zamiast wcisnąć enter, program zwraca informację o niepoprawnych danych
                    break
    else:
        print("you typed some text before pressing enter")
    suma_punktow = sum(punkty_gracza) #sumowanie punktów gracza nal iście
    print(f"Masz obecnie {suma_punktow} punktów")
    return (suma_punktow)

def rzuty2(): #pierwsza tura komputera - dwa rzuty, automatyczne losowanie numerów, dodawanych do listy punkty_komp
    punkty_komp = []
    for _ in range(2):
        a = random.choice(scianki)
        x = random.randint(1, a)
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