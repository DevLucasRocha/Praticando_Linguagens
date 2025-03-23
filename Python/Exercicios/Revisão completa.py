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
peso_1 = float(input('Digite seu peso :'))

resultado_teste = nome_1,idade_1,peso_1'''

#dá para identificar qual o tipo da váriavel usando o comando type.

'''print (type(nome_1))
print (type(idade_1))
print (type(peso_1))'''

#Matemática - sinais de operação: 
# % - operador resto, resto da divisão
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
#São conjuntos de dados armazenados em uma váriável. Na lista existe o indice sempre começar do 0,1,2,3... isso seria a ordem dos dados não o dado em si, siga o exemplo abaixo.

lista_numeros = [1,2,3]

lista_numeros[0] = 5
#perceba que acima foi atribuido o valor '5' no indice '0' substituindo o valor 1 por 5. e a lista não precisa ser só numeros, pode ser atribuidos strings, floats, int e etc..

print(lista_numeros [0])
print(lista_numeros [1])
print(lista_numeros [2])

#existem vários métodos, procure no google e pratique.

#REPETIÇÕES
#FOR - loop que pecorre sequências, repetindo ações para cada elemento;

'''notas = []
for x in range(5):
    codigo_aluno = input('RM:')
    nota = float (input('Nota:'))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)'''

    #append - adiciona um elemento no final da lista, neste caso está adicionando no final da lista de 'notas'

'''print('quantidade de notas', len(notas))'''

#len - contar o número de itens de uma sequência, como uma string, lista, tupla ou dicionário.

'''for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print('O RM', codigo_aluno, 'tirou a nota:', nota)'''

#While - loop que executa ações enquanto a condição for verdadeira ou eternamente.

notas = []
contador = 1

while contador <= 5:
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    # alternativa: contador += 1
    contador = contador + 1
print('quantidade de notas', len (notas))

#existe também o "while True" T sempre em maiusculo (enquanto verdadeiro) gera um loop infinito, porém se for usado o comando "break" quebra o loop.

# é necessário um contador para atribuir valor e gerar o loop no while pois ele significa enquanto algo for >= ou <= a tanto vai continuar rodando o loop ( se não pode fazer o uso do break)

# DICIONÁRIOS - usam chave e valor para armazenar informações: variavel = {"chave: "valor"}

#informações do jogador

player = {
    "nome" : "Lucas Airon",
    "Level": 549,
    "HP" : 7254,
    "exp": 1523689,
    "dano": 45689,
}

#lista de inimigos
npcs = {
    {"nome": "Monstrinho", "dano": 2, "HP" : 50, "exp": 5},
    {"nome": "Monstro", "dano": 5, "HP" : 100, "exp": 10},
    {"nome": "Monstrão", "dano": 200, "HP" : 150, "exp": 350},
    {"nome": "Chefão", "dano": 580, "HP" : 600, "exp": 1250},
}

# Funções - blocos reutilizaveis de códigos para fazer tarefas especificas usando comando "def"
# demonstração usando loop

def minha_funcao(valor1, valor2):
    return valor1 + valor2


while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))

    resposta = minha_funcao(valor1, valor2)
    print(valor1, "+", valor2, "=", resposta)

