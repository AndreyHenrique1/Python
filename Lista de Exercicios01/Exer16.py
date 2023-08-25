"""Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
conversão."""

escolha = input("Digite F para converter Fahrenheit para Celsius ou digite C para converter Celsius para Fahrenheit: ")

if escolha == "f" or escolha == "F":
    fah = int(input("Digite a temperatura em Fahrenheit: "))
    print(f"A temperatura em graus celsius é {(fah - 32) / 1.8}")

else:
    cel = int(input("Digite a temperatura em graus celsius: "))
    print(f"A temperatura em Fahrenheit é {(cel * 9/5) + 32}")

