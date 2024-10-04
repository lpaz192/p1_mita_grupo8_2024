from .hashtag import validar_hashtag, hashtag_no_repetido, hashtag_existente
from .usuario import validar_id, validar_mail, validar_usuario
from .publicacion import validar_fecha
import re
#Validar numero
def validar_numero(tipo, min_digitos=1, max_digitos=12):
    patron=rf"[0-9]{{{min_digitos} , {max_digitos}}}"
    comprobar_numero=lambda numero:re.match(patron,numero)
    num=input("x: ")
    while not comprobar_numero(num):  #Buscar validez del usuario
        usuario=input("Numero invalido, por favor ingrese un usuario valido: ") #Pedir un nuevo usuario
    return usuario
    
    """
    while True:
        try: 
            numero=int(input(f"Ingrese el numero de {tipo} (entre {min_digitos} y {max_digitos} digitos): "))
            if len(numero) < min_digitos  or len(numero) > max_digitos:
                print('Numero fuera de rango. ')
                continue
            return numero
        except ValueError:
            print('Entrada no valida. ')
"""
"""
    while True:
        if numero.isdigit() and len(numero)>=min_digitos and len(numero)<= max_digitos:
            return int(numero)
        else:
            numero=input(f"Numero invalido, por favor ingree un numero entre {min_digitos} y {max_digitos} digitos: ")
            """

