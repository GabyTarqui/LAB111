h,m,s=map(int,input("Ingrese la hora inicial con el formato hh:mm:ss ").split(":",3))
G=100
if(h<24 and h>=0) and (m<60 and m>=0) and (s<60 and s>=0):
    while 1<G:
        print("1: Incrementar un segundo. \n2: Finalizar programa")
        Resp=int(input("Ingrese una opción "))
        if (Resp==1):
            s=int(s)
            m=int(m)
            h=int(h)
            s=s+1
            if (s==60):
                m=m+1
                s=0
            if(m==60):
                h=h+1
                m=0
            if(h==24):
                h=0
                m=0
                s=0
            if(h<10):
                h = "0" + str(h)
            if(m<10):
                m = "0" + str(m)
            if(s<10):
                s = "0" + str(s)
            print(h,":",m,":",s)
        if (Resp==2):
            G=1
        if ((Resp!=1) and (Resp!=2)):
            print("Opción no válida \nLas opciones válidas son:")
else:
    print("Hora no válida")