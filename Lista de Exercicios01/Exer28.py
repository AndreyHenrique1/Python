"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

pedro = []
joao = []
alisson = []

while True:
    escolha = int(input("1 - Pedro"
                        "\n2 - João"
                        "\n3 - Alisson"
                        "\n4 - Sair do programa"
                        "\nQual é o seu candidato? "))

    if escolha == 1:
        pedro.append(1)

    elif escolha == 2:
        joao.append(1)

    elif escolha == 3:
        alisson.append(1)

    else:
        break

print(f"\nPedro: {pedro.count(1)} votos "
      f"\nJoão: {joao.count(1)} votos"
      f"\nAlisson: {alisson.count(1)} votos")