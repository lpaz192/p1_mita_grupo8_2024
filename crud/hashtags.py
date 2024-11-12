import diseño, validez, json

def cargar_hashtags(filename='hashtags.json'):
    '''Recibe el nombre del archivo y lo intenta abrir
    si no recibe ningún nombre abre el archivo "hashtags.json" '''
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_hashtags(hashtags_dict, filename='hashtags.json'):
    '''Recibe el nombre del archivo a cerrar
    en caso de no recibir nombre cierra el archivo "hashtags.json" '''
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(hashtags_dict, file, indent = 4)

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
    '''Pide el ingreso de los datos de un nuevo hashtag no repetido'''
    hashtags = cargar_hashtags(nombre_archivo)

    print('\n---Agregar Hashtag---')
    nuevo_hashtag = validez.hashtag_no_repetido(hashtags)
    hashtags[nuevo_hashtag] = {
        'Cant. posteos'   :validez.validar_numero('cantidad de posteos',1,10),
        'Veces compartido':validez.validar_numero('veces compartido',1,10),
        'Likes'           :validez.validar_numero('likes',1,10),
    }
    guardar_hashtags(hashtags, nombre_archivo)

def leer_hashtag(nombre_archivo):
    '''Muestra los valores del diccionario en forma de tabla'''
    hashtags = cargar_hashtags(nombre_archivo)

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
    
    hashtags = cargar_hashtags(nombre_archivo)
    
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

    guardar_hashtags(hashtags, nombre_archivo)

def eliminar_hashtag(nombre_archivo):
    hashtags = cargar_hashtags(nombre_archivo)

    leer_hashtag('hashtags.json')
    print("\nPara eliminar ingrese un hashtag existente: ",end="")
    hashtag_eliminar = validez.hashtag_existente(hashtags)
    
    hashtags.pop(hashtag_eliminar)

    guardar_hashtags(hashtags, nombre_archivo)