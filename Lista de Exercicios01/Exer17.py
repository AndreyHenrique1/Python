"""Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 ∗ h) − 58
• Mulheres: (62, 1 ∗ h) − 44, 7"""

h = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo [M/F]: ")

if sexo == "M" or sexo == "m":
    print(f"O seu peso ideal é de {(72.7 * h) - 58} Kg")

elif sexo == "F" or sexo == "f":
    print(f"O seu peso ideal é de {(62.1 * h) - 44.7} Kg")
