

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar numero")
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)
    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)



print()




x = 0 # coluna

while x < 10:
    y = 0 # linha
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1

print('Acabou')
