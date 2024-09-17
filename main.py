'''
import crud, json

# Funciones
def eleccion():
    matriz_elegida = 0
    while matriz_elegida != 1 and matriz_elegida != 2:
        print("¿En qué matriz deseas realizar esta operación?\n1. Usuarios\n2. Hashtags")
        matriz_elegida = int(input("Seleccione: "))  # 1 matriz de usuario, 2 matriz de hashtags
        if matriz_elegida != 1 and matriz_elegida != 2:
            print("Por favor, ingrese un número dentro de los solicitados")
    return matriz_elegida


#Se abre un json en donde tiene adentro dos secciones que antes eran matrices
#Ahora las matrices son diccionarios
def cargar_datos():
    try:
        with open('datos.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"usuarios": [], "hashtags": []}
    return data

def guardar_datos(data):
    with open('datos.json', 'w') as file:
        json.dump(data, file, indent=4)

data = cargar_datos()

menu = 0
while menu != -1:
    print("1. Para agregar")
    print("2. Para leer")
    print("3. Para actualizar")
    print("4. Para eliminar")
    print("5. Para ordenar")
    print("-1. Para cancelar")
    menu = int(input("Ingrese un número: "))

    if menu == 1:  
        matriz_elegida = eleccion()
        if matriz_elegida == 1:
            nuevo_usuario = crud.agregar_con_instaloader()
            if nuevo_usuario:
                data["usuarios"].append(nuevo_usuario)
                guardar_datos(data)
        else:
            nuevo_hashtag = crud.agregar(matriz_elegida)
            data["hashtags"].append(nuevo_hashtag)
            guardar_datos(data)

    elif menu == 2:  # Leer
        seleccion = int(input("¿Qué matriz deseas visualizar?\n1. Para usuarios\n2. Para hashtags\n"))
        while seleccion <= 0 or seleccion > 2:
            print("El número ingresado no está dentro de los números solicitados\nPor favor, ingrese el número nuevamente: ", end="")
            seleccion = int(input())
        if seleccion == 1:
            crud.leer(data["usuarios"])
        else:
            crud.leer(data["hashtags"])

    elif menu == 3:  
        #aca estaria bueno agregar los mails porque no se pueden tener de instaloader
        if eleccion() == 1:  
            usuario_modif = crud.seleccionar_usuario(data["usuarios"])
            usuario_elemento_modif = crud.seleccionar_elemento_usuario()  #cambia lo que quieras de un usuario
            data["usuarios"][usuario_modif][usuario_elemento_modif] = crud.actualizar(usuario_elemento_modif)  #se agregan
            guardar_datos(data)
        else:
            #actualizar hashtags????
            pass

    elif menu == 4:  #eliminar
        if eleccion() == 1:
            usuario_eliminar = crud.seleccionar_usuario(data["usuarios"])
            data["usuarios"].pop(usuario_eliminar)
            guardar_datos(data)
        else:
            #eliminar hashtags?????
            pass
'''
'''
#por si no quieren hacerlo manual esto hace el paso de matriz a diccionario
keys = usuario[0]
usuarios_dict = [dict(zip(keys, row)) for row in usuario[1:]]
'''

""" Notas: 

"""
from datetime import datetime
import random
import crud, metricas, json, validez
from diseño import __menu__, crud_hashtags, crud_usuarios, estadisticas, crud_publicacion, ordenamiento  

#Funciones
"""
def eleccion():
    matriz_elegida=0
    while matriz_elegida!=1 and matriz_elegida!=2:
        print("En que matriz deseas realizar esta operación\n1. Usuarios\n2. Hashtags")
        matriz_elegida=int(input("Seleccione: "))                          #1 matriz de usuario   2. matriz de posteo
        if matriz_elegida !=1 and matriz_elegida !=2:
            print("Por favor ingrese un numero dentro de los solicitados")
        else:     
            return matriz_elegida
            """
def ordenamiento(matriz):
    matriz.sort()
    return matriz

#Matrices
# 'ID'  'Usuario' 'Seguidores'  'Seguidos' 'Likes' 'Correo'  
usuario = [[1, "Martintin",     234,        200,         100,   "martincho@outlook.com"     ],
           [2, "Diego.lopez",  2000,        800,        1000,   "diegolopez@gmail.com"      ], 
           [3, "carlitaa",     5000,        500,        8000,   "carlaguilar@gmail.com"     ],   
           [4, "Marcediaz",     200,       1000,         100,   "marcelodiaz12@hotmail.com"]
           ]
  
usuarios_dict={                #Crear diccionario
    fil[0]:{
        'Usuario':fil[1],
        'Seguidores':fil[2],   #Una tupla con el id del usuario y los datos del usuario
        'Seguidos':fil[3],     #Dentro de los datos del usuario son tuplas entre la infromacion y su 'etiqueta'
        'Likes':fil[4],
        'Correo':fil[5]
    }for fil in usuario
}

hashtags = [["#Feriado",   400 ,  2000 ,  4000],   # 'Hashtag'  'Cant posteos'  'Veces compartido'  'Likes' 
            ["#UADELabs",  2000,  10000,  50000]
            ]  
                                    
hashtags_dict={
    fil[0]:{
        'Cant. posteos':fil[1],
        'Veces compartido':fil[2],
        'Likes':fil[3]
    }for fil in hashtags
}
posteos = [["ID Post", "Fecha de publicación", "Cantidad de likes", "Cantidad de comentarios"]]

for i in range(1,11): #se crean 10 publicaciones con numeros aleatorios
    id_post = str(i).zfill(3)
    while True:
        fecha_publicacion = datetime.now().strftime('%Y-%m-%d')
        if validez.validar_fecha(fecha_publicacion):
            break
    likes = random.randint(0, 1000)
    comentarios = random.randint(0, 1000)
    posteos.append([id_post, fecha_publicacion, likes, comentarios])


#Menu principal
menu=0
while menu!=-1:
    menu = __menu__()

    if menu==1:                  #----  Usuario     ----
        opcion_crud=crud_usuarios()   
        
        if opcion_crud==1:                   #Agregar
            crud.agregar_usuario(usuarios_dict)

        elif opcion_crud==2:                 #Eliminar
            crud.leer_usuario(usuarios_dict)
            print('Para eliminar')
            usuario_fila = validez.validar_id(usuarios_dict)
            crud.eliminar_usuario(usuario_fila,usuarios_dict)
        
        elif opcion_crud==3:                 #Actualizar
            crud.leer_usuario(usuarios_dict)  #Se muestra la matriz
            #Se selecciona el usuario a modificar
            opcion_usuario = validez.validar_id(usuarios_dict)   
            
            #Se selecciona el elemento a modificar
            opcion_usuario_elemento = crud.seleccionar_elemento_usuairos(opcion_usuario,usuarios_dict) 
            
            #Se modifica el elemento
            crud.actualizar_usuario(opcion_usuario,opcion_usuario_elemento,usuarios_dict)
        
        elif opcion_crud == 4:               #Leer
            crud.leer_usuario(usuarios_dict)

    elif menu==2:                #----Hashtag     ----
        opcion_crud = crud_hashtags()
        if opcion_crud==1:                #Agregar
            crud.agregar_hashtag(hashtags_dict)

        elif opcion_crud==2:              #Eliminar
            crud.leer_hashtag(hashtags_dict)
            print("Ingrese el hashtag que desee eliminar",end="")
            hashtag_fila= validez.hashtag_existente(hashtags_dict)
            crud.eliminar_hashtag(hashtag_fila,hashtags_dict)

        elif opcion_crud==3:              #Actualizar
            crud.leer_hashtag(hashtags_dict)
            print('Ingres el hashtag que desea modificar: ',end="")
            opcion_hashtag = validez.hashtag_existente(hashtags_dict)
            opcion_hashtag_elemento = crud.selccionar_elemento_hashtag(opcion_hashtag,hashtags_dict)
            crud.actualizar_hashtag(opcion_hashtag,opcion_hashtag_elemento,hashtags_dict)

        elif opcion_crud == 4:                        #Leer
            crud.leer_hashtag(hashtags_dict)
        
    elif menu==3:                #----Publicacion ----
        opcion=crud_publicacion()
        if opcion == 1:
            crud.agregar_publicacion(posteos)
        elif opcion == 2:
            crud.eliminar_publicacion(posteos)
        elif opcion == 3:
            crud.actualizar_publicacion(posteos)
        elif opcion == 4: 
            crud.leer_publicaciones(posteos)
        else:
            print("Opción no válida.")
        
    
    elif menu == 4:  # ---- Ordenar ----
        opcion = ordenamiento()  
        if opcion == 1:
            print("ordenar usuarios ")
        elif opcion == 2:
            print("ordenar hashtags")
        elif opcion == 3:
            crud.ordenar_publicaciones(posteos) 
        elif opcion == -1:
            continue  # vuelve al menu principal
        else:
            print("Opción no válida.")


    elif menu==5:                #----Estadisticas----
        estadisticas()
    
    elif menu!=-1:
        print("Opcion no valida")   