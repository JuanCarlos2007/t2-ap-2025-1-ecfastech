def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    with open("notas.txt", "a") as arq:
        arq.write(f"Nome:{nome},Nota1:{nota1},Nota2:{nota2},Nota3:{nota3}\n")

def calcular_medias():
    try:
        with open("notas.txt", "r") as arq:
            linhas = arq.readlines()
    except FileNotFoundError:
        print("Arquivo não encontrado.\n")
        return

    for linha in linhas:
        partes = linha.strip().split(",")
        nome = partes[0].split(":")[1].strip()
        n1 = float(partes[1].split(":")[1])
        n2 = float(partes[2].split(":")[1])
        n3 = float(partes[3].split(":")[1])
        media = (n1 + n2 + n3) / 3

        if media >= 7:
            with open("aprovados.txt", "a") as a:
                a.write(f"Nome:{nome},Média:{media:.2f},Situação:Aprovado\n")
        elif media >= 5:
            with open("exame.txt", "a") as e:
                e.write(f"Nome:{nome},Média:{media:.2f},Situação: De Exame\n")
        else:
            with open("reprovados.txt", "a") as r:
                r.write(f"Nome:{nome},Média:{media:.2f},Situação:Reprovado\n")

def processar_exame():
    try:
        with open("exame.txt", "r") as arq:
            linhas = arq.readlines()
    except FileNotFoundError:
        print("Nenhum aluno em exame.\n")
        return

    for linha in linhas:
        partes = linha.strip().split(",")
        nome = partes[0].split(":")[1].strip()
        media_anterior = float(partes[1].split(":")[1])
        nota_exame = float(input(f"Digite a nota do exame para {nome}: "))
        media_final = (media_anterior + nota_exame) / 2

        if media_final >= 5:
            with open("aprovados.txt", "a") as a:
                a.write(f"Nome:{nome},Média Final:{media_final:.2f},Situação:Aprovado pós exame\n")
        else:
            with open("reprovados.txt", "a") as r:
                r.write(f"Nome:{nome},Média Final:{media_final:.2f},Situação:Reprovado pós exame\n")

def exibir_resultados():
    def mostrar(arquivo, titulo):
        print(f"\n--- {titulo} ---")
        try:
            with open(arquivo, "r") as arq:
                linhas = arq.readlines()
                if linhas:
                    for linha in linhas:
                        print(linha.strip())
                else:
                    print("Nenhum registro encontrado.")
        except FileNotFoundError:
            print(f"Arquivo {arquivo} não encontrado.")

    mostrar("aprovados.txt", "Aprovados")
    mostrar("reprovados.txt", "Reprovados")
    print()

while True:
    print("1 - Cadastrar aluno")
    print("2 - Calcular médias e classificar")
    print("3 - Processar exame")
    print("4 - Exibir resultados")
    print("0 - Sair")

    opc = input("Escolha uma opção: ")

    if opc == "1":
        cadastrar_aluno()
    elif opc == "2":
        calcular_medias()
    elif opc == "3":
        processar_exame()
    elif opc == "4":
        exibir_resultados()
    elif opc == "0":
        print("Fechando o sistema.")
        break
    else:
        print("Opção inválida, tente novamente.\n")
