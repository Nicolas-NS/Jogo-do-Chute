import random


def numero_Mm(tentativa, numero_aleatorio):
    if tentativa < numero_aleatorio:
        return "número muito baixo!!"
    else:
        return "número muito alto!!"


def jogar():
    numero_aleatorio = random.randint(1, 100)

    print('=-=' * 5, "JOGO DO CHUTE", '=-=' * 5)

    for i in range(5):

        tentativa = input("escreva um número entre 1 a 100: ").strip()

        try:
            valor = int(tentativa)

            if valor != numero_aleatorio:

                dica = numero_Mm(valor, numero_aleatorio)

                print(dica)
                print(f"tentativa {i+1}/5")
                print("=-=" * 20)

            else:
                print("╔══════════════════════════════╗")
                print("║        !!VOCÊ GANHOU!!       ║")
                print("╚══════════════════════════════╝")

                print(f"O número é {numero_aleatorio}")
                print("=-=" * 20)
                return  # termina o jogo se ganhar

        except:
            print("Isso não é um número inteiro!")
            print(f"tentativa {i+1}/5")
            print("=-=" * 20)

    # Se saiu do for sem ganhar → perdeu
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("  ✖  VOCÊ   P E R D E U  ✖   ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print(f"!! O NÚMERO ERA {numero_aleatorio} !!")
