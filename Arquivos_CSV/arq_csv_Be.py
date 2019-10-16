#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas

df = pandas.read_csv('dados.csv')
print(df.loc[176:200,'Funcionário': 'Mês'])
