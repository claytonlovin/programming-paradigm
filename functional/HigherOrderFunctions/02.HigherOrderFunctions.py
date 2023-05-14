def mapear(funcao, lista):
    return [funcao(elemento) for elemento in lista]

def formatar(nome):
    return nome.capitalize()

nomes = ['ana', 'pedro', 'maria', 'joão']

nomes_formatados = mapear(formatar, nomes)
print(nomes_formatados)
