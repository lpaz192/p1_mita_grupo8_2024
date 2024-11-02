from datetime import datetime
from diseño import (crud_hashtags, 
                    crud_publicacion, 
                    crud_usuarios, 
                    mostrar_menu, 
                    estadisticas, 
                    menu_archivos,
                    confrimar_formateo,
                    mostrar_ordenamiento)
import crud, json, validez, random, ordenamiento
from archivos_json import inicializar_diccionairo_archivo
from archivos_txt import inicializar_txt
'''
import instaloader

loader = instaloader.Instaloader()

# cargar usuarios manualmente
def cargar_usuarios():
    usuarios = []
    print("Ingresa los nombres de usuario a analizar (escribe 'fin' para terminar):")
    while True:
        usuario = input("Usuario: ")
        if usuario.lower() == 'fin':
            break
        usuarios.append(usuario)
    return usuarios

# obtener datos de usuarios
def obtener_datos_usuarios(usuarios):
    usuarios_data = {}
    for usuario in usuarios:
        try:
            profile = instaloader.Profile.from_username(loader.context, usuario)
            usuarios_data[usuario] = {
                'Seguidores': profile.followers,
                'Seguidos': profile.followees,
                'Publicaciones': []
            }
        except Exception as e:
            print(f"Error al obtener datos de {usuario}: {e}")
    return usuarios_data

# obtener publicaciones 
def obtener_publicaciones(usuario):
    publicaciones_data = []
    try:
        profile = instaloader.Profile.from_username(loader.context, usuario)
        for post in profile.get_posts():
            publicaciones_data.append({
                'Fecha de publicación': post.date,
                'Cantidad de likes': post.likes,
                'Cantidad de comentarios': post.comments,
                'Hashtags': post.caption_hashtags,
            })
            if len(publicaciones_data) >= 10:  # solo carga 10
                break
    except Exception as e:
        print(f"Error al obtener publicaciones de {usuario}: {e}")
    return publicaciones_data


usuarios_a_analizar = cargar_usuarios()

usuarios_dict = obtener_datos_usuarios(usuarios_a_analizar)

# obtener las publicaciones de cada usuario
for usuario in usuarios_a_analizar:
    publicaciones = obtener_publicaciones(usuario)
    usuarios_dict[usuario]['Publicaciones'] = publicaciones

posteos = [["ID Post", "Fecha de publicación", "Cantidad de likes", "Cantidad de comentarios", "ID Usuario", "Usuario", 'Hashtags']]

for usuario, data in usuarios_dict.items():
    for idx, publicacion in enumerate(data['Publicaciones']):
        id_post = str(idx + 1).zfill(3)  # id del post
        fecha_publicacion = publicacion['Fecha de publicación'].strftime('%Y-%m-%d')
        likes = publicacion['Cantidad de likes']
        comentarios = publicacion['Cantidad de comentarios']
        hashtags_id = ', '.join(publicacion['Hashtags']) if publicacion['Hashtags'] else "Sin hashtags"
        
        posteos.append([id_post, fecha_publicacion, likes, comentarios, usuario, usuario, hashtags_id])

# mostrar posts
for post in posteos:
    print(post)

'''


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

#Crear posteos / Estructura principal de posteos
posteos = [["ID Post", "Fecha de publicación", "Cantidad de likes", "Cantidad de comentarios", "ID Usuario", "Usuario",'Hashtag']]

hashtags_index= list(hashtags_dict.keys())
for i in range(1,11): #se crean 10 publicaciones con numeros aleatorios
    id_post = str(i).zfill(3)
    while True:
        fecha_publicacion = datetime.now().strftime('%d-%m-%Y')
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

#Funcinoes de opciones
def opcion_crud_usuarios():
    opcion_elegida = crud_usuarios()   
            
    #Agregar
    if opcion_elegida == 1:
        print()                   
        crud.agregar_usuario('usuario.json')

    #Eliminar
    elif opcion_elegida == 2:                 
        crud.leer_usuario('usuario.json')
        print("\nPara eliminar un usuario ingrese el id del usuario: ", end="")
        usuario_id = validez.validar_id('usuario.json')
        crud.eliminar_usuario('usuario.json',usuario_id)
    
    #Actualizar
    elif opcion_elegida == 3:                 
        crud.actualizar_usuario('usuario.json')
    #Leer
    elif opcion_elegida == 4:               
        crud.leer_usuario('usuario.json')
        input('Oprima enter para continuar ')

def opcion_crud_hashtags():
    opcion_elegida = crud_hashtags()

    #Agregar
    if opcion_elegida == 1:                
        crud.agregar_hashtag('hashtag.json')

    #Eliminar
    elif opcion_elegida == 2:              
        crud.eliminar_hashtag('hashtag.json')

    #Actualizar
    elif opcion_elegida == 3:              
        crud.actualizar_hashtag('hashtag.json')

    #Leer
    elif opcion_elegida == 4:                        
        crud.leer_hashtag('hashtag.json')
        input('Oprima enter para continuar ')
    
def opcion_crud_publicaciones():
    opcion_elegida = crud_publicacion()

    #Agregar
    if opcion_elegida == 1:          
        crud.agregar_publicacion(posteos, usuarios_dict, hashtags_dict)
    
    #Eliminar
    elif opcion_elegida == 2:        
        crud.eliminar_publicacion(posteos)
    
    #Actualizar
    elif opcion_elegida == 3:        
        crud.actualizar_publicacion(posteos, usuarios_dict)
    
    #Leer
    elif opcion_elegida == 4:        
        crud.leer_publicaciones(posteos)
    else:
        print("Opción no válida.")
    
def opcion_archivos():
    opcion_elegida = menu_archivos()
    '''En caso de que los archivos json esten vacios o no existan
    estas funciones los crea y los llena con los datos del python'''
    
    #Archivos USUARIOS
    if opcion_elegida == 1:
        if confrimar_formateo('archivos de usuarios'):
            inicializar_diccionairo_archivo('usuario.json', usuarios_dict)
            input('Formateo realizado correctamente')
        else:
            input('Operacion cancelada')

    #Archivos HASHTAG
    elif opcion_elegida == 2:
        if confrimar_formateo('archivos de hashtag'):
            inicializar_diccionairo_archivo('hashtag.json', hashtags_dict)
            input('Formateo realizado correctamente')
        else:
            input('Operacion cancelada')

    #Archivos POSTEOS
    elif opcion_elegida == 3:
        if confrimar_formateo('archivos de hashtag'):
            inicializar_txt('publicaciones.txt',posteos)    
            input('Formateo realizado correctamente')
        else:
            input('Operacion cancelada')  
                  
#Menu principal
def __main__():
    opcion_menu = 0
    while opcion_menu != -1:
        opcion_menu = mostrar_menu()
        
        #----  CRUD Usuario     ----
        if opcion_menu == 1:                         
            opcion_crud_usuarios()

        #----  CRUD Hashtag     ----
        elif opcion_menu == 2:                       
            opcion_crud_hashtags()
        
        #----  CRUD Publicacion ----
        elif opcion_menu == 3:                       
            opcion_crud_publicaciones()

        # ---- Ordenar          ----
        elif opcion_menu == 4:                       
            opcion = mostrar_ordenamiento()  
            if opcion == 1:
                ordenamiento.ordenar_publicaciones(posteos) 
        
        #----  Estadisticas----
        elif opcion_menu == 5:                       
            estadisticas()

        elif opcion_menu == 6:
            opcion_archivos()

        elif opcion_menu==-1:
            break
        elif opcion_menu!=-1:
            print("Opcion no valida")   

if __name__ == '__main__':
    __main__()