"""Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = ((n1 + n2) + n3) / 2

if (media >= 6):
    print("Parabéns aluno aprovado!")
else:
    print("Aluno reprovado!")
