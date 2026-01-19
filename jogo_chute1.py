# Desenvolva um jogo de acerte o número, onde o computador escolhe um número inteiro aleatório de 0 a 10, e o usuário tem 5 tentativas para adivinhar o número

import random

numero_aleatorio = random.randint(1, 100)

def numero_Mm(tentativa):
    if tentativa < numero_aleatorio:
        baixo = print("número muito baixo!!")
    else:
        baixo = print("número muito alto!!")
    return baixo

chances = 0

while chances < 5:
    tentadiva= (input("escreva um número entre 1 a 100: ")).strip()

    try:
        valor = int(tentadiva)
        chances +=  1
        if valor != numero_aleatorio:
            t1 = numero_Mm(valor)
            print(f"tentadiva {chances}/5")
        else:
            print('VOCÊ GANHOU!!')
            print (f"O número é {numero_aleatorio}")
    except :
        print("isso não é um número inteiro seu burro!!!")
        chances == 0


print("VOCÊ PERDEU!!!")
print(f"o número era {numero_aleatorio}")
