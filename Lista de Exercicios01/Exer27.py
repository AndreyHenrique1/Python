# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

total = 1
n1 = int(input("Fatorial de: "))

for i in range(1, n1 + 1):
    total = total * i

print(total)