#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('dados.csv')
print(df.loc[160:179,'Funcionário': 'Mês'])
