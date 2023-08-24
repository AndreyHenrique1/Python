# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
# de aumento.

v1 = float(input("Digite o preço do produto: "))

print(f"O seu preço com 15% de aumento é de {v1 * 1.15}"
      f"\nO seu preço com 5% de aumento é de {v1 - (v1 * 0.05)}")

