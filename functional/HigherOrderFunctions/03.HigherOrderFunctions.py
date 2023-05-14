def filtrar(funcao, lista):
    return [elemento for elemento in lista if funcao(elemento)]

def filtrar_palavras_iniciadas_com_a(palavra):
    return palavra.startswith('a')

palavras = ['amigo', 'arroz', 'bola', 'abacaxi', 'casa']
palavras_iniciadas_com_a = filtrar(filtrar_palavras_iniciadas_com_a, palavras)
print(palavras_iniciadas_com_a)  # ['amigo', 'abacaxi']
