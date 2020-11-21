mensagem = str(input("Digite uma mensagem: \n")).strip()
palavras = mensagem.split()
juncao = ''.join(palavras)
inverso = ''
for letra in range(len(juncao) - 1, -1, -1):
    inverso += juncao[letra]
if inverso == juncao:
    print("A mensagem é um palindromo")
else:
    print("A mensagem não é um palindromo")
print(f"O inverso de {juncao} é {inverso}")