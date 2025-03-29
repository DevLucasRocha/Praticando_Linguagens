#faça um programa de número por extenso

numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num < 0 or num > 20:  # Verifica se o número está fora do intervalo
        print("Tente novamente. ", end='')  # Não pula linha
    else:
        print(f"Você digitou o número {numeros_extenso[num]}")
    
    loop = input("Quer continuar? sim/não\n").strip().lower()
    if loop in "n":
        break  # Sai do loop
    else:
        continue  # Continua o loop
        
    

