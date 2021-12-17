import random
import math

def rolls1(): # tura gracza - dwa rzuty, każdy po wciśnięciu enter, wynik dodawany do listy punkty_gracza i zwracany jako suma_punktów
    gamers_points = []
    for _ in range(2):
        text = input("Press enter to roll the dice")
        if text == "":
            x = random.randint(1,7)
            gamers_points.append(x)
            points_sum = sum(gamers_points)
        else:
            print("You typed some text before pressing enter")
    print(f"You have now {points_sum} points")
    return(points_sum)

def rolls2(): # tura komputera - dwa rzuty, automatyczne losowanie numerów, dodawanych do listy punkty_komp
    comp_points = []
    for _ in range(2):
        x = random.randint(1,7)
        comp_points.append(x)
        points_sum = sum(comp_points)
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
        print(f"You have now {x} points")
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
            return "Game aborted, you have over 2001 points" #koniec gry, gdy gracz przekroczy sumę 2001 punktów
        elif y > 2001:
            return "Game aborted, the computer has over 2001 points" #koniec gry, gdy komputer przekroczy sumę 2001 punktów
        else:
            pass


print(game())