def compor(funcoes):
    def composta(argumento):
        resultado = argumento
        for funcao in funcoes:
            resultado = funcao(resultado)
        return resultado
    return composta


def quadrado(x):
    return x * x

def incremento(x):
    return x + 1

def dobrar(x):
    return x * 2

f = compor([quadrado, incremento, dobrar])

resultado = f(5)

print(resultado) # 52
