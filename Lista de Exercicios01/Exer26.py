"""Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres)"""

nome = input("Digite seu nome: ")

while len(nome) <= 3:
    print("O nome tem que ser maior que 3 caracteres!!!")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

while idade <= 0 or idade >= 150:
    print("A idade não pode ser maior que 150 e não pode ser menor que 0!!!")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))

while salario < 0:
    print("O salário deve ser maior que 0!!!")
    salario = float(input("Digite seu salário: "))

sexo = input("Digite seu sexo [M/F]: ")
sexo = sexo.lower()

while sexo != "m" and sexo != "f":
        print("Só é permitido M e F !!!")
        sexo = input("Digite seu sexo [M/F]: ")

estadociv = input("Digite seu Estado Civil [S / C / V / D]: ")
estadociv = estadociv.lower()

while estadociv != "s" and estadociv != "c" and estadociv != "v" and estadociv != "d":
    print("Só é permitido [S / C / V / D]")
    estadociv = input("Digite seu Estado Civil [S / C / V / D]: ")

print("Programa Finalizado com sucesso!!!")