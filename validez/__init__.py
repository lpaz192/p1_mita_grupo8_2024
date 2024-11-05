from .hashtag import (validar_hashtag, 
                      hashtag_no_repetido, 
                      hashtag_existente)
from .usuario import validar_id, validar_mail, validar_usuario
from .publicacion import validar_fecha
import re

#Validar numero
def validar_numero(tipo, min_digitos=1, max_digitos=12):
    '''Pide el ingreso de un numero entre el rsngo de digitos indicado
    en caso de ser indicado el rango, este va a tomar un valor mminimo de 1 
    y un valor maximo de 12'''
    
    patron=rf"^[0-9]{{{min_digitos},{max_digitos}}}$"

    num = input(f"Ingrese el numero de {tipo} (entre {min_digitos} y {max_digitos} digitos): ")
    
    while not re.match(patron,num):  #Buscar validez del numero
        num = input("Numero invalido, por favor ingrese un numero valido: ") #Pedir un nuevo numero
    return int(num)
    
#Validacion de datos
def obtener_opcion(opciones_list):
    '''La funcion recibe una lista con los posibles valores que puede elegir
    el usuario
    '''

    while True:
        try:
            opcion = int(input('Seleccione una opcion: '))
            if not opcion in opciones_list:
                print('Opcion invalida, por favor selecione una opcion valida.')
                continue
            return opcion
        except ValueError:
            print('Entrada invalida, por favor selecione una opcion valida.')
