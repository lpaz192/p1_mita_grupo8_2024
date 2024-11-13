import diseño, validez, json

#Funciones de carga de archivos
def cargar_usuarios(filename='usuarios.json'):
    '''Recibe el nombre del archivo y lo intenta abrir
    si no recibe ningún nombre abre el archivo "usuarios.json" '''
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_usuarios(usuarios, filename='usuarios.json'):
    '''Recibe el nombre del archivo a cerrar
    en caso de no recibir nombre cierra el archivo "usuarios.json" '''
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(usuarios, file, indent = 4)

nuevo_id = lambda claves: max(claves) + 1 if claves else 1

#Funciones secundarias de usarios
def seleccionar_elemento_usuarios(id,usuario):
    print(f"\n---Usuario con ID {id}---")
    print(f"1. Usuario:      {usuario[id]['Usuario']}")
    print(f"2. Seguidores:   {usuario[id]['Seguidores']}")
    print(f"3. Seguidos:     {usuario[id]['Seguidos']}")
    print(f"4. Likes:        {usuario[id]['Likes']}")
    print(f"5. Correos:      {usuario[id]['Correo']}")
    opciones = [1,2,3,4,5]
    return validez.obtener_opcion(opciones)

#FUNCIONES CRUD USUARIOS

#Funcion agregar usuario
def agregar_usuario(nombre_archivo):      
    '''Crea un nuevo id que es una sucesión del mas grande y posteriormente 
    pide el ingreso de los datos'''
   
    usuarios = cargar_usuarios()
    
    print('---Agregar Usuario---')

    claves = [int(ids) for ids in usuarios] 
    usuarios[nuevo_id(claves)] = {   
        'Usuario':    validez.validar_usuario(usuarios),
        'Seguidores': validez.validar_numero('seguidores'),
        'Seguidos':   validez.validar_numero('seguidos'),
        'Likes':      validez.validar_numero('likes'),
        'Correo':     validez.validar_mail()
    }

    guardar_usuarios(usuarios)
   
#Funcion leer usuario
def leer_usuario(nombre_archivo): 
    '''Muestra los valores del diccionario en forma de tabla'''       
    usuarios = cargar_usuarios(nombre_archivo)

    diseño.usuarios.parte_superior()
    diseño.usuarios.encabezado()

    for id_usuario, datos_usuario in usuarios.items():
        if id_usuario==min(usuarios.keys()):
            diseño.usuarios.parte_conectiva()
            diseño.usuarios.mostrar(id_usuario,datos_usuario)
        
        elif max(usuarios.keys())==id_usuario:
            diseño.usuarios.parte_conectiva()
            diseño.usuarios.mostrar(id_usuario, datos_usuario)
        
        else:
            diseño.usuarios.parte_conectiva()
            diseño.usuarios.mostrar(id_usuario, datos_usuario)
    
    diseño.usuarios.parte_inferior()

#Funcion actualizar usuario
def actualizar_usuario(nombre_archivo):    
    '''Pide el ingreso'''
    usuarios = cargar_usuarios(nombre_archivo)
    
    leer_usuario('usuarios.json')  #Se muestra la matriz
    #Se selecciona el usuario a modificar
    print('---Actualización de Usuario---')
    print("\nIngrese el ID del usuario que desea modificar: ",end="")
    opcion_usuario = validez.validar_id('usuarios.json')   
    
    #Se selecciona el elemento a modificar
    elemento_elegido = seleccionar_elemento_usuarios(opcion_usuario,usuarios) 
    
    #Actualizar Usuario
    if elemento_elegido == 1:   
        usuarios[opcion_usuario]['Usuario']=validez.validar_usuario(usuarios)
    #Actualizar Seguidores
    elif elemento_elegido == 2: 
        usuarios[opcion_usuario]['Seguidores'] = validez.validar_numero('seguidores')
    #Actualizar Seguidos
    elif elemento_elegido == 3: 
        usuarios[opcion_usuario]['Seguidos'] = validez.validar_numero('seguidos')
    #Actualizar Likes
    elif elemento_elegido == 4: 
        usuarios[opcion_usuario]['Likes'] = validez.validar_numero('likes')
    #Actualizar Correo
    else:                       
        usuarios[opcion_usuario]['Correo'] = validez.validar_mail()
    
    guardar_usuarios(usuarios, nombre_archivo)
        
#Funcion eliminar usuario
def eliminar_usuario(nombre_archivo,id): 
    usuarios = cargar_usuarios(nombre_archivo)
    
    usuarios.pop(id)
    
    guardar_usuarios(usuarios, nombre_archivo)