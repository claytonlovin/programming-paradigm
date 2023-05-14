# uma função usuario, usuario recebe uma função saldo, temos mais uma função transferir saldo para a outra conta.
Saldo = 500
Valor_a_trasferir = 300

def realizar_transferencia(destino, transferir):
    if destino and transferir:
        print('Conta verificada! Realizando transferência')
        print(f'Valor trasferido:: R$ {transferir[1]},00 para a Conta:: {destino[1]} Agência:: {destino[2]} Banco:: {destino[3]}')
        print(f'Seu saldo agora é de R$ {transferir[2]}') 
    else:
        print(f'Seu saldo é insuficiente... Por favor verificar e tentar novamente')

def conta_destino(conta, agencia, banco):
    if len(conta) == 7 and len(agencia) == 4 and len(banco) == 3:
        return (True, conta, agencia, banco)
    else:
        return False


def saldo_transferir(valor, origem):
    if  origem  >=  valor:
        origem  -=  valor
        return (True, valor, origem)
    else:
        return False


T1 = conta_destino('0000000', '0000', '000') # 6 5 3

T2 = saldo_transferir(Valor_a_trasferir, Saldo)

T3 = realizar_transferencia(T1, T2)

