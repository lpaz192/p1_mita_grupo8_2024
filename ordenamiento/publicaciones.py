from crud import imprimir_posteos
from validez import obtener_opcion
#ORDENAMIENTO PUBLICACIONES

#Ordenamiento
def ordenar_publicaciones(posteos):
    print("\n--- Ordenar Publicaciones ---")
    print("1. Ordenar por ID")
    print("2. Ordenar por cantidad de likes")
    print("-1. Volver al menú principal")
    
    opciones=[-1,1,2]
    opcion = obtener_opcion(opciones)
    
    if opcion == 1:
        ordenar_por_id(posteos)
    elif opcion == 2:
        ordenar_por_likes(posteos)
    elif opcion == -1:
        return

def ordenar_por_id(posteos):
    print("\nElija el orden de clasificación por ID:")
    print("1. De menor a mayor")
    print("2. De mayor a menor")
    print('-1. Para volver')
    #Pide ingreso de datos
    opciones=[-1,1,2]
    opcion = obtener_opcion(opciones)           
 
    encabezado = posteos[0]  
    datos = posteos[1:] 

    if opcion == 1:
        datos.sort(key=lambda x: int(x[0])) 
    elif opcion == 2:
        datos.sort(key=lambda x: int(x[0]), reverse=True)
    elif opcion == -1:
        print("Volviendo al menu")
        return

    posteos = [encabezado] + datos

    imprimir_posteos(posteos)  

def ordenar_por_likes(posteos):
    print("\nElija el orden de clasificación por cantidad de likes:")
    print("1. De menor a mayor")
    print("2. De mayor a menor")
    print('-1. Para volver')
    opciones=[-1,1,2]
    opcion = obtener_opcion(opciones)

    encabezado = posteos[0]
    datos = posteos[1:]

    for post in datos:
        post[2] = int(post[2])

    if opcion == 1:
        datos.sort(key=lambda x: x[2]) 
    elif opcion == 2:
        datos.sort(key=lambda x: x[2], reverse=True)
    elif opcion==-1:
        return

    posteos = [encabezado] + datos

    imprimir_posteos(posteos)  
    return