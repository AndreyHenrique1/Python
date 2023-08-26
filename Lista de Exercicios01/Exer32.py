"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
a. Código da cidade; (digitado pelo usuário)
b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
Deseja-se saber:
b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
c. Qual a média de veículos nas cinco cidades juntas;
d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio"""

total = total3 = total4 = cod = cod2 = total2 = 0
maior = 0
menor = 0
for i in range(5):
    codigo = input("Código da cidade: ")
    veiculos = int(input("Número de veículos de passeio (em 1999): "))
    acidentes = int(input("Número de acidentes de trânsito com vítimas (em 1999): "))

    total += veiculos
    total2 = total / 5
    total3 += acidentes

    if acidentes > maior:
        maior = acidentes
        cod = codigo

    elif maior > menor:
        menor = acidentes
        cod2 = codigo

    if veiculos < 2000:
        total4 = total3 / 5


print(f"\nO maior indice de acidentes de transito foi {maior} e codigo da cidade é:  {cod}"
      f"\nO menor indice de acidenstes de transito foi {menor} e codigo da cidade é: {cod2}"
      f"\nMédia de veiculos nas cincos cidades: {total2}"
      f"\nMédia de acidentes de transitos nas cidades com menos de 2000: {total4}")

