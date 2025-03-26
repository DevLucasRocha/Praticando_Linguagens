number1 = float(input("Escreva o primeiro número: "))
number2 = float(input("Escreva o segundo número: "))
            
operacao = str(input("Escolha a operação: "))
            
def calculo(number1, number2):
    if operacao == "+":
        return number1 + number2
    elif operacao == "-":
        return number1 - number2
    elif operacao == "*":
        return number1 * number2
    elif operacao == "/":
        return number1 / number2

resultado = calculo

print(f"{number1} {operacao} {number2} = {resultado}")   

            

            

            
