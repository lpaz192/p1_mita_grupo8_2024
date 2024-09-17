'''
#IMPORTANTE:
#pip install instaloader
#y no carguen varios perfiles de una porque sino tenes que esperar porque colapsa
#no pongan perfiles grandes



import instaloader, re
import validez

L = instaloader.Instaloader()

def cargar_perfil_instaloader(username):
    try:
        perfil = instaloader.Profile.from_username(L.context, username) #se encuentra el perfil real, si perfil real
        #por las dudas busquen un perfil publico con pocos seguidores porque sino tardar mucho en agarrar los queries
        total_likes = 0

        #cantidad_posts = perfil.mediacount
        
        for post in perfil.get_posts():
            total_likes += post.likes
        
        return {
            "Usuario": perfil.username,
            "Seguidores": perfil.followers,
            "Seguidos": perfil.followees,
            "Likes": total_likes,  # aca agarro todos los likes sumados peroooo estaria bueno que veamos la forma de separarlos para las metricas. Estoy con eso ahora
            #"Cantidad_de_posts": cantidad_posts,
            #con las metricas seria likes likes total / cantidad de posts = media de likes / seguidores * 100 = porcentaje de alcance 
            "Correo": ""  #vacio por lo que dije antes
        }
    except Exception as e:
        print(f"Error al cargar el perfil {username}: {e}")
        return None

def agregar_con_instaloader():
    username = input("Ingrese el nombre de usuario de Instagram: ")
    perfil = cargar_perfil_instaloader(username)
    if perfil:
        return [perfil['Usuario'], perfil['Seguidores'], perfil['Seguidos'], perfil['Likes'], perfil['Correo']]
    else:
        print(f"No se pudo cargar el perfil de {username}")
        return None

def agregar(eleccion):
    lista, aux = [], ""
    if eleccion == 2:  # Hashtags
        #hay que ver la documentacion para ver si podemos agarrar las veces compartidas
        # relleno(?) si... relleno 
        x = ["Hashtag: ", "Cantidad de posteos: ", "Veces compartidos: ", "Likes: "]
        comparacion = lambda palabra: re.match(r"^#[a-zA-Z0-9-_.]{1,20}", palabra)
        for col in range(4):
            if col == 0:
                aux = input(f"Ingrese {x[col]}")
                while comparacion(aux) is None:
                    aux = input("Ingrese un Hashtag valido: ")
                lista.append(aux)
            else:
                lista.append(input(f"Ingrese {x[col]}"))
    return lista

def leer(matriz):
    if matriz:
        if matriz[0]: 
            encabezado = matriz[0]
            if encabezado[0] == "Usuario":
                # Imprimir encabezado
                print(f"| {'Usuario':<20} | {'Seguidores':<12} | {'Seguidos':<12} | {'Likes':<10} | {'Correo':<30} |")
                print("-" * 80)
                # Imprimir datos
                for fila in matriz[1:]:
                    print(f"| {fila[0]:<20} | {fila[1]:<12} | {fila[2]:<12} | {fila[3]:<10} | {fila[4]:<30} |")
            else:
                # Imprimir encabezado
                print(f"| {'Hashtag':<20} | {'Cantidad de posteos':<20} | {'Veces compartido':<20} | {'Likes':<10} |")
                print("-" * 70)
                # Imprimir datos
                for fila in matriz:
                    print(f"| {fila[0]:<20} | {fila[1]:<20} | {fila[2]:<20} | {fila[3]:<10} |")
    else:
        print("La matriz está vacía.")

def seleccionar_usuario(matriz):
    aux = -1
    while aux < 0 or aux >= len(matriz):
        print("¿Qué usuario deseas modificar?\nIngrese el número de la fila: ", end="")
        aux = int(input())  # Solicita qué usuario se quiere modificar
        if aux < 0 or aux >= len(matriz):
            print("Usuario no encontrado")
    return aux

def seleccionar_elemento_usuario():
    modif = -1
    while modif < 0 or modif > 4:
        print("¿Qué elemento deseas modificar?\n0. Usuario\n1. Seguidores\n2. Seguidos\n3. Likes\n4. Correo")
        modif = int(input("Seleccione: "))  # Solicita qué elemento se quiere modificar
        if modif < 0 or modif > 4:
            print("Por favor, ingrese un valor dentro del rango solicitado")
    return modif

def actualizar(modif):
    if modif == 0:
        comparacion = lambda palabra: re.match(r"[a-zA-Z-_.]{1,20}", palabra)
        aux = input("Ingrese el nuevo usuario: ")
        while comparacion(aux) is None:
            aux = input("Ingrese un nuevo nombre valido: ")
        return aux
    elif modif == 1:
        aux = int(input("Ingrese la nueva cantidad de seguidores: "))
        return aux
    elif modif == 2:
        aux = int(input("Ingrese la nueva cantidad de seguidos: "))
        return aux
    elif modif == 3:
        aux = int(input("Ingrese la nueva cantidad de likes: "))
        return aux
    else:
        aux = input("Ingrese el nuevo correo: ")
        while validez.validar_mail(aux) is None:
            aux = input("Ingrese un mail valido: ")
        return aux

def eliminar(matriz):
    print()

'''

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
def seleccionar_hashtag(matriz):
    while True:
            print("\n---Hashtags---")
            leer_usuario(matriz)
            aux  = int(input("Seleccione un usuario con el numero de id: "))
            if  aux>=0 and aux<=len(matriz[0]):
                return aux
            input("Dato invalido")

def selccionar_elemento_hashtag(hashtag,matriz): 
    while True:
        print(f"\n---Hashtag  {matriz[hashtag][0]}---")
        print(f"1. Cantidad de posteos: {matriz[hashtag][1]}")
        print(f"2. Veces compartido: {matriz[hashtag][2]}")
        print(f"3. Likes: {matriz[hashtag][3]}")
        aux = int(input("Seleccione un elemento: "))
        if aux >0 and aux<=len(matriz[hashtag]):
            return aux
        input("Dato invalido")    


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
    for id_usuario, datos_usuario in usuarios.items():
        if id_usuario==1:
            diseño.parte_superior()
            diseño.encabezado_usuarios()
            diseño.parte_conectiva()
            diseño.mostrar_usuario(id_usuario,datos_usuario)
            diseño.parte_conectiva()
            
        elif max(usuarios.keys())==id_usuario:
            diseño.mostrar_usuario(id_usuario, datos_usuario)
            diseño.parte_inferior()
        else:
            diseño.mostrar_usuario(id_usuario, datos_usuario)
            diseño.parte_conectiva()
    input('Oprima enter para continuar ')

def actualizar_usuario(opcion_usuario,elemento_elegido,usuarios):    #Actualizar
    if elemento_elegido == 1:
        usuarios[opcion_usuario]['Usuario']=validez.validar_usuario()

    elif elemento_elegido == 2:
        usuarios[opcion_usuario]['Seguidores'] = validez.validar_numero('seguidores')
        
    elif elemento_elegido == 3:
        usuarios[opcion_usuario]['Seguidos'] = validez.validar_numero('seguidos')
    
    elif elemento_elegido == 4:
        usuarios[opcion_usuario]['Likes'] = validez.validar_numero('likes')
    else:
        usuarios[opcion_usuario]['Correo'] = validez.validar_mail()

def eliminar_usuario(id,usuarios): #Eliminar
    usuarios.pop(id)

#Funciones CRUD Hashtags
def leer_hashtag(hashtag):         #Leer
    for fil in hashtag:
        if hashtag[0]==fil:
            diseño.parte_superior_hashtag()
            diseño.encabezado_hashtags()
            diseño.parte_conectiva_hashtag()
            
            diseño.mostrar_hashtag(fil)
            diseño.parte_conectiva_hashtag()
        elif hashtag[len(hashtag)-1]==fil:
            diseño.mostrar_hashtag(fil)
            diseño.parte_inferior_hashtag()
        else:
            diseño.mostrar_hashtag(fil)
            diseño.parte_conectiva_hashtag()
    input()


#Funciones CRUD Posteos
def agregar_publicacion(posteos):
    id_post = input("Ingrese el ID de la publicación: ").zfill(3)

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
    id_post = input("Ingrese el ID de la publicación a eliminar: ")

    for i in range(len(posteos)):
        if posteos[i][0] == id_post:
            del posteos[i]
            print("Publicación eliminada exitosamente.")
            return #aca termina la funcion
    
    #pero si no lo encuentra no hace return y tira la alerta
    print("ID de publicación no encontrado.")

def actualizar_publicacion(posteos):
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
        print("\n---Lista de Publicaciones---")
        for posteo in posteos:
            print("ID:", posteo[0], "Fecha:", posteo[1], "Likes:", posteo[2], "Comentarios:", posteo[3])
    else:
        print("Opción no válida.")
