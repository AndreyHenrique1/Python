"""Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a escrever valores."""

num = []
quan = []

while True:
    n1 = int(input("Digite um número: "))
    num.append(n1)
    quan.append(1)
    r = input("Deseja continuar? [S/N] ")
    if r == "N" or r == "n":
        break


qua = quan.count(1)

print(f"A media dos valores é {sum(num) / qua}"
      f"\nO menor valor é {min(num)}"
      f"\nO maior valor é {max(num)}")
