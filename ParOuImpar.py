import os
numero = int(input("Insira um número: "))
condicoes = ["par", "ímpar"]
resposta = numero % 2
print(f"O número informado é {condicoes[resposta]}")
os.system("pause")