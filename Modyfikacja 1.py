import random
import math

walls = [3, 4, 6, 8, 10, 12, 20, 100]
def choice():
    choice = input("Choose two dice from the set: D3, D4, D6, D8, D10, D12, D20, D100. \
    Enter your choice in the form: aDbD, where a is a number of walls of the first dice, and b is the number of walls of the second dice")
    rolls = list(choice)
    return(rolls) #funkcja zwraca ciąg znaków wpisanych przez gracza w formie listy

def spaces(): #funckja usuwa spacje z listy, jeśli użytkownik je wpisał
    data = choice()
    data = [x.strip(' ') for x in data]
    delete = [ele for ele in data if ele.strip()]
    return (delete)

def merge(): #funckja łączy liczby, jeśli wpisane zostały w formie znaków, np. z pozycji na liście "1", "0", "0" tworzy pozycję "100"
    data = spaces()
    index = 1
    while index < len(data):
        if data[index].isdigit() and data[index - 1].isdigit():
            data[index - 1] += data.pop(index)
        else:
            index += 1
    return (data)

def convert(): #funckja zamienia liczby wpisane przez użytkownika na formę int i zwraca wszystkie znaki w formie listy, np. [2, "D", 3, "D"]
    newdata = merge()
    for i in range(0, len(newdata)):
        try:
            newdata[i] = int(newdata[i])
        except (ValueError, TypeError):
            pass
    return (newdata)

def rolls1(): #rzuty gracza - pobieranie danych funkcji convert
    gamers_points = []
    dane = convert()
    text = input("Press enter to roll the dice")
    if text == "": #po wciśnięciu przez gracza enter funkcja zwraca lsowo wybran liczby z zakresu wprowadzonego przez gracza
        for index, i in enumerate(dane):
            if index == 0:
                if i in walls:
                    x = random.randint(1, i)
                    gamers_points.append(x) # dodwanie losowej liczby do listy z łącznnymi punktami
                else:
                    print("Enter correct data") #jeśli gracz coś wpisze, zamiast wcisnąć enter, program zwraca informację o niepoprawnych danych
                    break
            if index == 2:
                if i in walls:
                    x = random.randint(1, i)
                    gamers_points.append(x) # dodwanie losowej liczby do listy z łącznnymi punktami - drugi rzut kostką w turze
                else:
                    print("Enter correct data") #jeśli gracz coś wpisze, zamiast wcisnąć enter, program zwraca informację o niepoprawnych danych
                    break
            if index == 1:
                if i == "D": #sprawdzanie, czy gracz wpisał odpowiedni ciąg znaków
                    pass
                else:
                    print("Enter correct data") #jeśli gracz coś wpisze, zamiast wcisnąć enter, program zwraca informację o niepoprawnych danych
                    break
            if index == 3:
                if i == "D": #sprawdzanie, czy gracz wpisał odpowiedni ciąg znaków
                    pass
                else:
                    print("Enter correct data") #jeśli gracz coś wpisze, zamiast wcisnąć enter, program zwraca informację o niepoprawnych danych
                    break
    else:
        print("You typed some text before pressing enter")
    points_sum = sum(gamers_points) #sumowanie punktów gracza nal iście
    print(f"You now have {points_sum} points")
    return (points_sum)

def rolls2(): #pierwsza tura komputera - dwa rzuty, automatyczne losowanie numerów, dodawanych do listy punkty_komp
    comps_points = []
    for _ in range(2):
        a = random.choice(walls)
        x = random.randint(1, a)
        comps_points.append(x)
    points_sum = sum(comps_points)
    print(f"Computer's points: {points_sum}")
    return(points_sum)

def game(): #funkcja wywołująca wymagane podczas gry polecenia
    gamers_list = []  #lista kolejnych losowań gracza
    comp_list = [] #lista kolejnych losowań komputera
    b = rolls1() #wywołanie pierwszej tury gracza
    gamers_list.append(b) #dodanie sumy wyników pierwszej tury gracza do listy
    c = rolls2() #wywołanie pierwszej tury komputera
    comp_list.append(c) #dodanie sumy wyników pierwszej tury komputera do listy
    x = sum(gamers_list) #sumowanie wyników gracza
    y = sum(comp_list) #sumowanie wynik≤óœ komputera
    while x < 2001 or y < 2001:
        d = rolls1() #wywołanie drugiej i kolejnych tur gracza
        if d == 7:
            a = math.floor(x / 7)
            x = a #jeśli wylosowana zostanie siódemka, podziel sumę punktów gracza przez 7 i zamień punkty w liście na wynik dzielenia
            gamers_list.clear()
            gamers_list.append(x)
        elif d == 11:
            a = x * 11
            x = a #jeśli wylosowana zostanie 11, pomnóż sumę punktów razy 11 i zamień punkty w liście na wynik mnożenia
            gamers_list.clear()
            gamers_list.append(x)
        else:
            gamers_list.append(d) #jeśli nie będzie 7 albo 11, dodaj wynik tury do listy z punktami
            x = sum(gamers_list)
        print(f"You have {x} points")
        e = rolls2() #wywołanie drugiej i kolejnych tur komputera
        if e == 7:
            a = math.floor(y / 7)
            y = a #jeśli wylosowana zostanie siódemka, podziel sumę punktów gracza przez 7 i zamień punkty w liście na wynik dzielenia
            comp_list.clear()
            comp_list.append(y)
        elif e == 11:
            a = y * 11
            y = a #jeśli wylosowana zostanie 11, pomnóż sumę punktów razy 11 i zamień punkty w liście na wynik mnożenia
            comp_list.clear()
            comp_list.append(y)
        else:
            comp_list.append(e) #jeśli nie będzie 7 albo 11, dodaj wynik tury do listy z punktami
            y = sum(comp_list)
        print(f"Computer now has {y} points")
        if x == 2001:
            return "You won! You have 2001 points!" #koniec gry gdy gracz wylosuje w sumie 2001 punktów
        elif y == 2001:
            return "The computer won, it has 2001 points!" #koniec gry gdy komputer wylosuje w sumie 2001 punktów
        elif x > 2001:
            return "ame aborted, you have over 2001 points" #koniec gry, gdy gracz przekroczy sumę 2001 punktów
        elif y > 2001:
            return "Game aborted, the computer has over 2001 points" #koniec gry, gdy komputer przekroczy sumę 2001 punktów
        else:
            pass


print(game())