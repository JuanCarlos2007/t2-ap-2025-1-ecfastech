populacao_a = int(input("Digite o número de Habitantes_A: "))
populacao_b = int(input("Digite o número de Habitantes_B: "))
taxa_a = float(input("Digite a taxa_A de crecimento populacional em decimal: "))
taxa_b = float(input("Digite a taxa_B de crecimento populacional em decimal: ")) 
anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

    if populacao_a == populacao_b:
        print(f"Serão necessários {anos} anos para que a população do país A iguale a do país B.")
        break

    else:
        print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a do país B.")
