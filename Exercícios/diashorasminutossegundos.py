#!/usr/bin/python3
# -*- coding: utf-8 -*-


print('=====Calculo, dia, hora, minutos e segundos=====''\n')
d = int(input("Digite quantos dias: "))
h = int(input("Digite quantas horas: "))
m = int(input("Digite quantos minutos: "))

seg = (d * 60) + (h * 3600) + (m * 86400)

print(seg)
