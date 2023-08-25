"""Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
a. Soma de 2 n´umeros.
b. Diferença entre 2 números (maior pelo menor).
c.Produto entre 2 números.
d. Divisão entre 2 números (o denominador não pode ser zero)."""

maior = 0
menor = 0

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

while True:
    escolha = int(input("1 - Soma de dois números"
                        "\n2 - Diferença entre 2 números (maior pelo menor)"
                        "\n3 - Produto entre 2 números"
                        "\n4 - Divisão entre 2 números (o denominador não pode ser zero)"
                        "\n5 - Sair do Programa"
                        "\nDigite um número de 1 á 4: "))

    if escolha == 1:
        print(f"A soma dos dois números é {n1 + n2}")

    elif escolha == 2:
        maior = n1
        menor = n2
        if maior < menor:
            maior = n2
            menor = n1
            print(f"A diferença dos dois números é {maior - menor}")
        else:
            print(f"A diferença dos dois números é {maior - menor}")

    elif escolha == 3:
        print(f"O produto dos dois números é {n1 * n2}")

    elif escolha == 4:
        if n2 == 0:
            print("O denominador não pode ser zero!!!")
        else:
            print(f"A divisão dos dois números é {n1 / n2}")

    elif escolha == 5:
        break

    else:
        print("Erro!!!"
              "\nVocê não escolheu um número de 1 á 4")

print("Programa Finalizado!!!")