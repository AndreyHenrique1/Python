# Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
# mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
# Euros.

nome = input("Digite seu nome: ")
d = float(input("Digite um valor em R$: "))
print(f"O valor em Euro é {d / 5.27} "
      f"\nO valor em dólar {d / 4.87}")

