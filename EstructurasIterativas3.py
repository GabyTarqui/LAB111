#Gabriela Celeste Tarqui Quintanilla
n=int(input("Ingrese un número: "))
a=0
b=0
c=1
for i in range(1,n+1):
    if(i%3==0):
        print(c)
        a=b
        b=c
        c=a+b
    else:
        print(0)