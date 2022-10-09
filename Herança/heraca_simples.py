class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        print('Ligando o veículo...')

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def carregado(self):
        print('Caminhão carregado')

class Motocicleta(Veiculo):
    pass


moto = Motocicleta("Honda", "CG 150", 2018)
print(moto)
moto.ligar()


carro = Carro("Volkswagen", "Gol", 2018)
carro.ligar()

caminhao = Caminhao("Mercedes-Benz", "Actros", 2018)
caminhao.ligar()
caminhao.carregado()