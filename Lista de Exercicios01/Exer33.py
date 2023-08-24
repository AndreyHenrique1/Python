"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero"""

jose = []
joao = []
pedro = []
ana = []
nulo = []
branco = []
quantidade = []

r = "S"
while r == "S" or "s":
    escolha = int(input("1 - José"
                        "\n2 - João"
                        "\n3 - Pedro"
                        "\n4 - Ana"
                        "\n5 - Nulo"
                        "\n6 - Branco"
                        "\nDigite um número: "))

    if escolha == 1:
        jose.append(0)

    elif escolha == 2:
        joao.append(0)

    elif escolha == 3:
        pedro.append(0)

    elif escolha == 4:
        ana.append(0)

    elif escolha == 5:
        nulo.append(0)

    elif escolha == 6:
        branco.append(0)

    r = input("Você deseja continuar [S/N]: ")
    if r == "S" or r == "s":
        quantidade.append(0)
    else:
        break

total_voto = quantidade.count(0)
total_joao = joao.count(0)
total_jose = jose.count(0)
total_pedro = pedro.count(0)
total_ana = ana.count(0)
total_nulo = nulo.count(0)
total_branco = branco.count(0)

print(f"\nQuantidade de votos do José: {total_jose}"
      f"\nQuantidade de votos do João: {total_joao}"
      f"\nQuantidade de votos do Pedro: {total_pedro}"
      f"\nquantidade de votos da Ana: {total_ana}"
      f"\nQuantidade de votos Nulos: {total_nulo}"
      f"\nQuantidade de votos Brancos: {total_branco}"
      f"\nA porcentagem de votos nulos sobre o total de votos é: "
      f"\nA porcentagem de votos nulos sobre o total de votos é: ")

