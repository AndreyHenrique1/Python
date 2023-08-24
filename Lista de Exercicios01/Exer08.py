# Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
# quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input("Digite a largura da sua parede em metros: "))
a = float(input("Digite a altura da sua parede em metros: "))

total = l * a
print(f"A sua área é de {total} metros quadrados e a quantidade de litros de tinta é {total / 2}L")