from datetime import datetime
from heranca_multipla import Autenticavel, Pessoa, Sistema

class AutenticavelComRegistro(Autenticavel):
    @staticmethod
    def _get_data():
        return datetime.now().strftime('%d/%m/%Y %T')

    def autenticar(self, usuario, senha):
        print(f'{self._get_data()} Tentativa de acesso de {usuario}')
        acesso = super().autenticar(usuario, senha)
        if acesso:
            acesso_str = 'permitido'
        else:
            acesso_str = 'negado'
        print(f'{self._get_data()} Acesso de {usuario} {acesso_str}')
        return acesso


class PessoaAutenticavelComRegistro(AutenticavelComRegistro, Pessoa):
    ...


class SistemaAutenticavelComRegistro(AutenticavelComRegistro, Sistema):
    ...


p = PessoaAutenticavelComRegistro(
    nome='João', sobrenome='da Silva', idade=20,
    usuario='joao', senha='secreta',
)
p.autenticar('joao', 'secreta')
# Saída na tela:
# 23/04/2021 16:56:58 Tentativa de acesso de joao
# 23/04/2021 16:56:58 Acesso de joao permitido