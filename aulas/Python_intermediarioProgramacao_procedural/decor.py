'''
# Funções como variáveis
def fala_oi():
    print('Oi')


# A variável é igual a função
variavel = fala_oi
print(type(variavel))  # function
variavel()  # Oi
'''

'''
# Uma função dentro de outra
def master():
    # Função interna
    def slave():
        print('Oi')
    # Função a ser executada
    return slave

# Variável recebe função
variavel = master()
# Executa a função interna de master
variavel()
'''

'''
# Função como parâmetro
def master(funcao):
    # Função interna
    def slave():
        # executa a função enviada
        funcao()
    # Retorna a função interna sem executar
    return slave

# Uma função qualquer
def fala_oi():
    print('Oi')

# Variável como função
variavel = master(fala_oi)
# Executa a variável/função
variavel()
'''

'''
# Recebe uma função
def master(funcao):
    # Cria uma função interna
    def slave():
        # Decora
        print('Estou decorada.')
        # Executa a função enviada
        funcao()
    # Retorna a função interna sem executar
    return slave

# Uma função qualquer
def fala_oi():
    print('Oi')

# Decorando
fala_oi = master(fala_oi)
fala_oi()
'''

'''
# Função decoradora
def master(funcao):
    def slave():
        print('Estou decorada.')
        funcao()
    return slave

# Sintax sugar do decorador
@master
def fala_oi():
    print('Oi')

fala_oi()
'''

'''
# Decorando com parâmetros
def master(funcao):
    def slave(*args, **kwargs):
        print('Estou decorada.')
        funcao(*args, **kwargs)
    return slave

@master
def fala_oi(msg):
    print(msg)


fala_oi('Olá, sou Luiz')
'''

from time import time
from time import sleep


def velocidade(funcao):
    """
    Função decoradora: Verifica o tempo que uma função leva para executar
    """
    def envolve(*args, **kwargs):
        """ Função que envolve e executa outra função """
        # Tempo inicial
        start = time()
        # Executa a função
        resultado = funcao(*args, **kwargs)
        # Tempo final
        end = time()
        # Resultado de tempo em ms
        tempo = (end - start) * 1000
        # Mostra o tempo
        print(f'\nA função levou {tempo:.2f}ms para ser executada.')
        # Retorna a função original executada
        return resultado
    # Retorna a função que envolve
    return envolve


@velocidade
def demora(qtd):
    """ Função decorada """
    for i in range(qtd):
        print(i, end='')


# Executa a função decorada
demora(10000)
