"""Leia a idade e o tempo de servic¸o de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos"""

idade = int(input("Digite sua idade: "))
tempo = int(input("Quantos anos você tem de tempo de serviço? "))

if idade >= 65:
    print("Você está aposentado!!!")

elif tempo >= 30:
    print("Você está aposentado!!!")

elif idade >= 60 and tempo >= 25:
    print("Você está aposentado!!!")
else:
    print("Você não está aposentado!!!")
    