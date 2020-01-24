# split dividir uma str
# join juntar uma lista
# enumerate enumerar elementos de uma lista

string = "O Brasil é um país do futebol, O brasil é Penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')
palavra = ''
contagem = 0

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase')
    qtd_vezes = lista_1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que aparece mais vezes é {palavra} ({contagem}x)')
print(lista_2)
# strip remove espaços no inicio e fim do print

print()
print("join")

string = "O  brasil é Penta"
lista = string.split(' ')
string_2 = ' '.join(lista)
print(string)
print(lista)
print(string_2)

print('\n')
print("enumeração")

string = "O brasil é Penta"
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)
print('\n')

lista = ['Luiz','Maria','João']

for indice, nome in enumerate(lista):
    print(indice, nome)
