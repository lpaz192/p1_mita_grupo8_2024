from .hashtag import validar_hashtag, hashtag_no_repetido, hashtag_existente
from .usuario import validar_id, validar_mail, validar_usuario
from .publicacion import validar_fecha
#Validar numero
def validar_numero(tipo, min_digitos=1, max_digitos=12):
    numero=input(f"Ingrese el numero de {tipo} (entre {min_digitos} y {max_digitos} digitos): ")
    while True:
        if numero.isdigit() and len(numero)>=min_digitos and len(numero)<= max_digitos:
            return int(numero)
        else:
            numero=input(f"Numero invalido, por favor ingree un numero entre {min_digitos} y {max_digitos} digitos: ")