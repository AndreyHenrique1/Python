# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
# perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo
vitoria = []
from random import randint

while True:
    n1 = int(input("Digite um número: "))
    pc = randint(0, 10)
    total = n1 + pc
    op = input("Você quer ser Par ou Ímpar [P/I]? ")
    print(f"Você escolheu o número {n1} e o PC escolheu {pc}")
    op = op.upper()

    if (total % 2) == 0:
        if op == "P":
            print("Você ganhou!!!")
            vitoria.append(1)

        else:
            print("Você perdeu!!!")
            break

    if (total % 2) == 1:
        if op == "I":
            print("Você ganhou!!!")
            vitoria.append(1)
        else:
            print("Você perdeu!!!")
            break

print("Programa finalizado!!!")
print(f"Partidas ganhas: {vitoria.count(1)}")