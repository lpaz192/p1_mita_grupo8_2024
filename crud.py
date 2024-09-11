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
        
        for post in perfil.get_posts():
            total_likes += post.likes
        
        return {
            "Usuario": perfil.username,
            "Seguidores": perfil.followers,
            "Seguidos": perfil.followees,
            "Likes": total_likes,  # aca agarro todos los likes sumados peroooo estaria bueno que veamos la forma de separarlos para las metricas
            #con las metricas seria likes por cada publicacion / seguidores y eso se suma y promedio 
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
#Funciones secundarias
import json,validez,re

def seleccionar_usuario(usuarios):
    opcion=0
    while opcion==0 or opcion>4:
        if  opcion==0 or opcion>4:
            print("\n---Usuarios---")
            leer(1,usuarios)
            opcion = int(input("Seleccione un usuario con el numero de id: "))
        else: 
            print("Opcion no valida")    
    return opcion

def seleccionar_usuario_elemento(id,usuarios):
    opcion=0
    while opcion==0 or opcion>4:
        if  opcion==0 or opcion>4:
            print(f"\n---Usuario  {usuarios[id][0]}---")
            print(f"1. Seguidores: {usuarios[id][1]}")
            print(f"2. Seguidos: {usuarios[id][2]}")
            print(f"3. Likes: {usuarios[id][3]}")
            print(f"4. Correos: {usuarios[id][4]}")
            opcion = int(input("Seleccione un elemento: "))
        else: 
            print("Opcion no valida")    
    return opcion

# Funciones principales del CRUD
def agregar(opcion):
    lista,aux=[],""
    if opcion==1:
        comparacion= lambda nombre:re.match(r"^[a-zA-Z_]{2,20}",nombre)
        x =["Usuario: ","Seguidores: ","Seguidos: ","Likes: ","Correo: "]
        for col in range(5):
            if col == 0:
                aux=input(f"Ingrese {x[col]}")
                while comparacion(aux)==None:
                    aux=input("Ingrese un nombre valido: ")
                lista.append(aux)
            elif col == 4:
                aux=input(f"Ingrese {x[col]}")
                while validez.validar_mail(aux)==None:
                    aux=input("Ingrese un mail valido: ")
                lista.append(aux)  
            else:   
                lista.append(input(f"Ingrese {x[col]}"))
    else:
        x =["Hashtag: ","Cantidad de posteos: ","Veces compartidos: ","Likes: "]
        comparacion= lambda palabra:re.match(r"^#[a-zA-Z0-9-_.]{1,20}",palabra)
        for col in range(4):  
            if col == 0:
                aux=input(f"Ingrese {x[col]}")
                while comparacion(aux)==None:
                    aux=input("Ingrese un Hashtag valido: ")
                lista.append(aux)
            else: 
                lista.append(input(f"Ingrese {x[col]}"))
  
    return lista


def leer(opcion,matriz):
    if opcion==1:
        for fil in range(len(matriz)):
            print()
            for col in range(len(matriz[0])):
                print(f"|{matriz[fil][col]:^12}|",end="")
        print()
    elif opcion==2:
        for fil in range(len(matriz)):
            print()
            for col in range(len(matriz[0])):
                print(f"|{matriz[fil][col]:^12}|",end="")
        print()
    else:
        for fil in range(len(matriz)):
            print()
            for col in range(len(matriz[0])):
                print(f"|{matriz[fil][col]:^12}|",end="")
        input("\n")

    return 0

def actualizar(tipo_matriz,opcion):
    
    if tipo_matriz==1:

        if opcion == 0:
            comparacion= lambda palabra:re.match(r"[a-zA-Z-_.]{3,20}",palabra)
            aux=input("Ingrese el nuevo usuario (entre 3 y 20 caracteres): ")
            while comparacion(aux)==None:
                aux=input("Ingrese un nuevo usuario valido: ")
            return aux
        
        elif opcion ==1:
            aux=int(input("Ingrese el nueva cantidad seguidores: "))
            return aux
        elif opcion == 2:
            aux=int(input("Ingrese la nueva cantidad de seguidos: "))
            return aux
        elif opcion == 3:
            aux=int(input("Ingrese la nueva cantidad de likes: "))
            return aux
        else:
            aux=input("Ingrese el nuevo correo: ")
            while validez.validar_mail(aux)==None:
                aux=input("Ingrese un mail valido: ")
            return aux
        
    elif tipo_matriz == 1:                              # 
        opcion_hashtag = seleccionar_hashtag(main.hashtags)
        opcion_hashtag_elemento = seleccionar_hashtag_elemento(opcion_hashtag,main.hashtags)
        if opcion_hashtag_elemento == 0:
            main.hashtags[opcion_hashtag][opcion_hashtag_elemento]=input("Ingrese una nueva cantidad de posteos: ")
        
        elif opcion_hashtag_elemento ==1:
            main.hashtag[opcion_hashtag][opcion_hashtag_elemento]=int(input("Ingrese el nueva cantidad de veces compartido: "))
        
        elif opcion_hashtag_elemento == 2:
            main.hashtag[opcion_hashtag][opcion_hashtag_elemento]=int(input("Ingrese la nueva cantidad de likes: "))
        return
    """
    if modif == 0:
        comparacion= lambda palabra:re.match(r"[a-zA-Z-_.]{1,20}",palabra)
        aux=input("Ingrese el nuevo usuario: ")
        while comparacion(aux)==None:
            aux=input("Ingrese un nuevo nombre valido: ")
        return aux
    elif modif ==1:
        aux=int(input("Ingrese el nueva cantidad seguidores: "))
        return aux
    elif modif==2:
        aux=int(input("Ingrese la nueva cantidad de seguidos: "))
        return aux
    elif modif==3:
        aux=int(input("Ingrese la nueva cantidad de likes: "))
        return aux 
    else:
        aux=input("Ingrese el nuevo correo: ")
        while validez.validar_mail(aux)==None:
            aux=input("Ingrese un mail valido: ")
        return aux
        """

def eliminar(matriz):
    print()