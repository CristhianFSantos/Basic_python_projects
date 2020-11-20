#Tabuada
from time import sleep
import os
numero = int(input("\nInforme um número: "))
print("\nProcessando...\n")
sleep(2)
for contador in range(1, 11):
    print(f"{numero} X {contador} = {numero * contador}")
print("\nFim")
os.system("pause")
