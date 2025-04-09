#Sorteando números aletórios

import random
import time
import os
import sys
print("Sorteando números aleatórios")
print("-"*30)
print("Gerando 5 números aleatórios entre 1 e 10")
print("-"*30)
time.sleep(2)
for i in range(5): # Gera 5 números aleatórios
    print(random.randint(1,5)) # Gera números aleatórios entre 1 e 10
    time.sleep(1)
print("-"*30)
print("Maior número sorteado: ", end="")
os.system("cls") # Limpa a tela
print(f"menor número sorteado:{i}", end="") 
os.system("cls") # Limpa a tela
print("Fim do programa")
print("-"*30)