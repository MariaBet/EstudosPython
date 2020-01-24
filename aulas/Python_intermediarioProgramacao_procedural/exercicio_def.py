
def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao("olá", "Maria")
print('\n')

def funcao(n1, n2, n3):
    print(n1 + n2 + n3)
funcao(8, 5, 3)
funcao(1, 2, 6)
print('\n')
def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)

ap = aumento_percentual(50, 10)
print(ap)
ap =aumento_percentual(100, 10)
print(ap)
ap = aumento_percentual(10, 10)
print(ap)
ap = aumento_percentual(15,100)
print(ap)

print('\n')

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 ==0:
        return f'fizz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n

from random import randint
for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
