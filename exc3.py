def conta_vogais(frase):

    frase= frase.lower()
    quantidade =frase.count('a')
    quantidade += frase.count('e')
    quantidade += frase.count('i')
    quantidade += frase.count('o')
    quantidade += frase.count('u')
    return quantidade

frase = input('digite uma frase: ')
print (f'quantidade de vogais: { conta_vogais(frase)}')

