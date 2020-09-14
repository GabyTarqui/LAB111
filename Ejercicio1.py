TDis=int(input("Ingrese el tiempo que tiene disponible, en segundos: "))
if (TDis>=0):
    h,m,s=map(int,input("Ingrese el tiempo que le tomará realizar la tarea, en el formato hh:mm:ss ").split(":",3))
    if (m>=0 and m<60) and (s>=0 and s<60):
        h=h*3600
        m=m*60
        TTar=h+m+s
        Tiempo=TDis-TTar
        if(Tiempo>=0):
            print("Se podrá finalizar la tarea")
        else:
            print("No se podrá finalizar la tarea")
    else:
        print("El tiempo de la tarea no es válido")
else:
    print("El tiempo no es válido")
    