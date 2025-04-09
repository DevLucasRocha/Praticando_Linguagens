#Código inicial:

"""number_1 = int(input("Escreva o primeiro número: "))
number_2 = int(input("Escreva o segundo número: "))

resultado = number_1 + number_2
print("A soma de", number_1, "+", number_2, "=", resultado)"""


#Código corrigido e melhorado fazendo o uso de try-except:

try:
    number_1 = int(input("Escreva o primeiro número: "))
    number_2 = int(input("Escreva o segundo número: "))

    resultado = number_1 + number_2

    print(f'A soma de {number_1} + {number_2} = {resultado}')
except ValueError:
    print("Erro: Por favor, insira apenas números inteiros.")
    
