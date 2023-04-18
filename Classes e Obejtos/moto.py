

class Moto:
    def __init__(self, modelo:str, ano:int, cor:str, fabricante:str):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.fabricante = fabricante
        
    def __str__(self):
        return f"""{self.__class__.__name__}: {', '.join([f'{chave} = {valor}'
        for chave, valor in self.__dict__.items()])}"""
    
m1 = Moto('MT', 2022, 'Preto', 'yamaha')

print(m1)

