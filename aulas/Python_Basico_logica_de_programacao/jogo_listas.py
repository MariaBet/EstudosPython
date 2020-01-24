#!/usr/bin/python3
# -*- coding: utf-8 -*-

secreto = "computador"
digitadas = []
chances = 15

print("Dica é uma aparelho eletrônico")
print("=================================")

while True:
    if chances < 0:
        print('Você perdeu!!!!')
    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Boa!!! "{letra}" existe na palavra secreta \n')
    else:
        print(f'Não deu certo "{letra}" não existe na palavra secreta')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    if secreto_temp == secreto:
        print('Você Acertou! Parabéns......!!!')
        break
    else:
        print(f'A palavra secreta é: {secreto_temp}')
    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances')
    print()
