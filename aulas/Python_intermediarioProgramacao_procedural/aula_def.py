variavel = 'valor'
def func():
    print(variavel)


def func2(arg = None):
    arg = arg.replace('v', 'c') # trocar o v pelo c ficara calor
    return arg

func()
outra_variavel = func2(arg = variavel)

print(outra_variavel)
# escopo local e escopo fora alterando variaveis globais dentro da função porem não recomendavel
print()
