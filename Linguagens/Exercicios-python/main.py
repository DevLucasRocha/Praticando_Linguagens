#comando print para mostrar textos em formato string(ficam entre aspas)

print("Revisão de python")

#váriavéis
#váriavel são objetos em que eu posso atribuir algo a ela
#Exemplo
'''nome = "Lucas Rocha"
idade = 25
peso = 88.8
print(nome,idade,peso)'''

#IMPUT - armazena entrada de dados do usuário
#Tendo em mente disso, temos os tipos de váriáveis onde no exemplo abaixo foi usado números inteiros (int) e números fracionados ou ponto fluante (float)

'''nome_1 = input("Digite seu nome: ")
idade_1 = int(input('Digite sua idade: '))
peso_1 = float(input('Digite seu peso :'))'''

Resultado_1 = nome_1,idade_1,peso_1

#dá para identificar qual o tipo da váriavel usando o comando type.

print (type(nome_1))
print (type(idade_1))
print (type(peso_1))

#Matemática - sinais de operação: 

soma = 1+1
subtracao = 1-1
multiplicacao = 4*4
divisao = 30/3
potencia = 7**2

print('soma', soma)
print('subtração', subtracao)
print('multiplicação', multiplicacao)
print('divisão', divisao)
print('pontencia', potencia)

#ESTRUTURA E COMANDO CONDICIONAIS!
#lembrando que é algo que precisa de uma condição, exemplo, só entra na bala SE for >= que 18 anos, SE não for, não vai entrar.

salario = float(input('Informe seu salário:'))

#usamos IF para SE, ELIF para CASO SE e ELSE para SE NÃO;
#nas condicionais é muito usado os sinais de comparação (>,<,>>>,<<<,<=,>=,==)

if salario <= 3000:
    print('Programador junior!')
elif salario > 3000 and  salario <= 6000:
    print('Programador pleno!')
elif salario > 6000 and salario <= 15000:
    print('Programador senior!')
else:
    print('Gerente de projetos!')

# quando a linha vai um pouco mais para frente como no exemplo acima, se chama IDENTAÇÃO(são espaçamentos consistentes no inicio da linha do código, usado para demilitar blocos de código). Pode-se usar o atalho TAB.

#LISTAS;
#
