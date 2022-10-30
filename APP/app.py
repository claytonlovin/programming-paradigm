from main import Medicamento, Medico, Paciente, Consulta

Paciente = Paciente('João', '01/01/2000', '123.456.789-00', '11 99999-9999', 'claytoncsj@gmail.com', 'Unimed')
   
Medico = Medico('Clayton', '01/01/2000', '123.456.789-00', '11 99999-9999', 'medico@medico.com', '123456')

Medicamento = Medicamento('Dipirona', 'R$ 10,00', 'Bayer', '1', 'Tomar 1 comprimido a cada 8 horas')

Consulta = Consulta(Medico, Paciente, Medicamento, '01/01/2020', '11/01/2023')

print(Consulta)