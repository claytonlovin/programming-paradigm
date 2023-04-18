from distutils import core


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Plim Plim")
    
    def parar(self):
        print("Parando...")
        print("Bicicleta Parando")

    def correr(self):
        print("Correndo... Vrummm....")

    def __str__(self):
        return f"""{self.__class__.__name__}: {', '.join([f'{chave}={valor}'
        for chave, valor in self.__dict__.items()])}"""

b1 = Bicicleta("Vermelha", "Caloi", 2022, 600, 18)

b2 = Bicicleta("Vermelha", "Caloi", 2022, 600, 18)
b2.parar()
print(b2)

#print(b1)

