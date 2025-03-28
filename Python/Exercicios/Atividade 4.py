#faça um programa de número por extenso

numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
          break
    else:
         print("Tente novamente. ", end='') # end="" - ele não vai pular a linha e vai juntar com a próxima escrita
print(f"Você digitou o número {numeros_extenso[num]}")


        
    

