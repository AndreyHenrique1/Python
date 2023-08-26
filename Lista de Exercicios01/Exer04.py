# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre
# ele.

a = input("Digite algo: ")

print(f"O seu tipo é: {type(a)}")
print(f"É uma letra: {a.isalpha()}")
print(f"É só espaço: {a.isspace()}")
print(f"É um alpha númerico: {a.isalnum()}")
print(f"Está em letras maiúsculas: {a.islower()}")
print(f"É uma palavra capitalizada: {a.istitle()}")
