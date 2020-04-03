
def rolldice (d1, d2):
    d1 = random.range[1, 6, 1]
    d2 = random.range[1, 6, 1]
    sumD = d1 + d2
    return sumD

def bet(fichas):
    phase = 2
    bet = int(input("Quanto você gostaria de apostar?"))
    if (bet > fichas):
        print("Aposta inválida. Por favor, aposte uma quantidade de fichas que você possua.")
        phase = 3
    return bet

def rewind(wl):
    if (wl == 0):
        reset = input("Você perdeu o jogo. Você gostaria de jogar novamente?")
    elif (wl == 1):
        reset = input("Parabéns, você venceu o jogo com ", {1}, "fichas! Você gostaria de jogar novamente?", fichas)
    return phase

def plb (fichas, sumD):
    if (phase != 0):
        return null
    else:
        bet(fichas)
        if (sumD == 7 or 11):
            fichas = fichas + bet
            wl = 1
    return phase

fichas, bet = 10
d1, d2 = 0
wl, phase = 2
reset = " "
