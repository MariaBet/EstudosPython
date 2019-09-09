#!/usr/bin/python
# -*- coding: utf-8 -*-
# digite uma sequencia de numeros interios e o 0 para terminar este programa
# exemplo 9 10 32 56 -9 -8 1 0

def main():
    num = int(input("Digite um numero inteiro e o [0 para terminar]: "))
    soma = 0

    while num  != 0:
        soma = soma + num
        num = int(input("Digite um numero inteiro e o [0 para terminar]: "))
    print("A soma foi: ", soma)

main()
