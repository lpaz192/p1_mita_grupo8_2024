import re
from datetime import datetime

patron_mail = r"^[a-zA-Z0-9_]{2,20}+@[a-zA-Z]{2,10}+\.[a-zA-Z]{2,10}"
patron_usuario = r"^[a-zA-Z_]{2,20}"


#Funciones lambda
comprobar_usuario= lambda nombre:re.match(patron_usuario,nombre)
comprobar_mail=lambda mail:re.match(patron_mail,mail)

#Funciones

def validar_fecha(fecha):
    try: 
        datetime.strtime(fecha, '%Y-%m-%d')
        return True 
    except ValueError:
        return False

#Validar numero
def validar_numero(tipo, min_digitos=1, max_digitos=12):
    numero=input(f"Ingrese el numero de {tipo} (entre {min_digitos} y {max_digitos} digitos): ")
    while True:
        if numero.isdigit() and len(numero)>=min_digitos and len(numero)<= max_digitos:
            return int(numero)
        else:
            numero=input(f"Numero invalido, por favor ingree un numero entre {min_digitos} y {max_digitos} digitos: ")

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
    id_seleccion = input(f"Ingrese un id existente: ")
    while True:
        for id_usuarios in usuarios:
            if id_seleccion.isdigit() and int(id_seleccion) == id_usuarios:
                return int(id_seleccion)
        id_seleccion = input("Numero de id invalido, por favor ingrese un id valido: ")