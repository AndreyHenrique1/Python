"""Crie um programa que leia dois valores e mostre na tela um menu :
a. Somar
b. Multiplicar
c. Maior
d. Menor
e. Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
while True:
    escolha = int(input("\n1 - Somar"
                        "\n2 - Maior"
                        "\n3 - Menor"
                        "\n4 - Sair do programa"
                        "\nDigite um número de 1 á 4: "))

    if escolha == 1:
        print(f"A soma é {n1 + n2}")

    if escolha == 2:
        maior = n1
        menor = n2
        if maior < menor:
            maior = n2
            menor = n1
            print(f"O maior número é {maior}")
        else:
            print(f"O maior número é {maior}")

    if escolha == 3:
        maior = n1
        menor = n2
        if maior < menor:
            maior = n2
            menor = n1
            print(f"O menor número é {menor}")
        else:
            print(f"O menor número é {menor}")

    else:
        break

print("Programa Finalizado!!!")