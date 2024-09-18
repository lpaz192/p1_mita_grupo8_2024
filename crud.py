"""  Notas  """

import json,validez,re,diseño

#Funciones labmda
nuevo_id=lambda usuarios: max(usuarios.keys())+1 if usuarios else 1

#Funciones secundarias de usarios
def seleccionar_elemento_usuairos(id,usuario):
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


#Funciones CRUD Usuarios
def agregar_usuario(usuarios):      #Agregar
    #Agregar usuario
    usuarios[nuevo_id(usuarios)] = {
        'Usuario':validez.validar_usuario(),
        'Seguidores':validez.validar_numero('seguidores'),
        'Seguidos':validez.validar_numero('seguidos'),
        'Likes':validez.validar_numero('likes'),
        'Correo':validez.validar_mail()
    }
   
def leer_usuario(usuarios):         #Leer
    diseño.parte_superior()
    diseño.encabezado_usuarios()
    for id_usuario, datos_usuario in usuarios.items():
        if id_usuario==min(usuarios.keys()):
            diseño.parte_conectiva()
            diseño.mostrar_usuario(id_usuario,datos_usuario)
        elif max(usuarios.keys())==id_usuario:
            diseño.parte_conectiva()
            diseño.mostrar_usuario(id_usuario, datos_usuario)
        else:
            diseño.parte_conectiva()
            diseño.mostrar_usuario(id_usuario, datos_usuario)
    diseño.parte_inferior()
    input('Oprima enter para continuar ')

def actualizar_usuario(opcion_usuario,elemento_elegido,usuarios):    #Actualizar
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

def eliminar_usuario(id,usuarios): #Eliminar
    usuarios.pop(id)

#Funciones CRUD Hashtags
def agregar_hashtag(hashtag_dict):      #Agregar
    #Agregar hashtag
    nuevo_hashtag= validez.hashtag_no_repetido(hashtag_dict)
    hashtag_dict[nuevo_hashtag] = {
        'Cant. posteos'   :validez.validar_numero('cantidad de posteos',1,10),
        'Veces compartido':validez.validar_numero('veces compartido',1,10),
        'Likes'           :validez.validar_numero('likes',1,10),
    }

def leer_hashtag(hashtags_dict):
    hashtag = list(hashtags_dict.keys())
    diseño.parte_superior_hashtag()
    diseño.encabezado_hashtags()
    for i in range(len(hashtag)):
        if i == 0:
            diseño.parte_conectiva_hashtag()
            diseño.mostrar_hashtag(hashtag[i], hashtags_dict[hashtag[i]])
        elif i == len(hashtag)-1:
            diseño.parte_conectiva_hashtag()
            diseño.mostrar_hashtag(hashtag[i], hashtags_dict[hashtag[i]])
        else:
            diseño.parte_conectiva_hashtag()
            diseño.mostrar_hashtag(hashtag[i], hashtags_dict[hashtag[i]])
    diseño.parte_inferior_hashtag()
    input('Oprima enter para continuar ')

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

#Funciones CRUD Posteos
def imprimir_posteos(posteos):
    print("Publicaciones disponibles:")
    
    diseño.parte_superior_publicacion()
    diseño.encabezado_publicacion()
    
    for i in range(1, len(posteos)):  # Comienza desde el índice 1
        if i == len(posteos) - 1:
            diseño.mostrar_publicacion(*posteos[i])
        else:
            diseño.parte_conectiva_publicacion()
            diseño.mostrar_publicacion(*posteos[i])
    diseño.parte_inferior_publicacion()

def agregar_publicacion(posteos):
    id_post = input("Ingrese el ID de la publicación: ").zfill(3)

    #para que no hayan dos con el mismo id
    for posteo in posteos:
        if posteo[0] == id_post:
            print("Error: Ya existe una publicación con este ID.")
            return

    while True:
        fecha_publicacion = input("Ingrese la fecha de la publicación (YYYY-MM-DD): ")
        if validez.validar_fecha(fecha_publicacion):
            break
        else:
            print("Fecha inválida, por favor ingrese una fecha en formato válido (YYYY-MM-DD).")
    
    
    likes = int(input("Ingrese la cantidad de likes: "))
    comentarios = int(input("Ingrese la cantidad de comentarios: "))
    
    posteos.append([id_post, fecha_publicacion, likes, comentarios])
    print("Publicación agregada exitosamente.")

def eliminar_publicacion(posteos):

    imprimir_posteos(posteos)

    id_post = input("Ingrese el ID de la publicación a eliminar: ").zfill(3)

    for i in range(len(posteos)):
        if posteos[i][0] == id_post:
            del posteos[i]
            print("Publicación eliminada exitosamente.")
            return #aca termina la funcion
    
    #pero si no lo encuentra no hace return y tira la alerta
    print("ID de publicación no encontrado.")

def actualizar_publicacion(posteos):

    imprimir_posteos(posteos)

    id_post = input("Ingrese el ID de la publicación a actualizar: ")
    
    index = -1
    for i in range(len(posteos)):
        if posteos[i][0] == id_post:
            index = i
            break
    if index == -1:
        print("ID de publicación no encontrado.")
        return

    print("Seleccione el campo que desea actualizar:")
    print("1. Fecha de publicación")
    print("2. Likes")
    print("3. Comentarios")
    print("4. Modificar toda la publicación")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        fecha_publicacion = input("Ingrese la nueva fecha de la publicación (YYYY-MM-DD): ")
        if validez.validar_fecha(fecha_publicacion):
            posteos[index][1] = fecha_publicacion
        else:
            print("Fecha inválida.")
            return

    elif opcion == 2:
        posteos[index][2] = int(input("Ingrese la nueva cantidad de likes: "))

    elif opcion == 3:
        posteos[index][3] = int(input("Ingrese la nueva cantidad de comentarios: "))

    elif opcion == 4:
        nueva_fecha = input("Ingrese la nueva fecha de la publicación (YYYY-MM-DD): ")

        #si la validacion de la fecha no es True o sea no esta bien
        if not validez.validar_fecha(nueva_fecha):
            print("Fecha inválida.")
            return #para todo y volveria al principio
        nuevo_likes = int(input("Ingrese la nueva cantidad de likes: "))
        nuevo_comentarios = int(input("Ingrese la nueva cantidad de comentarios: "))
        posteos[index] = [id_post, nueva_fecha, nuevo_likes, nuevo_comentarios]

    else:
        print("Opción no válida.")
        return

    print("Publicación actualizada exitosamente.")

def leer_publicaciones(posteos):
    print("1. Ver una publicación específica")
    print("2. Ver todas las publicaciones")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_post = input("Ingrese el ID de la publicación que desea ver: ")
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
    else:
        print("Opción no válida.")

#ORDENAMIENTO PUBLICACIONES

def ordenar_publicaciones(posteos):
    print("\n--- Ordenar Publicaciones ---")
    print("1. Ordenar por ID")
    print("2. Ordenar por cantidad de likes")
    print("-1. Volver al menú principal")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        ordenar_por_id(posteos)
    elif opcion == 2:
        ordenar_por_likes(posteos)
    elif opcion == -1:
        return
    else:
        print("Opción no válida.")


def ordenar_por_id(posteos):
    print("Elija el orden de clasificación por ID:")
    print("1. De menor a mayor")
    print("2. De mayor a menor")
    opcion = int(input("Seleccione una opción: "))

    encabezado = posteos[0]  
    datos = posteos[1:] 


    if opcion == 1:
        datos.sort(key=lambda x: int(x[0])) 
    elif opcion == 2:
        datos.sort(key=lambda x: int(x[0]), reverse=True)
    else:
        print("Opción no válida.")
        return

    posteos = [encabezado] + datos

    imprimir_posteos(posteos)  

def ordenar_por_likes(posteos):
    print("Elija el orden de clasificación por cantidad de likes:")
    print("1. De menor a mayor")
    print("2. De mayor a menor")
    opcion = int(input("Seleccione una opción: "))

    encabezado = posteos[0]
    datos = posteos[1:]

    for post in datos:
        post[2] = int(post[2])

    if opcion == 1:
        datos.sort(key=lambda x: x[2]) 
    elif opcion == 2:
        datos.sort(key=lambda x: x[2], reverse=True)
    else:
        print("Opción no válida.")
        return

    posteos = [encabezado] + datos

    imprimir_posteos(posteos)  
