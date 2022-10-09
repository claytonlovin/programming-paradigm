# __init__ metodo especial, construtor, meotodo incializador

from functools import cache
from pickle import TRUE


class Cachorro():
    def __init__(self, nome, cor, acordado=TRUE):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("UAUAUA")


def criar_cachorro():
    c = Cachorro("Zeus", "Preto e branco", False)
    print(c.nome, c.cor, c.acordado)

criar_cachorro()


