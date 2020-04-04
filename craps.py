import sys
from enum import Enum
import random

class phases(Enum):
    COME_OUT = 0
    POINT = 1

fochas = 50
betT = fochas+1
d1, d2 = 0, 0
dice = d1 + d2
pointS = dice
wl, phase = 2, 2

def instructions():
    print("No jogo de Craps, você tem duas possibilidades:")
    print("Você pode, a qualquer momento, decidir se quer apostar o valor da soma dos dois dados que o computador jogou, ou sair do jogo.")
    print("O jogo tem duas fases: COME OUT e POINT.")
    instr = input("Você gostaria de ler mais sobre alguma delas? (sim/não) \n")
    if (instr == "sim"):
        instr = " "
        num = int(input("Sobre qual você quer saber mais? (1 ou 2, respectivamente)\n"))
        if (num == 1):
            print("FASE COME OUT")
            print("Esta fase começa antes da fase POINT.")
            print("Durante esta fase é possível fazer qualquer aposta.")
            print("Ela termina com o Pass Line Bet, um dos tipos de aposta.")
        elif (num == 2):
            print("FASE POINT")
            print("Durante esta fase é possível fazer qualquer aposta exceto o Pass Line Bet.")
            print("Esta fase começa ou não de acordo com o Pass Line Bet.")
            print("Durante esta fase, a soma dos dados torna-se o valor do POINT, e são jogados novos dados, com a mesma aposta inicial do Pass Line Bet.")
            print("Se ambos derem iguais, você vence o jogo, e ganha o valor que apostou em fichas.")
            print("Se a soma nova der igual a 7, você perde o jogo e todas suas fichas.")
            print("Este processo é repetido até que você ganhe, perca ou saia do jogo.")
    instr = input("Também existem as apostas. Você gostaria de ler mais sobre elas?\n")
    if (instr == "sim"):
        betInstr()

def betInstr():
    print("Caso você queira apostar, você tem 4 opções de apostas:")
    print("Pass Line Bet, Field, Any Craps, e Twelve.")
    print("Você pode fazer mais de uma aposta ao mesmo tempo, com valores diferentes de fichas.")
    print("Conforme você for jogando, você terá a opção de ler as instruções da aposta que estiver prestes a fazer.")
    instr = input("Você quer ler sobre alguma aposta agora? (sim/não)\n")
    if (instr == "sim"):
        num = int(input("Sobre qual você quer saber mais? (1 a 4, respectivamente)\n"))
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
    betonit= fichas + 1
    print("Você tem {0} fichas.".format(fichas))
    if (fichas != 0):
        while (betonit > fichas):
            betonit = int(input("Digite quantas fichas você gostaria de apostar, por favor.\n"))
            if (betonit > fichas):
                #system security
                print("Aposta inválida. Por favor, aposte uma quantidade de fichas que você possua.")
        return betonit
    else:
        wl = 0
        rewind(wl, fichas)

def rewind(wl, fichas):
    #resets game
    rset = " "
    if (wl == 0):
        rset = input("Você perdeu o jogo. Você gostaria de jogar novamente? (sim/não)\n")
        if (fichas == 0):
            #resets game in case of loss
            #set as an if because if scoop, it's possible to cary on with your own chips as in real cassino
            fichas = 10
    elif (wl == 1):
        rset = input("Parabéns, você venceu o jogo com {0} fichas! Você gostaria de jogar novamente? (sim/não)\n".format(fochas))
        #winning doesn't reset chips like a cassino as well
    if (rset == "sim"):
        wl = 2
        print("Você possui {0} fichas.".format(fochas))
    elif (rset == "não" or "nao"):
        sys.exit(0)
    return phase

def plb (phase, sumD, fichas):
    #pass line bet
    if (phase != 0):
        #guarantee of only during come out
        return fichas
    else:
        print("PASS LINE BET")
        print("O jogo está na fase {0}.".format(phases(phase)))
        betT = bet(fichas)
        if (sumD==7) or (sumD==11):
            fichas=fichas+betT
            print("Você agora tem {0} fichas." .format(fichas))
            return fichas
        elif (sumD== 2) or (sumD==3) or (sumD==12):
            fichas=fochas-betT
            print("Você agora tem {0} fichas." .format(fichas))
            return fichas
        elif (sumD== 4) or (sumD==5) or (sumD==6) or (sumD==8) or (sumD==9) or (sumD==10):
            #this controls the change of phase into point
            phase = 1
            point(sumD, fichas, phase)

def point(dice, fichas, phase):
    #method that organizes point phase
    print("O jogo está na fase {0}.".format(phases(phase)))
    pointS = dice
    sumD=rolldice(d1,d2)
    wl=2
    while (wl == 2):
        if (sumD == pointS):
            fichas = fichas + betT
            print("Você agora tem {0} fichas." .format(fichas))
            wl = 1
            return wl
        elif (sumD == 7):
            fichas = 0
            print("Você agora tem {0} fichas." .format(fichas))
            wl = 0
            return wl
        else:
            sumD=rolldice(d1, d2)

def field(sumD, fichas, phase):
    betT = bet(fichas)
    print("FIELD")
    print("O jogo está na fase {0}.".format(phases(phase)))
    if (sumD == 5) or (sumD==6) or (sumD==7) or (sumD==8):
        fichas = fichas - betT
        print("Você agora tem {0} fichas." .format(fichas))
        return fichas
    elif(sumD == 2):
        fichas = fichas + 2*betT
        print("Você agora tem {0} fichas." .format(fichas))
        return fichas
    elif (sumD == 12):
        fichas = fichas + 3*betT
        print("Você agora tem {0} fichas." .format(fichas))
        return fichas
    else:
        null
        return fichas

def anyC(sumD, fichas, phase):
    betT = bet(fochas)
    print("ANY CRAPS")
    print("O jogo está na fase {0}.".format(phases(phase)))
    if (sumD == 2) or (sumD==3) or (sumD==12):
        fichas = fichas + 7*betT
        print("Você agora tem {0} fichas." .format(fichas))
        return fichas
    else:
        fichas = fichas - betT
        print("Você agora tem {0} fichas." .format(fichas))
        return fichas

def twelve(sumD, fichas, phase):
    betT = bet(fichas)
    print("TWELVE")
    print("O jogo está na fase {0}.".format(phases(phase)))
    if (sumD == 12):
        fichas = fichas + 30*betT
        print("Você agora tem {0} fichas." .format(fichas))
        return fichas
    else:
        fichas = fichas - betT
        print("Você agora tem {0} fichas." .format(fichas))
        return fichas

newb = input("Bem-vindo ao jogo de Craps. Você já conhece o jogo? (sim/não)\n")
if (newb != "sim"):
    instructions()
else:
    1+1

dice = rolldice(d1, d2)
phase = 0
print("O jogo está na fase {0}.".format(phases(phase)))
print("Você atualmente tem  {0} fichas.".format(fochas))

i = input("Você gostaria de apostar ou sair?\n")

if (fochas == 0):
    leave()

if (i == "apostar"):
    print("Pass Line Bet, Field, Any Craps ou Twelve?")
    print("Digite plb, field, anyC ou twelve se você deseja fazer estas apostas.")
    print("Lembrando que é possível fazer mais de uma aposta.")
    print("Digite um de cada vez.")
    count = int(input("Digite quantas apostas você gostaria de fazer, e depois suas apostas. \n"))
    apostas = [" "]*count
    
    count = 0
    while (count != len(apostas)):
        apostas[count] = input()
        count +=1

    count = 0
    while(count != len(apostas)):
        if (apostas[count] == "plb"):
            fochas = plb(phase, dice, fochas)
            if (fochas == 0):
                phase = rewind(wl, fochas)
        elif(apostas[count] == "field"):
            fochas = field(dice, fochas, phase)
            if (fochas == 0):
                phase = rewind(wl, fochas)
        elif(apostas[count] == "anyC" or "anyc"):
            fochas = anyC(dice, fochas, phase)
            if (fochas == 0):
                phase = rewind(wl, fochas)
        elif(apostas[count] == "twelve"):
            fochas = twelve(dice, fochas, phase)
            if (fochas == 0):
                phase = rewind(wl, fochas)
        count+=1
else:
 sys.exit(0)   

phase=rewind(wl, fochas)

