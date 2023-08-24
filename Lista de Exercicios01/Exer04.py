# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre
# ele.

a = input("Digite algo: ")

print(type(a))
print(a.isdigit())
print(a.isalnum())
print(a.isalpha())
print(a.islower())
print(a.isspace())
print(a.isupper())