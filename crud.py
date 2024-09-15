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

#Funciones secundarias de usarios
def seleccionar_usuario(matriz):
    while True:
        print("\n---Usuarios---")
        leer_usuario(matriz)
        aux = int(input("Seleccione un usuario con el numero de id: "))
        if  aux>=0 and aux<=len(matriz[0]):
            return aux
        input("Dato invalido")

def seleccionar_elemento_usuairos(id,matriz):
    while True:
        print(f"\n---Usuario con ID {matriz[id][0]}---")
        print(f"1. Usuario  {matriz[id][1]}")
        print(f"2. Seguidores: {matriz[id][2]}")
        print(f"3. Seguidos: {matriz[id][3]}")
        print(f"4. Likes: {matriz[id][4]}")
        print(f"5. Correos: {matriz[id][5]}")
        aux = int(input("Seleccione un elemento: "))
        if aux >0 and aux<=len(matriz[id]):
            return aux
        input("Dato invalido")

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
def agregar_usuario(usuarios_dict):      #Agregar
    #Solicitar información
    nuevo_id= input()
    nuevo_nombre= input()
    nuevo_seguidores= input()
    nuevo_seguido= input()
    nuevo_likes= input()
    nuevo_correo= input()
    
    #Agregar usuario
    usuarios_dict[nuevo_id] = {
        'Usuario':nuevo_nombre,
        'Seguidores':nuevo_seguidores,
        'Seguidos':nuevo_seguido,
        'Likes':nuevo_likes,
        'Correo':nuevo_correo
    }
    """
    col=0
    while col<len(usuarios[0]):
        if col == 1:
            aux=input(f"Ingrese {x[col]}:")
            if validez.validar_usuario(aux)==None:
                aux=input(f"Ingrese un {x[col]} valido: ")
            else:
                lista.append(aux)
                col+=1
        elif col == 5:
            aux=input(f"Ingrese {x[col]}:")
            while validez.validar_mail(aux)==None:
                aux=input("Ingrese un mail valido: ")
            lista.append(aux)  
            col+=1
        else:   
            lista.append(int(input(f"Ingrese {x[col]}: ")))
            col+=1
    usuarios[len(usuarios)-1].extend(lista)
"""
def leer_usuario(usuarios):         #Leer
    for fil in usuarios:
        if usuarios[0]==fil:
            diseño.parte_superior()
            diseño.mostrar_usuario(fil)
            diseño.parte_conectiva()
        elif usuarios[len(usuarios)-1]==fil:
            diseño.mostrar_usuario(fil)
            diseño.parte_inferior()
        else:
            diseño.mostrar_usuario(fil)
            diseño.parte_conectiva()
    input()
    

def actualizar_usuario(opcion_usuario,opcion_elemento,usuarios):    #Actualizar
    if opcion_elemento == 0:
        aux=input("Ingrese el nuevo usuario (entre 3 y 20 caracteres): ")
        while validez.validar_usuario(aux)==None:
            aux=input("Ingrese un nuevo usuario valido: ")
    
    elif opcion_elemento ==1:
        aux=int(input("Ingrese el nueva cantidad seguidores: "))
        
    elif opcion_elemento == 2:
        aux=int(input("Ingrese la nueva cantidad de seguidos: "))
        
    elif opcion_elemento == 3:
        aux=int(input("Ingrese la nueva cantidad de likes: "))
       
    else:
        aux=input("Ingrese el nuevo correo: ")
        while validez.validar_mail(aux)==None:
            aux=input("Ingrese un mail valido: ")
    usuarios[opcion_usuario][opcion_elemento]=aux

def eliminar_usuario(id,usuarios):
    usuarios.pop(id)

#Funciones CRUD Hashtags
def leer_hashtag(hashtag):         #Leer
    for fil in hashtag:
        if hashtag[0]==fil:
            diseño.parte_superior_hashtag()
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
