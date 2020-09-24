#Gabriela Celeste Tarqui Quintanilla
a=int(input("Ingrese un número: "))
b=int(input("Ingrese un número: "))
c=0
d=0
e=0
aux=0
if(a==b):
    print("Los números son iguales")
else:
    if(a<=0 and b<=0):
        "Ambos números son negativos o cero, por lo tanto no existe una sucesión de números naturales entre ellos"
    else:
        if(a<=0):
            a=0
        elif (b<=0):
            b=a
            a=0
        elif (b<a):
            aux=b
            b=a
            a=aux
        print("La sucesión es: ")
        for i in range(a,b):
            print(i)
            c=c+1
            if(i%2==0):
                d=d+i
            else:
                e=e+i
        print("El número de términos de la sucesión es:",c)
        print("La suma de los números pares de la sucesión",d)
        print("La suma de los números impares de la sucesión",e)
        