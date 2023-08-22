def preenche_lista():
    lista=[]
    for i in range(10):
        numero= int(input('numero: '))
        lista.append(numero)
        print(lista)

    maior= max(lista)
    menor=min(lista)
    media=sum(lista)/ len(lista)

    return maior, menor ,media  #retorna uma tupla 

resultado= preenche_lista()
print(resultado)
print(f'maior: {resultado[0]}') #primeira posição da tupla
print(f'menor: {resultado[1]}') #segunda posição da tupla 
print(f'media: {resultado[2]}') #terceira posição da tupla 
