# Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.

lista = ["Andrey", "Henrique", "João", "Teste02", "Teste01"]

procurar = input("Digite algo que pode estar na lista: ")

if procurar in lista:
    print(f"O item {procurar} está na lista")
    print(f"O item {procurar} está na posição {lista.index(procurar)}")
else:
    print(f"O item {procurar} não está na lista")




