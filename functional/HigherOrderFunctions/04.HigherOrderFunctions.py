def reduzir(funcao, lista, valor_inicial):
    resultado = valor_inicial
    for elemento in lista:
        resultado = funcao(resultado, elemento)
    return resultado


def somar(a, b):
    return a + b

numeros = [1, 2, 3, 4, 5]
resultado = reduzir(somar, numeros, 0)
print(resultado)  # saída: 15
