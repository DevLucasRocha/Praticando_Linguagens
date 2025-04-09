#Sorteando números aletórios

import random
import time
import os
import sys
print("Sorteando números aleatórios")
print("-"*30)
print("Gerando 10 números aleatórios entre 1 e 10")
print("-"*30)
time.sleep(2)
for i in range(10): # Gera 10 números aleatórios
    print(random.randint(1,10)) # Gera números aleatórios entre 1 e 10
    time.sleep(1)
print("-"*30)
print("Fim do programa")
print("-"*30)