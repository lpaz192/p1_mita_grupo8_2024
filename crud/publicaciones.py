import diseño, validez, re
from crud import leer_usuario,leer_hashtag, cargar_hashtags, cargar_usuarios

#Funciones de carga de archivos
def cargar_publicaciones(filename='publicaciones.txt'):
    '''Recibe el nombre del archivo y lo intenta abrir
    si no recibe ningún nombre abre el archivo "publicacines.txt" '''
    posteos = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for linea in file:
            datos = re.split(r'\s+', linea.strip())
            posteos.append(datos)
        return posteos

def guardar_publicaciones(posteos, filename='publicaciones.txt'):
    '''Recibe el nombre del archivo a cerrar
    en caso de no recibir nombre cierra el archivo "publicaciones.json" '''
    with open(filename, 'w', encoding='UTF-8') as arch:
        for fila in posteos:
            linea = ''.join([str(dato).ljust(24, ' ') for dato in fila])
            arch.write(linea + '\n')

nuevo_id = lambda claves: max(claves) + 1 if claves else 1

#Funciones secundarias de publicaciones
def selccionar_elemento_publicaciones(posteos, id_post): 
    print(f'\n---Publicación con id: {id_post}---')
    print(f'1. Likes:                {posteos[id_post][2]}')
    print(f'2. Comentarios:          {posteos[id_post][3]}')
    print(f'3. Usuario:              {posteos[id_post][5]}')
    print(f'4. Modificar toda la publicacion')
    opciones=[1,2,3,4]
    return validez.obtener_opcion(opciones)

#Funciones CRUD Publicaciones

#Función agregar hashtag
def agregar_publicacion(archivo_posteo, archivo_usuario, archivo_hashtag):
    posteos = cargar_publicaciones(archivo_posteo)
    usuarios = cargar_usuarios(archivo_usuario)
    hashtags = cargar_hashtags(archivo_hashtag)

    claves = [int(fill[0]) for fill in usuarios] 
    id_post = nuevo_id(claves)
    print('\n---Agregar Publicación')
    while True:
        fecha_publicacion = input('Ingrese la fecha de la publicación (DD-MM-YYYY): ')
        if validez.validar_fecha(fecha_publicacion):
            break
        else:
            print('Fecha inválida, por favor ingrese una fecha en formato válido (DD-MM-YYYY).')
    
    
    likes = validez.validar_numero('likes')
    comentarios = validez.validar_numero('cantidad de comentarios')
    '''
    print('Para seleccionar el usuario que realizo la publicacion')
    print('Ingrese 1 para ingresar el id del usuario o ingrese -1 para ver la tabla: ')
    
    opciones = [-1,1]
    opcion= validez.obtener_opcion(opciones)
    '''
    leer_usuario('usuarios.json')
    print('Ingrese el numero de ID del usuario que utiliza la publicación: ', end='')
    opcion = input()
    while not opcion in usuarios:
            opcion = input('Opcion invalida porfavor ingrese un dato valido: ')
    id_usuario = opcion
    '''
    if opcion == -1:
        leer_usuario('usuarios.json')
        print('Ingrese el id del usuario: ', end='')
        id_usuario =validez.validar_id('usuarios.json')
    else:
        id_usuario = opcion
'''
    usuario = usuarios[id_usuario]['Usuario']
    
    leer_hashtag(archivo_hashtag)
    print('Ingrese el hashtag que utiliza la publicación: ', end='')
    opcion = input()
    while not opcion in hashtags:
            opcion = input('Opcion invalida porfavor ingrese un dato valido: ')
    nombre_hashtag = opcion
    '''
    print("Para seleccionar el hashtag que realizo la publicacion")
    print("Por favor, ingrese el hashtag o selecciones -1 para ver la tabla: ", end="")
    opciones = [-1]
     while True:
        if opcion == -1:
            leer_hashtag(archivo_hashtag)
            print('Ingrese el hashtag de la publicación: ', end='')
            nombre_hashtag = validez.hashtag_existente(hashtags)
            break
        elif opcion in hashtags:
            nombre_hashtag = opcion
            break
        if opcion in hashtags:
            nombre_hashtag = opcion
            break
        else:
        
    '''
    posteos.append([str(id_post).zfill(4), fecha_publicacion, likes, comentarios, id_usuario, usuario, nombre_hashtag])
    input("Publicación agregada exitosamente.")
    guardar_publicaciones(posteos, 'publicaciones.txt')

#Función eliminar publicación
def eliminar_publicacion(nombre_archivo):
    posteos = cargar_publicaciones(nombre_archivo)
    imprimir_posteos(posteos)

    id_post = input("Ingrese el ID de la publicación a eliminar: ").zfill(3)

    for i in range(len(posteos)):
        if posteos[i][0] == id_post:
            del posteos[i]
            print("Publicación eliminada exitosamente.")
            guardar_publicaciones(posteos, nombre_archivo)
            return #aca termina la funcion
    
    #pero si no lo encuentra no hace return y tira la alerta
    print("ID de publicación no encontrado.")

#Función actualizar publicación
def actualizar_publicacion(nombre_archivo):
    posteos = cargar_publicaciones(nombre_archivo)
    imprimir_posteos(posteos)

    ids = [int(claves[0]) for claves in posteos[1:]]
    print('Ingrese el ID de la publicacion a actualizar')
    id_post = validez.obtener_opcion(ids)
   
    opcion = selccionar_elemento_publicaciones(posteos, id_post)

    if opcion == 1:   #Actualizar cantidad de likes
        posteos[id_post][2] = validez.validar_numero('cantidad de likes')

    elif opcion == 2: #Actualizar cantidad de comentarios
        posteos[id_post][3] = validez.validar_numero('cantidad de comentarios')
    
    elif opcion == 3: # Actualizar el nombre de usuario
        
        usuarios_dict = cargar_usuarios('usuarios.json')
        nuevo_usuario = validez.validar_usuario(usuarios_dict)
        posteos[id_post][5] = nuevo_usuario
    
    elif opcion == 4: #Actualizar todo
        usuarios_dict = cargar_usuarios('usuarios.json')
        
        nuevo_likes = validez.validar_numero('cantidad de likes')
        nuevo_comentarios = validez.validar_numero('cantidad de comentarios')
        nuevo_usuario = validez.validar_usuario(usuarios_dict)
        posteos[id_post][3] = nuevo_likes
        posteos[id_post][4] = nuevo_comentarios
        posteos[id_post][5] = nuevo_usuario
    
    guardar_publicaciones(posteos, nombre_archivo)
    print("Publicación actualizada exitosamente.")

#Función leer publicación
def leer_publicaciones(nombre_archivo):
    posteos = cargar_publicaciones(nombre_archivo)
    
    print("1. Ver una publicación específica")
    print("2. Ver todas las publicaciones")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_post = input("Ingrese el ID de la publicación que desea ver: ").zfill(4)
        encontrado = False
        for posteo in posteos:
            if posteo[0] == id_post:
                print("ID:", posteo[0], "Fecha:", posteo[1], "Likes:", posteo[2], "Comentarios:", posteo[3])
                encontrado = True
                break
        if not encontrado:
            print("ID de publicación no encontrado.")
    
    elif opcion == "2":
        imprimir_posteos(posteos)
        input('Oprima enter para continuar ')
    else:
        print("Opción no válida.")
        
#Función imprimir publicaciones
def imprimir_posteos(posteos):
    '''Muestra los valores de la matriz en forma de tabla'''
    print("Publicaciones disponibles:")
    
    diseño.publicaciones.parte_superior()
    diseño.publicaciones.encabezado()
    
    for i in range(1, len(posteos)):  # Comienza desde el índice 1
        if i == len(posteos) - 1:
            diseño.publicaciones.parte_conectiva()
            diseño.publicaciones.mostrar(*posteos[i])
        else:   
            diseño.publicaciones.parte_conectiva()
            diseño.publicaciones.mostrar(*posteos[i])
            
    diseño.publicaciones.parte_inferior()
