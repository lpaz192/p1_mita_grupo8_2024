""" Notas: 

"""
from datetime import datetime
import random
import crud, metricas, json, validez
from diseño import __menu__, crud_hashtags, crud_usuarios, estadisticas, crud_publicacion, ordenamiento  

#Funciones

#Matrices
# 'ID'  'Usuario' 'Seguidores'  'Seguidos' 'Likes' 'Correo'  
usuario = [[1, "Martinn",     234,   200,   100,   "martincho@outlook.com"    ],
           [2, "Diego.lopez",  2000,   800,   1000,  "diegolopez@gmail.com"     ], 
           [3, "carlaa_",     5000,   500,   8000,  "carlaguilar@gmail.com"    ],   
           [4, "Marcediaz",     200,   1000,  100,   "marcelodiaz12@hotmail.com"],
           [5, "gasparlab",     600,   300,  200,   "gasparlabastie@gmail.com"]
           ]
  
usuarios_dict={                #Crear diccionario usuarios
    fil[0]:{
        'Usuario':fil[1],
        'Seguidores':fil[2],   #Una tupla con el id del usuario y los datos del usuario
        'Seguidos':fil[3],     #Dentro de los datos del usuario son tuplas entre la infromacion y su 'etiqueta'
        'Likes':fil[4],
        'Correo':fil[5]
    }for fil in usuario
}

hashtags = [["#Feriado",     400 ,  2000 ,  6000  ],   # 'Hashtag'  'Cant posteos'  'Veces compartido'  'Likes' 
            ["#UADELabs",    200,   1500,   5000  ],
            ["#UADE",        3000,  50000,  200000],
            ["#Progra1",     500,   3000,   80000 ],
            ["#ArteDigital", 2000,  40000,  100000],
            ]  
                                    
hashtags_dict={                #Crear diccionario hashtags
    fil[0]:{
        'Cant. posteos':fil[1],
        'Veces compartido':fil[2],
        'Likes':fil[3]
    }for fil in hashtags
}

posteos = [["ID Post", "ID usuario", "Hashtag", "Fecha de publicación", "Cantidad de likes", "Cantidad de comentarios"]]
lista_hashtag = list(hashtags_dict.keys())

for i in range(1,11): #se crean 10 publicaciones con numeros aleatorios
    id_post = str(i).zfill(3)
    while True:
        fecha_publicacion = datetime.now().strftime('%Y-%m-%d')
        if validez.validar_fecha(fecha_publicacion):
            break
    likes = random.randint(0, 10000)
    comentarios = random.randint(0, 1000)

    lista_id = list(usuarios_dict.keys())
    lista_hashtag = list(hashtags_dict.keys())

    usuario_posteo = usuarios_dict[lista_id[random.randint(0,len(lista_id)-1)]]['Usuario']
    hashtag_posteo = lista_hashtag[random.randint(0,len(lista_hashtag)-1)]

    posteos.append([id_post, usuario_posteo, hashtag_posteo, fecha_publicacion, likes, comentarios])


#Menu principal
menu=0
while menu!=-1:
    menu = __menu__()

    if menu==1:                        #----  Usuario     ----
        opcion_crud=crud_usuarios()   
        
        if opcion_crud==1:                   #Agregar
            crud.agregar_usuario(usuarios_dict)

        elif opcion_crud==2:                 #Eliminar
            crud.leer_usuario(usuarios_dict)
            print("\nIngrese el usuario que desee eliminar",end="")
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
            print("\nIngrese el hashtag que desee eliminar",end="")
            hashtag_fila= validez.hashtag_existente(hashtags_dict)
            crud.eliminar_hashtag(hashtag_fila,hashtags_dict)

        elif opcion_crud==3:              #Actualizar
            crud.leer_hashtag(hashtags_dict)
            print('\nIngres el hashtag que desea modificar: ',end="")
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
        
    
    elif menu==4:  # ---- Ordenar ----
        opcion = ordenamiento()  
        if opcion == 1:
            print("ordenar usuarios ")
        elif opcion == 2:
            print("ordenar hashtags")
        elif opcion == 3:
            crud.ordenar_publicaciones(posteos) 
        else:
            print("Opción no válida.")


    elif menu==5:                #----Estadisticas----
        estadisticas()
    
    elif menu!=-1:
        print("Opcion no valida")   