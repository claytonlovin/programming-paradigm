from datetime import datetime

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        
class Contato:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email

class Medico(Pessoa, Contato):
    def __init__(self, nome, data_nascimento, cpf, telefone, email, crm):
        Pessoa.__init__(self, nome, data_nascimento, cpf)
        Contato.__init__(self, telefone, email)
        self.crm = crm
        
    def __str__(self):
        return f'Nome: {self.nome} - CRM: {self.crm}'

class Paciente(Pessoa, Contato):
    def __init__(self, nome, data_nascimento, cpf, telefone, email, plano_saude):
        Pessoa.__init__(self, nome, data_nascimento, cpf)
        Contato.__init__(self, telefone, email)
        self.plano_saude = plano_saude
        
    def __str__(self):
        return f"""
        Nome: {self.nome} - 
        Data de Nascimento: {self.data_nascimento} - 
        Plano de Saúde: {self.plano_saude} - 
        Telefone: {self.telefone} - 
        E-mail: {self.email}
        """

class Medicamento:
    def __init__(self, nome, preco, fabricante, quantidade, modo_de_uso):
        self.nome = nome
        self.preco = preco
        self.fabricante = fabricante
        self.quantidade = quantidade
        self.modo_de_uso = modo_de_uso

    def __str__(self):
        return f"""
        Nome: {self.nome} - 
        Preço: {self.preco} - 
        Fabricante: {self.fabricante} - 
        Quantidade: {self.quantidade} - 
        Modo de Uso: {self.modo_de_uso}
        """
        
class Consulta:
    def __init__(self, medico, paciente, medicamento, data, data_retorno):
        self.medico = medico
        self.paciente = paciente
        self.medicamento = medicamento
        self.data = data
        self.data_retorno = data_retorno
        self.cancelada = False
        self.motivo_cancelamento = None

    def editar_consulta(self, medico=None, paciente=None, medicamento=None, data=None, data_retorno=None):
        if not self.cancelada and datetime.strptime(self.data_retorno, '%d/%m/%Y') >= datetime.now():
            if medico:
                self.medico = medico
            if paciente:
                self.paciente = paciente
            if medicamento:
                self.medicamento = medicamento
            if data:
                self.data = data
            if data_retorno:
                self.data_retorno = data_retorno
        else:
            print(f"Não é possível editar essa consulta pois ela já ocorreu em: {self.data_retorno}")
            
    def cancelar_consulta(self, motivo):
        if not self.cancelada and datetime.strptime(self.data_retorno, '%d/%m/%Y') >= datetime.now():
            self.cancelada = True
            self.motivo_cancelamento = motivo
        else:
            self.motivo_cancelamento = "Não é possível cancelar esta consulta."
            
    def __str__(self):
        return f"""
        Médico: {self.medico} - 
        Paciente: {self.paciente} - 
        Data da Consulta: {self.data} - 
        Data de Retorno: {self.data_retorno} - 
        Medicamentos: {self.medicamento}
        Cancelada: {self.cancelada} -
        Motivo do cancelamento: {self.motivo_cancelamento}
        """

#print(r.imprimir())
