import diseño, validez

'''


import json

def cargar_usuarios(filename='usuarios.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_usuarios(usuarios, filename='usuarios.json'):
    with open(filename, 'w') as file:
        json.dump(usuarios, file)

def agregar_usuario(usuarios):
    usuarios[nuevo_id(usuarios)] = {   
        'Usuario': validez.validar_usuario(),
        'Seguidores': validez.validar_numero('seguidores'),
        'Seguidos': validez.validar_numero('seguidos'),
        'Likes': validez.validar_numero('likes'),
        'Correo': validez.validar_mail()
    }
    guardar_usuarios(usuarios)


'''





nuevo_id=lambda usuarios: max(usuarios.keys())+1 if usuarios else 1

#Funciones secundarias de usarios
def seleccionar_elemento_usuarios(id,usuario):
    print(f"\n---Usuario con ID {id}---")
    print(f"1. Usuario:      {usuario[id]['Usuario']}")
    print(f"2. Seguidores:   {usuario[id]['Seguidores']}")
    print(f"3. Seguidos:     {usuario[id]['Seguidos']}")
    print(f"4. Likes:        {usuario[id]['Likes']}")
    print(f"5. Correos:      {usuario[id]['Correo']}")
    elemento = input("Seleccione un elemento: ")
    while True:
        if elemento.isdigit() and int(elemento) > 0 and int(elemento) <= 5:
            return int(elemento)
        else:
            elemento = input("Elemento invalido, por favor ingrese un elemento valido: ")

#Funciones CRUD Usuarios

#Funcion agregar usuario
def agregar_usuario(usuarios):      
    '''Crea un nuevo id que es una sucesión del mas grande y posteriormente 
    pide el ingreso de los datos'''
    usuarios[nuevo_id(usuarios)] = {   
        'Usuario':    validez.validar_usuario(),
        'Seguidores': validez.validar_numero('seguidores'),
        'Seguidos':   validez.validar_numero('seguidos'),
        'Likes':      validez.validar_numero('likes'),
        'Correo':     validez.validar_mail()
    }
   
#Funcion leer usuario
def leer_usuario(usuarios):        
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
def actualizar_usuario(opcion_usuario,elemento_elegido,usuarios):    
    
    #Actualizar Usuario
    if elemento_elegido == 1:   
        usuarios[opcion_usuario]['Usuario']=validez.validar_usuario()
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

#Funcion eliminar usuario
def eliminar_usuario(id,usuarios): 
    usuarios.pop(id)
