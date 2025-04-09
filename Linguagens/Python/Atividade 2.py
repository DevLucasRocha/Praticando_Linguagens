
# Código praticado

'''def calculo(number1, number2):
    if operacao == "+":
        return number1 + number2
    elif operacao == "-":
        return number1 - number2
    elif operacao == "*":
        return number1 * number2
    elif operacao == "/":
        return number1 / number2

while True:
    number1 = float(input("Escreva o primeiro número: "))
    number2 = float(input("Escreva o segundo número: "))

    operacao = str(input("Escolha a operação: "))

    print(f"{number1} {operacao} {number2} = {calculo(number1, number2):.1f}")

    loop = ' '
    while loop not in 'SN': 
        loop = str(input("Quer continuar? sim/não\n")).strip().upper()[0]
    if loop == "N":
        break'''

#Código corrigido e melhorado:

def converter_numero(valor):
    #Converte um número com vírgula para float, tratando erros.
    try:
        return float(valor.replace(",", "."))
    except ValueError:
        return None  # Retorna None se a conversão falhar

def calculo(number1, number2, operacao):
    
    #Realiza a operação matemática escolhida pelo usuário.

    if operacao == "+":
        return number1 + number2
    elif operacao == "-":
        return number1 - number2
    elif operacao == "*":
        return number1 * number2
    elif operacao == "/":
        if number2 == 0:
            return "Erro: divisão por zero!"
        return number1 / number2
    else:
        return "Erro: operação inválida!"

while True:
    # Solicita os números e converte para float
    number1 = converter_numero(input("Escreva o primeiro número: "))
    number2 = converter_numero(input("Escreva o segundo número: "))

    if number1 is None or number2 is None:
        print("Erro: Digite números válidos! (use '.' ou ',')")
        continue  # Volta para o início do loop

    operacao = input("Escolha a operação (+, -, *, /): ").strip()

    resultado = calculo(number1, number2, operacao)

    print(f"{number1:.2f} {operacao} {number2:.2f} = {resultado}")

    # Perguntar se o usuário quer continuar
    while True:
        loop = input("Quer continuar? (sim/não): ").strip().lower()
        if loop in ["sim", "não"]:
            break
        print("Erro: Digite 'sim' ou 'não'.")
    
    if loop == "não":
        print("Encerrando a calculadora. Até mais!")
        break



    
    

            

            
