
class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class PessoaAutenticavel(Pessoa):
    def __init__(self, nome, sobrenome, idade, usuario, senha):
        Pessoa.__init__(self, nome, sobrenome, idade)
        self.usuario = usuario
        self.senha = senha

    def autenticar(self, usuario, senha):
        return self.usuario == usuario and self.senha == senha


p = PessoaAutenticavel('João', 'da Silva', 20, 'joao', 'secreta')

print(Pessoa.nome_completo(p))
print(PessoaAutenticavel.autenticar(p, 'joao', 'secreta'))

#
class Autenticavel:
    def __init__(self, *args, usuario, senha, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario
        self.senha = senha

    def autenticar(self, usuario, senha):
        return self.usuario == usuario and self.senha == senha

# SISTEMA DE HERANÇA MULTIPLA
class Sistema:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def autenticar(self, usuario, senha):
        if self.usuario == usuario and self.senha == senha:
            return True
        else:
            return False

