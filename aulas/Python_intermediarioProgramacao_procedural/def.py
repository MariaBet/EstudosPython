


def saudacao(msg = 'ola', nome = 'usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'
variavel = saudacao()

print(variavel)
print('\n')

def funcao(var):
    return(var)
    print("não vai executar")

variavel= funcao('valor que eu quero')
if variavel:
    print(variavel)
else:
    print('nenhum valor')


print('\n')

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

divide = divisao(8, 4)

if divide:
    print(divide)
else:
    print('conta invalida')


print('\n')

def dumb():
    return [1, 2, 3 ,4, 5]
var = dumb()
print(dumb(), type(var))
