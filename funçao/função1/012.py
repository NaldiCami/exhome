def ordenar_list(lista):
    for i in range(len(lista)):
        for j in range(i +1, len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j], = lista[j], lista[i]
    return lista

lista = [5,2,9,1,7]
lista_ordem = ordenar_list(lista)
print('a lista ordenada é:', lista_ordem)