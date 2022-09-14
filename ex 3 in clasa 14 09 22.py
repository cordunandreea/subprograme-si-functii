#suma si inmultirea a 2 fractii
a1=int(input('Dati un numarator pentru prima fractie a1='))
b1=int(input('Dati un numitor pentru prima fractie b1='))
a2=int(input('Dati un numarator pentru a doua fractie a2='))
b2=int(input('Dati un numitor pentru a doua fractie b2='))
def f_fractie1(a1,b1):
    return a1/b1
def f_fractie2(a2,b2):
    return a2/b2
suma=f_fractie1(a1,b1)+f_fractie2(a2,b2)
inmultirea=f_fractie1(a1,b1)*f_fractie2(a2,b2)
print('Suma fractiilor este=',suma)
print('Inmultirea fractiilor este=',inmultirea)