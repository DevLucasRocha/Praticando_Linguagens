# Dicionário para armazenar os dados dos alunos
alunos = {}

# Função para adicionar um aluno
def adicionar_aluno(nome, idade, notas):
    alunos[nome] = (idade, notas)

# Função para exibir os dados de um aluno
def exibir_dados_aluno(nome):
    if nome in alunos:
        idade, notas = alunos[nome]
        print(f"\nNome: {nome}")
        print(f"Idade: {idade}")
        print(f"Notas: {notas}")
        print(f"Média: {sum(notas) / len(notas):.2f}")
    else:
        print(f"Aluno {nome} não encontrado.")

# Função para calcular e exibir a média de cada aluno
def media_de_cada_aluno():
    for nome, dados in alunos.items():
        idade, notas = dados
        print(f"\nAluno: {nome} | Idade: {idade} | Notas: {notas} | Média: {sum(notas) / len(notas):.2f}")

# Função principal para interagir com o usuário
def menu():
    while True:
        nome = input("Digite o nome do aluno: ")
        idade = int(input(f"Digite a idade de {nome}: "))
        notas = list(map(float, input(f"Digite as notas de {nome} (separadas por espaço): ").split()))
        
        adicionar_aluno(nome, idade, notas)
        
        continuar = input("Deseja adicionar outro aluno? (sim/não): ").strip().lower()
        if continuar != 'sim':
            break
    
    # Exibe as médias de cada aluno
    media_de_cada_aluno()

# Iniciar o programa
if __name__ == "__main__":
    menu()
