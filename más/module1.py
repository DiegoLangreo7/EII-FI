# Dado un numero entero n>=0, ecribir un programa para obtener la suma
# de los n primeros numeros naturales y escribir el resultado
# obtenido en la forma:

#con for:
##for i in range (1,1000,1):
##    n=int(input("Entero natural?"))
##    if n>=1:
##        break
##print(n)
##s=0
##for i in range(1,n+1,1):
##    s=s+i
##print("La suma de los ",n,"numeros naturales es ",s)
#con while:
##n=0
##while n<1:
##    n=int(input("Entero natural?"))
##i=1
##s=0
##while i<=n:
##    s=s + i
##    i=i + 1
##print("La suma de los ",n,"numeros naturales es ",s)
#-------------------------------------------------------------------------------

# Dados dos enteros a>0 y b, modificar el programa anterior para calcular
# la expresión matemática y escribir el resultado en pantalla.

##a=0
##while a<=0:
##    a=int(input("Entero >0?"))
### leer b OBLIG >=a
##b=a-1
##while b<=a:
##    b=int(input("Entero>="+str(a)+" ?"))
##print(a,b)
##s=0
##for i in range (a,b+1):
##    s=s + (i*i+1)/i
##print ("La suma pedida es=",round(s,3))
#-------------------------------------------------------------------------------

# Dado un numero natural n, escribir un programa que musetre todos sus
# divisores en la forma: "Los divisores de 12 son: 1 2 3 4 6 12."

##n=0
##while n<=1:
##    n=int(input("Entero >=1?"))
##cdiv=0
###calcular y escribir los divisores
##print("Los divisores de",n,"son",end=" ")
##for i in range (1,n+1):
##    if n%i==0:
##        print(i,end=" ")
##        cdiv=cdiv+1
##print()
##print("Cantidad divisores =",cdiv)
#-------------------------------------------------------------------------------

# Dado un numero natural n, escribe un programa que clasifique dicho numero
# en perfecto, abundante o defectivo. Ademas, en este ultimo caso,
# debera indicarse si es o no primo.
##DEFINICION: un numero natural se dice que es perfecto si es igual a la
## suma de todos sus divisores propios, abundante si la suma es mayor que el
## y defectivo si la suma es menor.

##n=0
##while n<1:
##    n=int(input("Numero >=1? "))
##sdiv=0
##for i in range (1,n):
##    if n%i==0:
##        sdiv=sdiv+i
##
##if sdiv>n:
##    print(sdiv,n,"es abundante")
##elif sdiv==n:
##    print (sdiv,n,"es perfecto")
##else:
##    if sdiv==1:
##        print (sdiv,n,"es defectivo primo")
##    else:
##        print(sdiv,n,"es defectivo no primo")

#Dado un número natural n, escribe un programa para generar (escribir
#en pantalla) la secuencia de los n primeros números de Perrin.
# Los tres primeros números de esta secuencia son P(0)=3,
#P(1)=0 y P(2)=2 y el resto se obtienen en la forma:
#P(n) = P(n-2) + P(n-3) si n>2.

n=-1
while n<0:
    n=int(input("Numero >0"))
p=0
for n in range (0,n+1):
    if n==2:
        print ("Numeros de perrin 3,0,2")
    elif n==1:
        print ("Numeros de perrin 3,0")
    elif n==0:
        print("Numeros de perrin 3")
    else:
        p=(3-n^2)/(1-(n^2)-(n^3))

        print("Numeros de perrin 3,0,2",p)


























