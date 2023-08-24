# Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
# tela dizendo se está “quente”, “frio” ou “agradável”

tem = float(input("Digite a temperatura atual: "))

if tem <= 18:
    print("O clima está frio")

elif (tem > 18) and (tem <= 30):
    print("O clima está agradavel")

else:
    print("O clima está quente")
    