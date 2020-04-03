import sys
from enum import Enum
import random

fichas, bet = 10, 11
d1, d2 = 0, 0
sumD = d1 + d2
pointS = sumD
wl, phase = 2, 2
fase, num = 5, 5

class phases(Enum):
    COME_OUT = 0
    POINT = 1

def instructions():
    print("No jogo de Craps, você tem duas possibilidades:")
    print("Você pode, a qualquer momento, decidir se quer apostar o valor da soma dos dois dados que o computador jogou, ou sair do jogo.")
    print("O jogo tem duas fases: COME OUT e POINT.")
    instr = input("Você gostaria de ler mais sobre alguma delas? (sim/não)")
    print(" ")
    if (instr == "sim"):
        instr = " "
        num = int(input("Sobre qual você quer saber mais? (1 ou 2, respectivamente)"))
        if (num == 1):
            print("FASE COME OUT")
            print("Esta fase começa antes da fase POINT.")
            print("Durante esta fase é possível fazer qualquer aposta.")
            print("Ela termina com o Pass Line Bet, um dos tipos de aposta.")
        elif (num == 2):
            print("FASE POINT")
            print("Durante esta fase é possível fase qualquer aposta exceto o Pass Line Bet.")
            print("Esta fase começa ou não de acordo com o Pass Line Bet.")
            print("Durante esta fase, a soma dos dados torna-se o valor do POINT, e são jogados novos dados, com a mesma aposta inicial do Pass Line Bet.")
            print("Se ambos derem iguais, você vence o jogo, e ganha o valor que apostou em fichas.")
            print("Se a soma nova der igual a 7, você perde o jogo e todas suas fichas.")
            print("Este processo é repetido até que você ganhe, perca ou saia do jogo.")
    instr = input("Também existem as apostas. Você gostaria de ler mais sobre elas?")
    if (instr == "sim"):
        betInstr()
    return none

def betInstr():
    print("Caso você queira apostar, você tem 4 opções de apostas:")
    print("Pass Line Bet, Field, Any Craps, e Twelve.")
    print("Você pode fazer mais de uma aposta ao mesmo tempo, com valores diferentes de fichas.")
    print("Conforme você for jogando, você terá a opção de ler as instruções da aposta que estiver prestes a fazer.")
    instr = input("Você quer ler sobre alguma aposta agora? (sim/não)")
    print(" ")
    if (instr == "sim"):
        num = int(input("Sobre qual você quer saber mais? (1 a 4, respectivamente)"))
        if (num == 1):
            print("PASS LINE BET")
            print("Se você acertar a aposta e for 7 ou 11, você recebe duas vezes o valor apostado.")
            print("Se você acertar a aposta e for 2, 3 ou 12, você perde o valor apostado.")
            print("No entanto, se você acertar a aposta e 4, 5, 6, 8, 9 ou 10, o jogo vai para a fase POINT.")
        if (num == 2):
            print("FIELD")
            print("Esta aposta pode ser feita a qualquer momento durante o jogo.")
            print("Se você acertar a aposta e for 5, 6, 7 ou 8, você perde o valor apostado.")
            print("Se você acertar a aposta e for 2, você recebe duas vezes o valor apostado.")
            print("Se você acertar a aposta e for 12, você recebe três vezes o valor apostado.")
        if (num == 3):
            print("ANY CRAPS")
            print("Esta aposta pode ser feita a qualquer momento durante o jogo.")
            print("Se você acertar a aposta e for 2, 3, 12, você recebe sete vezes o valor apostado.")
            print("Se você acertar a aposta e for qualquer outro valor, você perde o valor apostado.")
        if (num == 4):
            print("TWELVE")
            print("Esta aposta pode ser feita a qualquer momento durante o jogo.")
            print("Se você acertar a aposta e for 12, você recebe trinta vezes o valor apostado.")
            print("Se você acertar a aposta e for qualquer outro valor, você perde o valor apostado.")
    return none

def rolldice (d1, d2):
    #rola 2 dados random e soma
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6) 
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
        reset = input("Parabéns, você venceu o jogo com ", {0}, " fichas! Você gostaria de jogar novamente? (sim/não)".format(fichas))
        #winning doesn't reset chips like a cassino as well
    if (reset == "sim"):
        wl = 2
        phase = 0
        print("Você possui ", {1}, " fichas.".format(fichas))
    elif (reset == "não" or "nao"):
        sys.exit(0)
    return phase

def plb (phase, fichas, sumD, wl):
    #pass line bet
    if (phase != 0):
        #guarantee of only during come out
        return phase
    else:
        print("O jogo está na fase ", {0}, ".".format(phases(phase)))
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
    print("O jogo está na fase ", {0}, ".".format(phases(phase)))
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

def field(sumD, fichas):
    bet = bet(fichas)
    if (sumD == 5 or 6 or 7 or 8):
        fichas = fichas - bet
    elif(sumD == 2):
        fichas = fichas + 2*bet
    elif (sumD == 12):
        fichas = fichas + 3*bet
    else:
        null
    return fichas

def anyC(sumD, fichas):
    bet = bet(fichas)
    if (sumD == 2 or 3 or 12):
        fichas = fichas + 7*bet
    else:
        fichas = fichas - bet
    return fichas

def twelve(sumD, fichas):
    bet = bet(fichas)
    if (sumD == 12):
        fichas = fichas + 30*bet
    else:
        fichas = fichas - bet
    return fichas

def leave():
    sys.exit(0)
    return void

#newb = input("Bem-vindo ao jogo de Craps. Você já conhece o jogo? (sim/não)")
#if (newb == "não" or "nao"):
    instructions()

rolldice(d1, d2)
phase = 0
print("O jogo está na fase ", {0}, ".".format(phases(phase)))
print("Você atualmente tem ", {0}, " fichas.".format(fichas))

i = input("Você gostaria de apostar ou sair?")
if (i == "apostar"):
    print("Pass Line Bet, Field, Any Craps ou Twelve?")
    print("Digite plb, field, anyC ou twelve se você deseja fazer estas apostas.")
    print("Lembrando que é possível fazer mais de uma aposta.")
    print("Digite um de cada vez.")
    apostas = [input()]*4
    count = 0
    while(count != 4):
        if (apostas[count] == "plb"):
            plb(phase, fichas, sumD, wl)
        elif(apostas[count] == "field"):
            field(sumD, fichas)
        elif(apostas[count] == "anyC"):
            anyC(sumD, fichas)
        elif(apostas[count] == "twelve"):
            twelve(sumD, fichas)
        count+=1
elif (i == "sair"):
    leave()
else:
    print("Desculpe. Não entedi, pode repetir?")