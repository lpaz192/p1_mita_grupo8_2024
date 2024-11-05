<<<<<<< HEAD
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



=======
import diseño, validez, json
>>>>>>> fb37805bae5d3efc6021c1a514b7faa8a305290e
#Funciones secundarias de Hashtags
def selccionar_elemento_hashtag(hashtagh_opcion,hashtags_dict): 
    print(f"\n---Hashtag {hashtagh_opcion}---")
    print(f"1. Cantidad de posteos: {hashtags_dict[hashtagh_opcion]['Cant. posteos']}")
    print(f"2. Veces compartido:    {hashtags_dict[hashtagh_opcion]['Veces compartido']}")
    print(f"3. Likes:               {hashtags_dict[hashtagh_opcion]['Likes']}")
    opciones=[1,2,3]
    return validez.obtener_opcion(opciones)
    
#Funciones CRUD Hashtags
def agregar_hashtag(nombre_archivo):      #Agregar
    with open(nombre_archivo, 'r', encoding='UTF-8') as archivo:
        hashtags = json.load(archivo)

    nuevo_hashtag = validez.hashtag_no_repetido(hashtags)
    hashtags[nuevo_hashtag] = {
        'Cant. posteos'   :validez.validar_numero('cantidad de posteos',1,10),
        'Veces compartido':validez.validar_numero('veces compartido',1,10),
        'Likes'           :validez.validar_numero('likes',1,10),
    }

    with open(nombre_archivo, 'w', encoding='UTF-8') as archivo:
        json.dump(hashtags, archivo, indent = 4)

def leer_hashtag(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='UTF-8') as archivo:
        hashtags = json.load(archivo)

    hashtag_keys = list(hashtags.keys())
    
    diseño.hashtags.parte_superior()
    diseño.hashtags.encabezado()
    for i in range(len(hashtag_keys)):
        if i == 0:
            diseño.hashtags.parte_conectiva()
            diseño.hashtags.mostrar(hashtag_keys[i], hashtags[hashtag_keys[i]])
        elif i == len(hashtag_keys)-1:
            diseño.hashtags.parte_conectiva()
            diseño.hashtags.mostrar(hashtag_keys[i], hashtags[hashtag_keys[i]])
        else:
            diseño.hashtags.parte_conectiva()
            diseño.hashtags.mostrar(hashtag_keys[i], hashtags[hashtag_keys[i]])
    diseño.hashtags.parte_inferior()

def actualizar_hashtag(nombre_archivo):
    leer_hashtag(nombre_archivo)
    print('\nIngres el hashtag que desea modificar: ',end="")
    
    with open(nombre_archivo, 'r', encoding='UTF-8') as archivo:
        hashtags = json.load(archivo)
    
    opcion_hashtag = validez.hashtag_existente(hashtags)
    elemento_elegido = selccionar_elemento_hashtag(opcion_hashtag,hashtags)
        
    #Eliminar Cant. Posteos
    if elemento_elegido == 1:
        hashtags[opcion_hashtag]['Cant. posteos'] = validez.validar_numero('cantidad de posteos',1,10)
    
    #Eliminar Veces Compartido
    elif elemento_elegido == 2:
        hashtags[opcion_hashtag]['Veces compartido']=validez.validar_numero('veces compartido',1,10)
    
    #Eliminar Likes
    else:
        hashtags[opcion_hashtag]['Likes']=validez.validar_numero('likes',1,10)

    with open(nombre_archivo, 'w', encoding='UTF-8') as archivo:
        json.dump(hashtags, archivo, indent = 4)

def eliminar_hashtag(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='UTF-8') as archivo:
        hashtags = json.load(archivo)

    leer_hashtag('hashtag.json')
    print("\nPara eliminar ingrese un hashtag existente: ",end="")
    hashtag_eliminar = validez.hashtag_existente(hashtags)
    
    hashtags.pop(hashtag_eliminar)

    with open(nombre_archivo, 'w', encoding='UTF-8') as archivo:
        json.dump(hashtags, archivo, indent = 4)