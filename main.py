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


""" Notas: 

"""
import crud, metricas, json, validez
from diseño import __menu__, crud_hashtags, crud_usuarios, estadisticas, crud_publicacion
#Funciones
def eleccion():
    matriz_elegida=0
    while matriz_elegida!=1 and matriz_elegida!=2:
        print("En que matriz deseas realizar esta operación\n1. Usuarios\n2. Hashtags")
        matriz_elegida=int(input("Seleccione: "))                          #1 matriz de usuario   2. matriz de posteo
        if matriz_elegida !=1 and matriz_elegida !=2:
            print("Por favor ingrese un numero dentro de los solicitados")
    return matriz_elegida

def ordenamiento(matriz):
    matriz.sort()
    return matriz

#Matrices
usuario = [["Usuario",     "Seguidores", "Seguidos", "Likes",  "Correo"],
           ["Diego.lopez", 2000,       800,       1000,  "diegolopez@gmail.com"],  #Estos son ejemplos aleatorios
           ["carlitaa",    5000,       500,       8000,  "carlaguilar@gmail.com"],
           ["Marcediaz",   200,        1000,      100,   "marcelodiaz12@hotmail.com"]]

hashtags = [["hashtag","Cantidad de posteos","Veces compartido","Likes"],
            ["#UADELabs",2000,10000,50000]]                                        #Estos son ejemplos aleatorios  

posteos = [[]]

#Menu principal
"""
def seleccion():    
    opcion=__menu__()
    if opcion==1:                   #agregar
        matriz_elegida = eleccion()
        if matriz_elegida == 1:
            usuario.append(crud.agregar(matriz_elegida))  
        else:
            hashtags.append(crud.agregar(matriz_elegida))

    elif menu==2:                 #Leer
        seleccion = int(input("Que matriz deseas visualizar\n1. Para usuarios\n2. Para hashtags\n3. Para publicaciones\n"))
        while seleccion<=0 or seleccion>3:    
            print("el numero ingresado no está dentro de los numeros solicitados\n Por favor ingrese el numero nuevamente: ",end="")
            seleccion=int(input())
        if seleccion==1:
            crud.leer(seleccion,usuario) 
        elif seleccion==2:
            crud.leer(seleccion,hashtags) 
        else:
            crud.leer(seleccion,posteos)

    elif menu==3:                 #Actualizar
        if eleccion() == 1:        #Modificacion de usuarios
            usuario_modif = crud.seleccionar_usuario(usuario)
            usuario_elemnto_modif = crud.seleccionar_elemento_usuario()        #Se solicita el elemento a modificar
            usuario[usuario_modif][usuario_elemnto_modif]=crud.actualizar(usuario_elemnto_modif)  #Se inserta el elemento modificado
        else:
            crud.actualizar(hashtags)

    elif menu==4:                 #Eliminar
        if eleccion()==1:
            
            usuario_eliminar=crud.seleccionar_usuario(usuario)
            """
"""
            crud.eliminar(usuario,usuario_eliminar)
            """
"""
            usuario.pop(usuario_eliminar)
        else:
            crud.eliminar(hashtags)
"""
menu=0
while menu!=-1:
    menu = __menu__()

    if menu==1:                 #Usuario
        opcion=crud_usuarios()   
        
        if opcion==1:                 #Agregar
            usuario.append(crud.agregar(menu))
        
        elif opcion==2:               #Eliminar
            print()
        
        elif opcion==3:               #Actualizar
            opcion_usuario = crud.seleccionar(menu,usuario)
            opcion_usuario_elemento = crud.seleccionar_elemento(menu,opcion_usuario,usuario)
            usuario[opcion_usuario][opcion_usuario_elemento]=crud.actualizar(menu,opcion_usuario_elemento)
        
        elif opcion==4:               #Leer
            crud.leer(opcion,usuario)

    elif menu==2:               #Hashtag
        opcion=crud_hashtags()
        if opcion==1:
            hashtags.append(crud.agregar(menu))

        elif opcion==2: 
            print("Falta funcion")

        elif opcion==3:
            opcion_hashtag = crud.seleccionar(menu,hashtags)
            opcion_hashtag_elemento = crud.seleccionar(menu,opcion_hashtag,hashtags)
            hashtags[opcion_hashtag][opcion_hashtag_elemento]=crud.actualizar(menu,opcion_usuario_elemento)
    elif menu==3:
        opcion=crud_publicacion()
    
    elif menu==4:
        ordenamiento()
    
    elif menu==5:
        estadisticas()
    
    else:
        print("Opcion no valida")