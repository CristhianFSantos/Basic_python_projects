import os
from time import sleep


def loading(message):
    for index in range(8):
        dots = [
            f'{message}   ',
            f'{message}.',
            f'{message}..',
            f'{message}...',
            f'{message}   ',
            f'{message}.',
            f'{message}..',
            f'{message}...',
        ]
        print(f"{dots[index]}", end="\r")
        sleep(0.3)


while True:
    os.system("cls")
    print("=*=" * 20)
    print(
        "\n• Para converter minutos em decimal, digite [1].\n• Para calcular a diferença entre horários, digite [2].\n• Ou para calcular a diferença entre horários já convertidos para decimal, digite [3]."
    )
    print("=*=" * 20)
    escolha_app = int(input("Escolha uma das opções acima:\n"))
    loading("CARREGANDO")
    os.system("cls")

    if escolha_app == 1:
        convert = int(
            input("Insira o valor em minutos (mm) para conversão : "))
        decimal = (convert / 60) * 100
        print(f"\nO valor {convert} em decimal é: {round(decimal)}\n")

    elif escolha_app == 2:
        hora_in = int(input("\nInforme a hora do tempo inicial: "))
        min_in = int(input("Informe os minutos do tempo inicial: "))

        hora_fim = int(input("\n\nAgora informe a hora do tempo final: "))
        min_fim = int(input("Agora informe os minutos do tempo final: "))
        loading("CARREGANDO")
        os.system("cls")
        print(
            f"Sua tarefa foi iniciada em {hora_in}:{min_in} e encerrada em {hora_fim}:{min_fim}.\nSeu tempo de execução foi,"
        )
        #conta Matemática
        hora_result = hora_fim - hora_in
        min_result = min_fim - min_in
        if min_result < 0:
            min_result = (min_result + (+60))
            hora_result = (hora_result - 1)
        if hora_result <= 0 and min_result > 9:
            print(f"0{hora_result}:{min_result} minutos\n")
        elif hora_result <= 0 and min_result <= 9:
            print(f"0{hora_result}:0{min_result} minutos\n")
        elif hora_result == 1 and min_result == 0:
            print(f"{hora_result}:0{min_result} hora\n")
        elif hora_result == 1 and min_result > 9:
            print(f"{hora_result} hora e {min_result} minutos\n")
        elif hora_result == 1 and min_result <= 9:
            print(f"{hora_result} hora e 0{min_result} minutos\n")
        elif min_result <= 9:
            print(f"{hora_result} horas e 0{min_result} minutos\n")
        elif min_result > 9:
            print(f"{hora_result} horas e {min_result} minutos\n")

    elif escolha_app == 3:
        hora_in = int(input("\nInforme a hora do tempo inicial: "))
        min_in = int(input("Informe os minutos do tempo inicial: "))

        hora_fim = int(input("\n\nAgora informe a hora do tempo final: "))
        min_fim = int(input("Agora informe os minutos do tempo final: "))
        loading("CARREGANDO")
        os.system("cls")
        print(
            f"Sua tarefa foi iniciada em {hora_in}:{min_in} e encerrada em {hora_fim}:{min_fim}.\nSeu tempo de execução foi,"
        )
        #conta Matemática
        hora_result = hora_fim - hora_in
        min_result = min_fim - min_in
        if min_result < 0:
            min_result = (min_result + (+60))
            hora_result = (hora_result - 1)
        convertido = (convert / 60) * 100
        if hora_result <= 0:
            print(f" {hora_result}:{convertido}")

    else:
        print("Valor incorreto!!\n")

    os.system("pause")