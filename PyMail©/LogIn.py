def guardarFichero(correo,contraseña):
    """Crea un fichero con el correo y la contraseña de la
    cuenta que está ahora mismo conectada a la aplicación"""
    f=open("InicioDeSesión"+".txt","w")
    f.write(correo+"\n")
    f.write(contraseña)
    f.close()

def cerrarSesión():
    """Deja el fichero de inicio de sesión completamente en blanco"""
    f=open("InicioDeSesión"+".txt","w")
    f.write(""+"\n")
    f.write("")


def iniciarSesión():
    """Te pide que introduzcas un correo y su contraseña, si el correo
    no contiene @gmail.com te pide que vuelvas a introducirlo"""
    correo=input("Nombre del correo electronico: ")
    while "@gmail.com" not in correo:
        correo=input("El nombre del correo debe incluir @gmail.com: ")
    contraseña=input("Contraseña del correo: ")
    guardarFichero(correo,contraseña)

def leerFichero():
    """Lee las líneas de el fichero inicio de sesión para así luego poder
    almacenar el correo y la contraseña"""
    f=open("InicioDeSesión"+".txt","r")
    cad1=[]
    for linea in f:
        cad1.append(linea.strip("\n"))
    f.close()
    return(cad1)

