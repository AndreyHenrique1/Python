"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido."""

while True:
    nota = float(input("Digite uma nota de 0 á 10: "))
    if nota < 0 or nota >= 11:
        print("Erro!!!"
              "\nSó é permitido nota de 0 á 10!!!")
    else:
        break

print("Programa finalizado com sucesso!!!")
