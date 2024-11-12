from crud import cargar_usuarios
import re, json
patron_mail    = r"^[a-zA-Z0-9._-]{2,15}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
patron_usuario = r"[a-zA-Z_0-9]{2,15}$"

#Funciones lambda
comprobar_usuario = lambda nombre:re.match(patron_usuario,nombre)
comprobar_mail    = lambda mail:re.match(patron_mail,mail)

#Comparar usuario
def comparar_usuario(nombre_usuario, usuarios):
    for usuario_id, datos in usuarios.items():
        if datos['Usuario'] == nombre_usuario:
            return True
         
    return False

#Validar usuario
def validar_usuario(usuario_dict):
    ''''Pide un ingreso de usuario, en caso de que sea invalido 
    entra en el while hasta conseguir un usuario valido'''

    usuario = input("Ingrese un nuevo usuario: ")  #Solicitar usuario
    
    while not comprobar_usuario(usuario):  #Buscar validez del usuario
        usuario=input("Usuario invalido, por favor ingrese un usuario valido: ") #Pedir un nuevo usuario
    while comparar_usuario(usuario, usuario_dict):
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
def validar_id(nombre_archivo):
    usuarios = cargar_usuarios(nombre_archivo)
    
    ids = usuarios.keys()
    while True:
        id_existente = input()
        if id_existente in ids:
            return id_existente
        else:
            print('El id ingresado no existe, por favor ingrese un id existente: ', end='')