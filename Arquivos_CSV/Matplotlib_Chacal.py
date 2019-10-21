#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Biblioteca é a matplotlib.
# utilizar ela para criar, plotar, gráficos.
# Então, falamos para o Python importar (import) da biblioteca
# matplotlib a parte de plotar gráficos com o Python (pyplot).
import matplotlib.pyplot

# Vamos criar um gráfico com a nossa planilha de vendas semestrais.
# Para isso, precisamos falar para o pyplot quais são os meses e
# quais são os valores de cada mês. Uma maneira de fazer isso é
# criar duas listas, uma com os meses e outra com os valores:
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

# Agora, basta falar para o pyplot plotar (plot) o gráfico
matplotlib.pyplot.plot(meses, valores)

#Adicionando titulo e label p/ os eixos X e Y
matplotlib.pyplot.title('Faturamento no primeiro semestre de 2017')
matplotlib.pyplot.xlabel('Meses')
matplotlib.pyplot.ylabel('Faturamento em R$')

# O pyplot criou o gráfico, mas onde ele está?
# O gráfico não apareceu. Quando falamos para o pyplot criar
# o gráfico, ele constrói o gráfico e o guarda em uma região da memória.
# Para conseguir ver o gráfico, precisamos falar para o
# pyplot mostrá-lo (show()):
matplotlib.pyplot.show()
