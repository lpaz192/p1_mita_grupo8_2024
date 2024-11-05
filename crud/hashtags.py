import diseño, validez

'''
import json

def cargar_hashtags(filename='hashtags.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_hashtags(hashtags_dict, filename='hashtags.json'):
    with open(filename, 'w') as file:
        json.dump(hashtags_dict, file)

def agregar_hashtag(hashtag_dict):
    print()
    nuevo_hashtag = validez.hashtag_no_repetido(hashtag_dict)
    hashtag_dict[nuevo_hashtag] = {
        'Cant. posteos': validez.validar_numero('cantidad de posteos', 1, 10),
        'Veces compartido': validez.validar_numero('veces compartido', 1, 10),
        'Likes': validez.validar_numero('likes', 1, 10),
    }
    guardar_hashtags(hashtag_dict)  # Guardar cambios en el archivo JSON

def leer_hashtag(hashtags_dict):
    hashtags_dict = cargar_hashtags()
    # aca seria igual a lo que teniamos, agregar

'''



#Funciones secundarias de Hashtags
def selccionar_elemento_hashtag(hashtagh_opcion,hashtags_dict): 
    print(f"\n---Hashtag {hashtagh_opcion}---")
    print(f"1. Cantidad de posteos: {hashtags_dict[hashtagh_opcion]['Cant. posteos']}")
    print(f"2. Veces compartido:    {hashtags_dict[hashtagh_opcion]['Veces compartido']}")
    print(f"3. Likes:               {hashtags_dict[hashtagh_opcion]['Likes']}")
    elemento = input("Seleccione un elemento: ")
    while True:
        if elemento.isdigit() and int(elemento) >= 1 and int(elemento) <= 3:
            return int(elemento)
        else:
            elemento= input("elemento invalido, por favor seleccione un elemento valido: ")    


#Funciones CRUD Hashtags
def agregar_hashtag(hashtag_dict):      #Agregar
    #Agregar hashtag
    print()
    nuevo_hashtag= validez.hashtag_no_repetido(hashtag_dict)
    hashtag_dict[nuevo_hashtag] = {
        'Cant. posteos'   :validez.validar_numero('cantidad de posteos',1,10),
        'Veces compartido':validez.validar_numero('veces compartido',1,10),
        'Likes'           :validez.validar_numero('likes',1,10),
    }

def leer_hashtag(hashtags_dict):
    hashtag = list(hashtags_dict.keys())
    diseño.hashtags.parte_superior()
    diseño.hashtags.encabezado()
    for i in range(len(hashtag)):
        if i == 0:
            diseño.hashtags.parte_conectiva()
            diseño.hashtags.mostrar(hashtag[i], hashtags_dict[hashtag[i]])
        elif i == len(hashtag)-1:
            diseño.hashtags.parte_conectiva()
            diseño.hashtags.mostrar(hashtag[i], hashtags_dict[hashtag[i]])
        else:
            diseño.hashtags.parte_conectiva()
            diseño.hashtags.mostrar(hashtag[i], hashtags_dict[hashtag[i]])
    diseño.hashtags.parte_inferior()

def actualizar_hashtag(opcion_hashtag,elemento_elegido,hashtag_dict):
    if elemento_elegido == 1:
        hashtag_dict[opcion_hashtag]['Cant. posteos']=validez.validar_numero('cantidad de posteos',1,10)
        return
    
    elif elemento_elegido == 2:
        hashtag_dict[opcion_hashtag]['Veces compartido']=validez.validar_numero('veces compartido',1,10)
        return
    else:
        hashtag_dict[opcion_hashtag]['Likes']=validez.validar_numero('likes',1,10)
        return

def eliminar_hashtag(hashtag_eliminar,hashtag_dict):
    hashtag_dict.pop(hashtag_eliminar)
