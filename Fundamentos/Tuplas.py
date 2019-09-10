#!/usr/bin/python
# -*- coding: utf-8 -*-

# Tupla serve p/ vc criar dados imutaveis
# Pois uma tupla diferente da lista vc não consegue manipular.
# Exemplo ... vc precisa criar uma lista com dias da semana
# ou meses do ano, só um exemplo.
# Você pode usar lista, porem tupla é mais indicado pq dias
# e meses não mudam. Uma tupla não muda tmb.



# tuplas bem parecido com listas, porem é ultizado com parenteses
computador=('mouse','teclado','cpu','monitor','impressora','caixa de som')
print (computador[2:5])  #leitura em intervalos- 3, 4 e 5º item


modelo = ('Dell', 'Samsung', 'Itautec', 'Lenovo', 'Positivo')
for fabricante in modelo:     # percorrer itens na tupla
  print(fabricante)
