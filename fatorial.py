print(
    "Faça um programa em Python que calcule o fatorial de um número informado pelo usuário.\n"
)

numero = int(input("Digite um número inteiro positivo: "))
contador = 1
fatorial = 1
while contador <= numero:
    fatorial = fatorial * contador
    contador = contador + 1
print(f"{numero} fatorial é: {fatorial}")