import json
from crud import cargar_hashtags, guardar_hashtags  
import validez  
import diseño 

#Funcioes de carga de archivos
def cargar_hashtags_spam(filename='hashtags_spam.txt'):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            return set([line.strip() for line in file])
    except FileNotFoundError:
        print("Archivo de hashtags spam no encontrado.")
        return set()

def cargar_hashtags(filename='hashtags.json'):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_hashtags(hashtags_dict, filename='hashtags.json'):
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(hashtags_dict, file, indent=4)

#Funciones de CuentasSPAM
def contar_hashtags_spam(hashtags_dict, spam_set, index=0, count=0):
    hashtag_keys = list(hashtags_dict.keys())
    
    # si se recorrio todos los hashtags 
    if index >= len(hashtag_keys):
        return count

    # revisa si el hashtag actual está en la lista de spam
    hashtag_actual = hashtag_keys[index]
    if hashtag_actual in spam_set:
        count += 1
    
    # llamada recursiva avanzando al siguiente indice
    return contar_hashtags_spam(hashtags_dict, spam_set, index + 1, count)

def mostrar_hashtags_spam(hashtags_dict, spam_set, index=0):
    hashtag_keys = list(hashtags_dict.keys())
    
    # si se recorre todos los hashtags 
    if index >= len(hashtag_keys):
        return
    
    hashtag_actual = hashtag_keys[index]
    if hashtag_actual in spam_set:
        print(f"Hashtag '{hashtag_actual}' es spam, utilizado en {hashtags_dict[hashtag_actual]['Cant. posteos']} posteos, "
              f"{hashtags_dict[hashtag_actual]['Veces compartido']} veces compartido, {hashtags_dict[hashtag_actual]['Likes']} likes.")
    
    # llamada recursiva avanzando al siguiente indice
    mostrar_hashtags_spam(hashtags_dict, spam_set, index + 1)

def analizar_spam_hashtags():
    # carga el archivo JSON con los hashtags existentes
    hashtags = cargar_hashtags()
    #carga el archivo de texto con los hashtags clasificados como spam
    hashtags_spam = cargar_hashtags_spam()

    #cuenta los hashtags clasificados como spam
    total_spam = contar_hashtags_spam(hashtags, hashtags_spam)
    print(f"Total de hashtags clasificados como spam encontrados: {total_spam}")
    
    mostrar_hashtags_spam(hashtags, hashtags_spam)
    input()


