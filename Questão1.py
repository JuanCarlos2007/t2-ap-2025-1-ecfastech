while True:
        nota = int(input("Digite uma nota entre zero e dez: "))
        if 0 <= nota <= 10:
            print("Nota válida")
            break
        else:
            print("A nota deve estar entre zero e dez.")