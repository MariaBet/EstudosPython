nome = 'Flavia Alexandra'
idade = 38
altura = 1.76
maior = idade > 18
data = True
data_atual = 2019
peso = 79

imc = peso / altura ** 2
print(nome, 'tem', idade, 'de idade e seu imc é: ', imc)
print(f' {nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')
print('{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome, idade, imc))
