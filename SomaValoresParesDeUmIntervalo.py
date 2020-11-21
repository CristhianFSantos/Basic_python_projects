print(
    sum(number for number in range(
        int(input("Defina um valor inicial para o intervalo: ")),
        int(input("Defina um valor final para o intervalo: ")) + 1)
        if number % 2 == 0))
