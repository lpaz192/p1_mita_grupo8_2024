import re

#Patron
patron_hashtag = r'^#[a-zA-Z0-9_.@!()/&%$]{1,15}$'

#Funcion lambda
comprobar_hashtag = lambda hashtag: re.match(patron_hashtag,hashtag)

#Validar hashtag
def validar_hashtag():
    hashtag = input("Ingrese un hashtag: ")
    while True:
        if comprobar_hashtag(hashtag):
            return hashtag
        else:
            hashtag = input("Hashtag invalido, por favor ingrese un hashtag valido: ")

#Hashtag no repetido
def hashtag_no_repetido(hashtag_dict):
    while True:
        hashtag = validar_hashtag()
        if hashtag in hashtag_dict:
            print("El hashtag ingresado ya existe.")
        else:
            return hashtag

#hashtag existente
def hashtag_existente(hashtag_dict):
    hashtag = input()
    while True:
        if hashtag in hashtag_dict:
            return hashtag
        else:
            hashtag = input("El hashtag ingresado no existe, por favor ingrese un hashtag existente: ")