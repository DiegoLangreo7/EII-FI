from math import *

##GUION FUNCIONES 1.

####INTRODUCIR PESO Y ALTURA Y CALCULAR IMC. AÑADIR DEVOLVER
####VALOR NUTRICIONAL.
##def calcularIMC():
##    p=0
##    a=0
##    while p<1:
##        p=int(input("Peso en Kg?"))
##    while a<1:
##        a=float(input("Altura en m?"))
##    IMC=round(p/a**2,2)
##    print("El IMC es:",IMC,end="\n")
##    if IMC<18.5:
##        print("Bajo peso")
##    elif IMC>= 18.5 and IMC<25:
##        print("Peso normal")
##    elif IMC>=25:
##        print("Sobrepeso")
##    else:
##        print("Obesidad")
###ES MEJOR USAR RETURN EN VEZ DE PRINT
##calcularIMC()

####HALLAR LA DISTANCIA AL CENTRO DEL EJE AL PUNTO INTRODUCIDO (x,y)
##def calcularDistancia(x,y):
##    """Calcula el modulo para hallar la distancia
##    al punto 0.0"""
##    m=sqrt(pow(x,2)+pow(y,2)) ##pow(x,2) = elevame x a 2
##    return m
##x=float(input("Introduce x= "))
##y=float(input("Intruduce y= "))
###print(calcularDistancia(x,y))
##
####HALLAR LONGITUD DE UNA CIRCUNFERENCIA DE CENTRO EL PUNTO 0.0
##def longCircunferencia(x,y):
##    """ bla bla bla """
##    return 2*pi*calcularDistancia(x,y)
##def areaCircunferencia(x,y):
##    """ bla bla bla """
##    return pi*(calcularDistancia(x,y)**2)
##print(longCircunferencia(x,y))
##print(areaCircunferencia(x,y))


##def Cuadrado(n):
##    """Introducir numero entero y devuelve contorno de un cuadrado
##    de n * de lado"""
##    m=n
##    for i in range(m):
##        for j in range(m):
##            print("*",end="")
##        print()
##Cuadrado(4)

##def contorno_Cuadrado(n):
##    """Introducir numero entero y devuelve contorno de un cuadrado
##    de n * de lado"""
##    m=n
##    for i in range(0,m):
##        print("*",end="")
##        for j in range(0,m-2):
##            if i==0 or i==m-1:
##                print("*",end="")
##            else:
##                print(" ",end="")
##        print("*",end="")
##        print()
##n=int(input("Lado?"))
##contorno_Cuadrado(n)
##print("Cuadrado sin rellenar de",n,"lado",end="")

##def contorno_Rectangulo(m,n):
##    """Introducir numero entero y devuelve contorno de un cuadrado
##    de n * de lado"""
##    for i in range(0,m):
##        if n==1:
##            print("",end="")
##        else:
##            print("*",end="")
##        for j in range(0,n-2):
##            if i==0 or i==m-1:
##                print("*",end="")
##            else:
##                print(" ",end="")
##        print("*",end="")
##        print()
##n=int(input("Longitud?"))
##m=int(input("Altura?"))
##contorno_Rectangulo(m,n)
##print("Rectangulo sin rellenar de",n,"longitud",m,"altura",end="")

##def sucesion(b,c,d,k):
##    """ bla bla bla """
##    a=0
##    if k==0:
##        a=b
##    else:
##        a=b
##        for i in range(0,k,1):
##            a=a+c*a+d
##    print(a)
##
##b=int(input("Dame la b"))
##c=int(input("Dame la c"))
##d=int(input("Dame la d"))
##k=int(input("Dame la k"))
##sucesion(b,c,d,k)

##def cambioDeBase(m,n):
##    if n==2:
##        print(bin(m))
##    elif n==8:
##        print(oct(m))
##    elif n==10:
##        print(m)
##    elif n==16:
##        print(hex(m))
##m=-1
##while m<0:
##    m=int(input("Dame un número entero positivo"))
##n=-1
##while n<2 or n>16:
##    n=int(input("Dame su base [entre 2 y 16]"))
##cambioDeBase(m,n)

