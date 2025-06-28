while True:
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if senha != nome:
        print("Usuário e senha cadastrados com sucesso!")
        break
    else:
        print("Erro: a senha não pode ser igual ao nome de usuário. Tente novamente.\n")