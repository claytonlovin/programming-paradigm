
class Medico:
    def __init__(self, nome, crm):
        self.nome = nome
        self.crm = crm
    
    def receitar(self):
        return  self.nome, self.crm



class Paciente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def consultar(self):
        return self.nome, self.cpf



class Medicamento:
    def __init__(self, nome):
        self.nome = nome

        return self.nome


class Receita:
    def __init__(self, Medico, Paciente, Medicamento, receita):
        self.Medico = Medico.nome
        self.MedicoCRM = Medico.crm
        self.Paciente = Paciente.nome
        self.PacienteCPF = Paciente.cpf
        self.Medicamento = Medicamento
        self.receita = receita

    def imprimir(self):
       return f"""{
                    "Nome Médico:", self.Medico, 
                    "CRM:", self.MedicoCRM, 
                    "Nome Paciente:", self.Paciente,
                    "Nome Medicamento:", self.Medicamento,
                    "Receita:", self.receita}"""
    
   
p = Paciente("João", "123.456.789-00")
m = Medico("Maria", "123456")

r = Receita(m, p, "Dipirona", "Tomar 1 comprimido 3x ao dia")

print(r.imprimir())
