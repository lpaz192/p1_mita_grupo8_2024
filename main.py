from datetime import datetime
from diseño import crud_hashtags, crud_publicacion, crud_usuarios, mostrar_menu, estadisticas, mostrar_ordenamiento
import crud, metricas, json, validez, random, ordenamiento
#Matrices
# 'ID'  'Usuario' 'Seguidores'  'Seguidos' 'Likes' 'Correo'  
usuario = [
    [1,  "Martinn",         234,   200,   100,    "martincho@outlook.com"    ],
    [2,  "Diego.lopez",     2000,  800,   1000,   "diegolopez@gmail.com"     ], 
    [3,  "carlaa_",         5000,  500,   8000,   "carlaguilar@gmail.com"    ],   
    [4,  "Marcediaz",       200,   1000,  100,    "marcelodiaz12@hotmail.com"],
    [5,  "gasparlab",       600,   300,   200,    "gasparlabastie@gmail.com" ],
    [6,  "maria.jones",     1200,  450,   500,    "mjones@hotmail.com"       ],
    [7,  "Lucas12",         1800,  750,   900,    "lucas12@domain.com"       ],
    [8,  "AnaPerez",        2500,  1100,  1200,   "anaperez@domain.org"      ],
    [9,  "JuanP",           1500,  400,   850,    "juanp@correo.com"         ],
    [10, "CamiloG_",        800,   600,   300,    "camilogomez@gmail.com"    ],
    [11, "nati.fernandez",  1700,  1000,  1200,   "nati_fernandez@yahoo.com" ],
    [12, "David_89",        3500,  1500,  2500,   "david89@gmail.com"        ]
]
  
# 'Hashtag'  'Cant posteos'  'Veces compartido'  'Likes' 
hashtags = [
    ["#Feriado",           400,   2000,   6000  ],   
    ["#UADELabs",          200,   1500,   5000  ],
    ["#UADE",              3000,  50000,  200000],
    ["#Progra1",           500,   3000,   80000 ],
    ["#ArteDigital",       2000,  40000,  100000],
    ["#FitnessGoals",      1500,  10000,  45000 ],
    ["#VueltaAlCole",      800,   5000,   20000 ],
    ["#TechNews",          600,   4000,   15000 ],
    ["#CineFan",           1200,  25000,  70000 ],
    ["#Recetas",           500,   3000,   12000 ],
    ["#Viajes2024",        2200,  60000,  250000]
]

#Diccionarios
#Crear diccionario usuarios
usuarios_dict={                
    fil[0]:{
        'Usuario':fil[1],
        'Seguidores':fil[2],   #Un diccionario con el id del usuario y los datos del usuario
        'Seguidos':fil[3],     #Dentro de los datos del usuario son diccioanrios con la infromacion y su 'etiqueta'
        'Likes':fil[4],
        'Correo':fil[5]
    }for fil in usuario
}

#Crear diccionario hashtags
hashtags_dict={                
    fil[0]:{
        'Cant. posteos':fil[1],
        'Veces compartido':fil[2],
        'Likes':fil[3]
    }for fil in hashtags
}

posteos = [["ID Post", "Fecha de publicación", "Cantidad de likes", "Cantidad de comentarios", "ID Usuario", "Usuario",'Hashtag']]

hashtags_index= list(hashtags_dict.keys())
for i in range(1,11): #se crean 10 publicaciones con numeros aleatorios
    id_post = str(i).zfill(3)
    while True:
        fecha_publicacion = datetime.now().strftime('%Y-%m-%d')
        if validez.validar_fecha(fecha_publicacion):
            break
    likes = random.randint(0, 10000)
    comentarios = random.randint(0, 1000)

    hashtags_id=hashtags_index[random.randint(0,len(hashtags_index)-1)]
    ids_usuarios = list(usuarios_dict.keys())
    id_usuario = random.choice(ids_usuarios)
    datos_usuario = usuarios_dict[id_usuario]
    nombre_usuario = datos_usuario['Usuario']

    posteos.append([id_post, fecha_publicacion, likes, comentarios, id_usuario, nombre_usuario,hashtags_id])


#Menu principal
menu=0
while menu!=-1:
    menu = mostrar_menu()

    
    if menu==1:                        #----  Usuario     ----
        opcion_crud=crud_usuarios()   
        
        if opcion_crud==1:                   #Agregar
            crud.agregar_usuario(usuarios_dict)

        elif opcion_crud==2:                 #Eliminar
            crud.leer_usuario(usuarios_dict)
            print("\nPara eliminar ",end="")
            usuario_fila = validez.validar_id(usuarios_dict)
            crud.eliminar_usuario(usuario_fila,usuarios_dict)
        
        elif opcion_crud==3:                 #Actualizar
            crud.leer_usuario(usuarios_dict)  #Se muestra la matriz
            #Se selecciona el usuario a modificar
            print("\nPara actualizar ",end="")
            opcion_usuario = validez.validar_id(usuarios_dict)   
            
            #Se selecciona el elemento a modificar
            opcion_usuario_elemento = crud.seleccionar_elemento_usuarios(opcion_usuario,usuarios_dict) 
            
            #Se modifica el elemento
            crud.actualizar_usuario(opcion_usuario,opcion_usuario_elemento,usuarios_dict)
        
        elif opcion_crud == 4:               #Leer
            crud.leer_usuario(usuarios_dict)
            input('Oprima enter para continuar ')

    elif menu==2:                #----Hashtag     ----
        opcion_crud = crud_hashtags()
        if opcion_crud==1:                #Agregar
            crud.agregar_hashtag(hashtags_dict)

        elif opcion_crud==2:              #Eliminar
            crud.leer_hashtag(hashtags_dict)
            print("\nPara eliminar ingrese un hashtag existente: ",end="")
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
            input('Oprima enter para continuar ')
        
    elif menu==3:                #----Publicacion ----
        opcion=crud_publicacion()
        if opcion == 1:          #Agregar
            crud.agregar_publicacion(posteos, usuarios_dict, hashtags_dict)
        elif opcion == 2:        #Eliminar
            crud.eliminar_publicacion(posteos)
        elif opcion == 3:        #Actualizar
            crud.actualizar_publicacion(posteos, usuarios_dict)
        elif opcion == 4:        #Leer
            crud.leer_publicaciones(posteos)
        else:
            print("Opción no válida.")
        
    
    elif menu==4:  # ---- Ordenar ----
        opcion = mostrar_ordenamiento()  
        if opcion == 1:
            ordenamiento.ordenar_publicaciones(posteos) 


    elif menu==5:                #----Estadisticas----
        estadisticas()
    
    elif menu!=-1:
        print("Opcion no valida")   