from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor("Rick Riodan")
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()
