def realizar_transferencia(destino, transferir):
    if destino and transferir:
        conta, agencia, banco = destino
        valor_transferido, novo_saldo = transferir
        mensagem = f'Valor transferido: R$ {valor_transferido},00 para a Conta: {conta} Agência: {agencia} Banco: {banco}'
        return (mensagem, novo_saldo)
    else:
        return None


def conta_destino(conta, agencia, banco):
    if len(conta) == 7 and len(agencia) == 4 and len(banco) == 3:
        return (conta, agencia, banco)
    else:
        return None


def saldo_transferir(valor, origem):
    if origem >= valor:
        novo_saldo = origem - valor
        return (valor, novo_saldo)
    else:
        return None


def transferencia_realizada(resultado_transferencia):
    if resultado_transferencia:
        mensagem, saldo = resultado_transferencia
        print(mensagem)
        print(f'Seu saldo agora é de R$ {saldo}')
    else:
        mensagem = 'Dados de transferência incorretos!! Por faovr verificar'
        print(mensagem)


saldo = 500
valor_a_transferir = 300

conta_destino = conta_destino('0000000', '0000', '000')
saldo_transferir = saldo_transferir(valor_a_transferir, saldo)
resultado_transferencia = realizar_transferencia(conta_destino, saldo_transferir)
transferencia_realizada(resultado_transferencia)
