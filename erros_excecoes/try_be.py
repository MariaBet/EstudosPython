#!/usr/bin/python
# -*- coding: utf-8 -*-


'''try - bloco permite testar um bloco do código quanto a erros
except bloco permite lidar com o erro
finally executar o código independente do resultado do try e Exception'''


try:
    print(n)
except:
    print("exceção" '\n')



try:
    print(b)
except:
    print("Algo deu errado e agora?" '\n')
finally:
    print("programa finalizado" '\n')
print('\n')




c = "chacal"
if not type(c) is int:
    raise TypeError("somente numeros interios")

'''sem o try e o Exception o codigo gerará um erro'''
print(n)
