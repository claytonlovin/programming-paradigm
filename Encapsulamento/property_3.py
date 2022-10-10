class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self._nome = nome
        self.sobrenome = sobrenome
        self._idade = idade
    
    @property
    def nome (self):
        return self._nome
    
    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        valor = valor.split(' ', 1)
        self._nome = valor[0]
        self.sobrenome = valor[1]
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError('Idade não pode ser negativa')
        self._idade = valor
    
    def fazer_aniversario(self):
        self.idade += 1

p1 = Pessoa('Luiz', 'Otávio', 32)
p1.nome_completo = 'João da Silva'
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)

# Saída ValueError: Idade não pode ser negativa
p2 = Pessoa('Maria', 'Silva', 25)
p2.idade = -10
print(p2.idade)