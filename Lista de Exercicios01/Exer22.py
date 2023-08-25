"""Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
Desconsiderando o valor 1000 da parada."""

num = []
while True:
    n1 = int(input("Digite um número: "))

    if n1 != 1000:
        num.append(n1)
    else:
        break

print(f"A soma foi {sum(num)}")