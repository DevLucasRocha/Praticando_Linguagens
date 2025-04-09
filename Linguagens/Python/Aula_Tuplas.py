# Tuplas são imutáveis (não podem ser mudadas)
# pode declarar variável tuplas sem o uso do parenteses a partir do python 3.5

jogo = 'RPG','TERROR','2DPIXEL','MOBILE','CONSOLE'

# 3 maneiras para poder manipular as tuplas:

for videogame in jogo:
    print(f"Eu vou jogar {videogame}")

for videogame in range(0, len(jogo)):
    print(f'Eu vou jogar {jogo[videogame]} na posição {videogame}')

for pos, videogame in enumerate(jogo):
    print(f"Eu vou jogar {videogame} na posição {pos}")

print(sorted(jogo)) # sorted altera ordem da dos dados da tupla

print(jogo)

print('Joguei que só!')

# print(variavel.count) - conta a quantidade de dados
print(jogo.count)

# print(variavel.index) - mostra a posição (índice) do primeiro elemento encontrado na lista ou tupla.
print(jogo.index('RPG'))