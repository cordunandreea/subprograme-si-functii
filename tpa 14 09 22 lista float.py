#functie care citeste o lista cu elemente de tip float
def lista_float():
    x=float(input('numarul de elemente din lista='))
    lista_float_locala=[]
    for i in range(int(x)):
        e=input('elementul cu nr. '+str(i)+' este:')
        lista_float_locala.append(e)
    return lista_float_locala
lista_finala=lista_float()
print(lista_finala)