
#2 fases: come out, point
#SEMPRE informar qual fase tá
#computador lança 2 d6 secretos
    #objetivo é adivinhar o resultado?
#jogador escolhe se aposta ou sai
    #automaticamente removido se tiver sem ficha
#SEMPRE informar o jogador sobre o gamestate
    #mostrar possibilidades de apostas e valores
    #podem ser feitas apostas simultâneas de valores e tipos diferentes

#tipos de apostas
    #pass line bet
        #SÓ NO COME OUT
        #7 ou 11: win (double fichas apostadas)
        #2, 3 ou 12 (CRAPS): loss (perde apostadas e recebe nada)
        #4, 5, 6, 8, 9 ou 10: jogo vai pra POINT
            #em POINT: aposta mantém 
                #soma dos dados vira point
                #relança os d6
                    #se d6 == point, win
                    #se d6 == 7, loss
                    #else, rejoga até conseguir point ou sair 7
        #no fim de plb, acaba esta rodada e começa COME OUT nova
    #field
        #em qualquer fase
        #5, 6, 7 ou 8: perde apostadas e recebe nada
        #3, 4, 9, 10 ou 11: neutro (recebe de volta o que apostou, delta 0)
        #2: dobra as fichas apostadas
        #12: triplica as fichas apostadas
    #any craps
        #em qualquer fase
        #2, 3 ou 12: x7 apostadas
        #else, perde aposta
    #twelve
        #em qualquer fase
        #12: x30 apostadas
        #else, perde aposta

#will need:
    #var: d1, d2, fichas, sumD, pointS, wl, phase
        #wl como controle de rodadas
        #phase como controle de come out vs point
    #methods:
        #rolldice: rola 2 dados random e soma - return sumD
        #plb: testa as condições - retorna phase
            #point: testa as condições - retorna wl
        #field: testa as condições - retorna phase
        #anyC: testa as condições - retorna phase
        #twelve: testa as condições - retorna phase

def rolldice (d1, d2):