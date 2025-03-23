import os

mensagens = []

nome = input("Nome: ")

while True:

    #limpando terminal
    os.system('cls')

    if len(mensagens) > 0:

        for m in mensagens: 
            print(m['nome'], "-", m['texto'])
    
    print("________________")

    # obtendo texto
    texto = str.lower(input("mensagem: "))
    if texto == "fim":
        break

    # str.lower - converter tu que for escrito em letra minúscula assim como str.upper que vai tudo para maiúscula

    # adicionando mensagem na lista
    mensagens.append({"nome": nome,
        "texto": texto})
    