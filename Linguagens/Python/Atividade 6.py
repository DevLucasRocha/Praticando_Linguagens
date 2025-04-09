import random
import time

print("Gerando 5 números aleatórios entre 1 e 10")
print("-" * 30)
print("Sorteando números...")
time.sleep(2)

numeros = (
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10)
)
for n in numeros:
    print(n, end=" ", flush=True) # flush=True mostra o valor do print imediatamente
    time.sleep(0.3)

print(f"\nMaior número sorteado: {max(numeros)}")
print("-" * 30)
print(f"Menor número sorteado: {min(numeros)}")
print("-" * 30)
print(f"Soma dos números sorteados: {sum(numeros)}")
