
num = input("Digite um número inteiro: \n")

if not num.isdigit():
    print("Isso não é um número inteiro")
else:
    num = int(num)
    if not num % 2 == 0:
        print(f'{num} é ímpar')
    else:
        print(f'{num} é par')
print('\n')
print('\n')

hora = input('Digite um horario (0-23): ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print(" A hora deve ser ente 0 e 23")
    else:
        if hora <= 11:
            print("Bom dia!")
        elif hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite")

print('\n')
print('\n')
nome = input('Digite seu primeiro nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto!")
elif tamanho <= 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é muito grande!")
