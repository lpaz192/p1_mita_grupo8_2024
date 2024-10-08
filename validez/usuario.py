import re
patron_mail = r"^[a-zA-Z0-9._-]{2,15}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
patron_usuario = r"[a-zA-Z_0-9]{2,15}$"

#Funciones lambda
comprobar_usuario= lambda nombre:re.match(patron_usuario,nombre)
comprobar_mail=lambda mail:re.match(patron_mail,mail)

#Validar usuario
def validar_usuario():
    ''''Pide un ingreso de usuario, en caso de que sea invalido 
    entra en el while hasta conseguir un usuario valido'''

    usuario = input("Ingrese un nuevo usuario: ")  #Solicitar usuario
    
    while not comprobar_usuario(usuario):  #Buscar validez del usuario
        usuario=input("Usuario invalido, por favor ingrese un usuario valido: ") #Pedir un nuevo usuario
    return usuario

#Validar mail
def validar_mail():
    ''''Pide un ingreso de correo, en caso de que sea invalido 
    entra en el while hasta conseguir un correo valido'''
    
    correo= input("Ingrese un nuevo correo: ") #Solicitar correo

    while not comprobar_mail(correo): #Buscar validez del correo
        correo=input("Correo invalido, por favor ingrese un correo valido: ") #Pedir un nuevo inreso
    return correo

#Validar id
def validar_id(usuarios):

    ids = usuarios.keys()
    while True:
        try:
            id_existente = int(input())
            if not id_existente in ids:
                print('El id ingresado no existe, por favor ingrese un id existente: ')
                continue
            return id_existente
        except ValueError:
            print('Entrada no valida, por favor ingrese un id existente: ')