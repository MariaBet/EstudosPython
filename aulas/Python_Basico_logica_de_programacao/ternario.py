
logged_user = True

if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuario precisa logar'
print(msg)

logged_user = True
msg = 'Usuário Logado' if logged_user else 'Usuario precisa logar'
print(msg)
print()

idade = 18
if idade >= 18:
    print('Pode acessar')
else:
    print('Não pode acessar')
print()
idade = input('Qual a sua idade:  ?')
if not idade.isnumeric():
    print("somente numeros")
else:
    idade = int(idade)
    e_de_maior = (idade>= 18)
    msg ='Pode acessar'if e_de_maior else 'Não pode acessar'
    print(msg)
