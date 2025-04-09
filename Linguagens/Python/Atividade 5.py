times = 'Vasco', 'São Paulo', 'Flamengo', 'Palmeiras', 'Grêmio', 'Atlético Mineiro', 'Internacional', 'Corinthians', 'Santos', 'Fluminense', 'Bahia', 'Sport Recife', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético Goianiense', 'Juventude'
print(f'Lista de times do Brasileirão: {times}')
print('='*50)
print(f'Os 5 primeiros são {times[0:5]}')
print('='*50)
print(f'Os 4 últimos são {times[-4:]}')
print('='*50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('='*50)
while True:
    change = str(input('Escolha um time: ')).strip().title()
    if change in times:
        print(f'O {change} está na {times.index(change)+1}ª posição')  #+1 para corrigir o índice
    elif change not in times:
        print('Time não encontrado, tente novamente')
        continue
    loop = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if loop == 'N':
            break
    
