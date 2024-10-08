import diseño, validez
#Funciones CRUD Publicaciones
def imprimir_posteos(posteos):
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

def agregar_publicacion(posteos, usuarios,hashtag):
    id_post = validez.validar_numero('nuevo id',1,4)
    #para que no hayan dos con el mismo id
    for posteo in posteos:
        if posteo[0] == id_post:
            print("Error: Ya existe una publicación con este ID.")
            return

    while True:
        fecha_publicacion = input("Ingrese la fecha de la publicación (DD-MM-YYYY): ")
        if validez.validar_fecha(fecha_publicacion):
            break
        else:
            print("Fecha inválida, por favor ingrese una fecha en formato válido (DD-MM-YYYY).")
    
    
    likes = validez.validar_numero('likes')
    comentarios = validez.validar_numero('cantidad de comentarios')

    print('--- Seleccion de usuario ---')
    print('1. Para ver la tabla de usuarios')
    print('2. Para selecionar usuario')
    opcion= validez.obtener_opcion([1,2])
        
    print("Para seleccionar el usuario que realizo la publicacion")
    print("Por favor, ingrese el numero de id del usuario o selecciones -1 para ver la tabla: ", end="")
    
    id_usuario = validez.validar_id(usuarios)

    usuario = usuarios[id_usuario]['Usuario']
    
    print("Ingrese el hashtag que usa la publicacion: ", end=" ")
    hashtag=validez.hashtag.hashtag_existente(hashtag)

    posteos.append([id_post, fecha_publicacion, likes, comentarios, id_usuario, usuario, hashtag])
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

def actualizar_publicacion(posteos, usuarios):

    imprimir_posteos(posteos)

    id_post = input("Ingrese el ID de la publicación a actualizar: ").zfill(3)
    
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
    print("4. ID de Usuario")
    print("5. Modificar toda la publicación")
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
        # Actualizar el ID de usuario
        id_usuario = validez.validar_id(usuarios)
        # Verificar que el ID de usuario existe en el diccionario
        if id_usuario in usuarios:
            usuario = usuarios[id_usuario]['Usuario']
            posteos[index][5] = usuario
        else:
            print("ID de usuario no encontrado en el diccionario.")
            return
        
    elif opcion == 5:
        nueva_fecha = input("Ingrese la nueva fecha de la publicación (YYYY-MM-DD): ")

        #si la validacion de la fecha no es True o sea no esta bien
        if not validez.validar_fecha(nueva_fecha):
            print("Fecha inválida.")
            return #para todo y volveria al principio
        nuevo_likes = int(input("Ingrese la nueva cantidad de likes: "))
        nuevo_comentarios = int(input("Ingrese la nueva cantidad de comentarios: "))
        id_usuario = input("Ingrese el ID del usuario: ")
        if int(id_usuario) in usuarios:
            usuario = usuarios[int(id_usuario)]
            posteos[index] = [id_post, nueva_fecha, nuevo_likes, nuevo_comentarios, id_usuario, usuario]
        else:
            print("ID de usuario no encontrado en el diccionario.")
            return

    else:
        print("Opción no válida.")
        return

    print("Publicación actualizada exitosamente.")

def leer_publicaciones(posteos):
    print("1. Ver una publicación específica")
    print("2. Ver todas las publicaciones")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_post = input("Ingrese el ID de la publicación que desea ver: ").zfill(3)
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
