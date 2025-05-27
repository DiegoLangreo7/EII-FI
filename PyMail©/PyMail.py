from email.message import EmailMessage
import smtplib
from tkinter import *
from LogIn import *
from SendMail import *





iniciarSesión()
datos=leerFichero()
remitente=datos[0]
contraseña=datos[1]

root=Tk()
root.title("PyMail")
root.iconbitmap("vaca.ico")

miFrame=Frame()
miFrame.pack()
miFrame.config(width="650",height="350")
miFrame.config(cursor="hand2")

miTexto=Text(miFrame,width=100,height=30)
miTexto.grid(row=3,column=1,padx=10,pady=5)

barrita=Scrollbar(miFrame,command=miTexto.yview)
barrita.grid(row=3,column=2,sticky="nsew")

miTexto.config(yscrollcommand=barrita.set)

miDestinatarioCuadro=Text(miFrame,width=100,height=1)
miDestinatarioCuadro.grid(row=1,column=1)

miAsuntoCuadro=Text(miFrame,width=100,height=1)
miAsuntoCuadro.grid(row=2,column=1)

miDestinatarioLabel=Label(miFrame,text="Destinatario:")
miDestinatarioLabel.grid(row=1,column=0,sticky="e",padx=10,pady=5)

miAsuntoLabel=Label(miFrame,text="Asunto:")
miAsuntoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=5)

miTextoLabel=Label(miFrame,text="Texto:")
miTextoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=5)

def codigoBoton():
    """Al darle al botón enviar, se envía el correo"""
    destinatario=miDestinatarioCuadro.get(1.0,2.0)
    asunto=miAsuntoCuadro.get(1.0,2.0)
    texto=miTexto.get(1.0,10000.0)
    f=open("DatosDeEnvio"+".txt","w")
    f.write(destinatario)
    f.write(asunto)
    f.write(texto)
    f.close()
    f=open("DatosDeEnvio"+".txt","r")
    cad1=[]
    for linea in f:
        cad1.append(linea.strip("\n"))
    f.close()
    destinatario=cad1[0].split()
    asunto=cad1[1]
    texto=""
    for i in range(2,len(cad1)):
        texto=texto+cad1[i]+"\n"
    send(remitente,contraseña,destinatario,asunto,texto)

def cerrar():
    """Al darle al botón de cerrar sesión, se borran los datos
    del correo y contraseña de la persona y permite volver a introducir
    el inicio de sesión para seguir redactando correos con otra cuenta
    si fuera necesario sin salir de la aplicación"""
    cerrarSesión()
    iniciarSesión()


botonEnviar=Button(root,text="Enviar",command=codigoBoton)
botonEnviar.pack()

botonCerrar=Button(root,text="Cerrar Sesión",command=cerrar)
botonCerrar.pack()



root.mainloop()