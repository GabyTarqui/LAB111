print("Ecuación de segundo grado: ax^2+bx+c=0")
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))
n=(b**2)-(4*a*c)
if n>0:
    print("Las raices serán dos números reales y diferentes")
else:
    if n<0:
        print("Las raices serán dos números complejos")
    else:
        print("Las raices serán dos números reales e iguales")