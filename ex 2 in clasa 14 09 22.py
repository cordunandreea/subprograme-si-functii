#calcularea factorialului
n=int(input('Dati o valoare lui n='))
m=int(input('Dati o valoare lui m='))
def f_factorial(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
if n<m:
    print('nr n trebuie sa fie mai mare ca nr m, factorialul admite doar numere naturale intregi')
else:
    C=f_factorial(n)/f_factorial(m)*f_factorial(n-m)
    print('C=',C)