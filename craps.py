import sys
from enum import Enum

fichas, bet = 10
d1, d2 = 0
sumD = d1 + d2
pointS = sumD
wl, phase = 2
reset = " "

class phases(Enum):
    COME_OUT = 0
    POINT = 1
    APOSTAS = 2

def rolldice (d1, d2):
    d1 = random.range[1, 6, 1]
    d2 = random.range[1, 6, 1]
    sumD = d1 + d2
    return sumD

def bet(fichas):
    phase = 2
    bet = int(input("Digite quantas fichas você gostaria de apostar, por favor."))
    if (bet > fichas):
        print("Aposta inválida. Por favor, aposte uma quantidade de fichas que você possua.")
        phase = 2
    return bet

def rewind(wl):
    if (wl == 0):
        reset = input("Você perdeu o jogo. Você gostaria de jogar novamente? (sim/não)")
    elif (wl == 1):
        reset = input("Parabéns, você venceu o jogo com ", {1}, " fichas! Você gostaria de jogar novamente? (sim/não)", fichas)
    if (reset == "sim"):
        wl = 2
        phase = 0
    elif (reset == "não" or "nao"):
        sys.exit(0)
    return phase

def plb (fichas, sumD):
    if (phase != 0):
        return null
    else:
        bet(fichas)
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
    return phase


