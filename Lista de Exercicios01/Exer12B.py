"""Faça 4 listas:
A. Filmes
B. Jogos
C. Livros
D. Esporte
a. Adicione no mínimo 2 itens em cada lista.
b. Crie uma lista das 4 listas criadas acima.
c. Acesse (mostrar) algum item da lista livros.
d. Remova um item da lista esporte."""

filme = []
jogos = []
livros = []
esporte = []

filme.append("Homem-Aranha")
filme.append("Super Mario")

jogos.append("Uncharted")
jogos.append("Gears 5")

livros.append("Harry Potter")
livros.append("Turma da Mônica")

esporte.append("Futebol")
esporte.append("Basquete")

lista = filme + jogos + livros + esporte
print(f"Lista completa: {lista}")
print(f"Os item da lista livros são {livros}")
lista.remove("Basquete")
print(f"Lista sem um item da lista esporte {lista}")



