#!/usr/bin/python3
# -*- coding: utf-8 -*-


print('======================temperatura==================')

c = float(input("Digite a temperatura em Celsius: "))

f =  9 * c / 5 + 32

print("Temperatura: Fahrenheit = ", f)

print('\n')


f = float(input("Digite a temperatura em Fahrenheit: "))

c = (f - 32) * 5 / 9

print("Temperatura: Celsius = ", c)
