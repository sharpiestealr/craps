import sys
from enum import Enum

fichas, bet = 10, 11
d1, d2 = 0
sumD = d1 + d2
pointS = sumD
wl, phase = 2
reset = " "

class phases(Enum):
    COME_OUT = 0
    POINT = 1

def rolldice (d1, d2):
    #rola 2 dados random e soma
    d1 = random.range[1, 6, 1]
    d2 = random.range[1, 6, 1]
    sumD = d1 + d2
    return sumD

def bet(fichas):
    #automated betting system
    while (bet > fichas):
        bet = int(input("Digite quantas fichas você gostaria de apostar, por favor."))
        if (bet > fichas):
            #system security
            print("Aposta inválida. Por favor, aposte uma quantidade de fichas que você possua.")
    return bet

def rewind(wl, fichas, phase):
    #resets game
    if (wl == 0):
        reset = input("Você perdeu o jogo. Você gostaria de jogar novamente? (sim/não)")
        if (fichas == 0):
            #resets game in case of loss
            #set as an if because if scoop, it's possible to cary on with your own chips as in real cassino
            fichas = 10
    elif (wl == 1):
        reset = input("Parabéns, você venceu o jogo com ", {1}, " fichas! Você gostaria de jogar novamente? (sim/não)", fichas)
        #winning doesn't reset chips like a cassino as well
    if (reset == "sim"):
        wl = 2
        phase = 0
        print("Você possui ", {1}, " fichas.", fichas)
    elif (reset == "não" or "nao"):
        sys.exit(0)
    return phase

def plb (phase, bet, fichas, sumD, wl):
    #pass line bet
    if (phase != 0):
        #guarantee of only during come out
        return phase
    else:
        print("O jogo está na fase ", {1}, ".", phases(phase))
        bet = bet(fichas)
        if (sumD == 7 or 11):
            fichas = fichas + bet
            wl = 2
            phase = 0
        elif (sumD == 2 or 3 or 12):
            fichas = fichas - bet
            wl = 2
            phase = 0
        elif (sumD == 4 or 5 or 6 or 8 or 9 or 10):
            phase = 1
            #this controls the change of phase into point
    return phase

def point(phase, sumD, fichas, bet):
    #method that organizes point phase
    print("O jogo está na fase ", {1}, ".", phases(phase))
    pointS = sumD
    rolldice(d1,d2)
    if (sumD == pointS):
        fichas = fichas + bet
        wl = 1
    elif (sumD == 7):
        fichas = fichas - bet
        wl = 0
    else:
        rolldice(d1, d2)
    return wl

