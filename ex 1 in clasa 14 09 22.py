#se calculeaza valoarea unei expresii prin functia putere 
def functia_putere(a,b):
    putere=a**b
    return putere
S=1+functia_putere(0.5,2)+functia_putere(0.5,4)+functia_putere(0.5,6)+functia_putere(0.5,8)
print('valoarea expresiei S=',S)