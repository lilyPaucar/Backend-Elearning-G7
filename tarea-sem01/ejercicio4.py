n=int(input('Ingrese un numero: '))

while n!=1:
    if n%2==0:
        n=n/2
    elif n%2!=0:
        n=n*3+1
    print (int(n), end=" ")