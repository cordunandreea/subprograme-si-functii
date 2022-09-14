#functie care citeste o lista cu elemente de tip int
def lista_int():
    n=int(input('numarul de elemente din lista='))
    lista_locala=[]
    for i in range(n):
        e=input('elementul cu nr. '+str(i)+' este:')
        lista_locala.append(e)
    return lista_locala
lista_finala=lista_int()
print(lista_finala)