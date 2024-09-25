import re
patron_mail = r"^[a-zA-Z0-9._-]{2,15}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
patron_usuario = r"^[a-zA-Z_0-9]{2,15}$"

#Funciones lambda
comprobar_usuario= lambda nombre:re.match(patron_usuario,nombre)
comprobar_mail=lambda mail:re.match(patron_mail,mail)

#Validar usuario
def validar_usuario():  #Se busca validar que el usuario ingresado sea correcto
    usuario = input("Ingrese un nuevo usuario: ")  #Solicitar usuario
    while True:
        if comprobar_usuario(usuario):     #Validar información
            return usuario     
        else:
            usuario=input("Usuario invalido, por favor ingrese un usuario valido: ")

#Validar mail
def validar_mail():     #Se busca validar que el mail ingresado sea correcto
    correo= input("Ingrese un nuevo correo: ") #Solicitar correo
    while True:
        if comprobar_mail(correo):         #Validar correo   
            return correo
        else:
            correo=input("Correo invalido, por favor ingrese un correo valido: ")

#Validar id
def validar_id(usuarios):
    id_seleccion = input("ingrese un id de un usuario existente: ")
    while True:
        for id_usuarios in usuarios:
            if id_seleccion.isdigit() and int(id_seleccion) == id_usuarios:
                return int(id_seleccion)
        id_seleccion = input("Numero de id invalido, por favor ingrese un id valido: ")