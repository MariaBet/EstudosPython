"""
Exemplo de classe e objeto.
Criado para rapidinha #7: https://youtu.be/SQXmC6PbZWk
"""


class Personagem:
    """Molde para o rato."""
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def __repr__(self):
        return f'Personagem("{self.nome}", "{self.cor}")'


mickey = Personagem('Mickey', 'Preto')
pluto = Personagem('Pluto', 'Laranja')
pateta = Personagem('Pateta', 'Preto')
