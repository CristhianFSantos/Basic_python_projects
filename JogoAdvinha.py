from random import randint
from time import sleep
import os


def QuebraLinha():
    print("\n", "--=--" * 15, "\n")


def validacao(jogador):
    if jogador <= 5 and jogador >= 1:
        return jogador
    else:
        sleep(2)
        print("Você inseriu um valor incorreto")
        os._exit(0)


QuebraLinha()
print("\nVou pensar em um número entre 1 e 5! TENTE ADVINHAR...")
QuebraLinha()
for tentativa in range(0, 3):
    computador = randint(1, 5)
    jogador = int(input("\nEm que número pensei ?  "))
    validacao(jogador)
    print("\nProcessando...")
    sleep(2)
    if jogador == computador:
        print("\nPARABÉNS! Consegiu me derrotar! ")
        break
    else:
        print(
            f"\nTente novamente, eu pensei em {computador} e não em {jogador}")
        print(f"Você ainda tem {3-tentativa} tentativas")
    sleep(2)