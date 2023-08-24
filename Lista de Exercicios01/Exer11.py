# Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
# trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
# ao final mostrar seu nome e salário final calculado.

nome = input("Digite seu nome: ")
horas = int(input("Digite o número de hora trabalhadas: "))
valor = float(input("Digite o valor da hora trabalhada: "))

sal_bruto = horas * valor
inss = sal_bruto - (sal_bruto * 0.02)

print(f"O {nome} tem como salário final R${inss}")