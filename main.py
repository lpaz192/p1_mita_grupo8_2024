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
            ["#UADELabs",2000,10000,50000]]                          #Estos son ejemplos aleatorios  

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
opcion=0
while opcion!=-1:
    opcion = __menu__()

    if opcion==1:
        opcion_usuario=crud_usuarios()
        while opcion_usuario!=-1:
            opcion_usuario_elemento = crud_usuarios()
            

    elif opcion==2:
        opcion=crud_hashtags()
    
    elif opcion==3:
        opcion=crud_publicacion()
    
    elif opcion==4:
        ordenamiento()
    
    elif opcion==5:
        estadisticas()
    
    else:
        print("Opcion no valida")