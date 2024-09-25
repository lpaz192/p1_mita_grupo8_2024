from crud import imprimir_posteos
#ORDENAMIENTO PUBLICACIONES
def ordenar_publicaciones(posteos):
    print("\n--- Ordenar Publicaciones ---")
    print("1. Ordenar por ID")
    print("2. Ordenar por cantidad de likes")
    print("-1. Volver al menú principal")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        ordenar_por_id(posteos)
    elif opcion == 2:
        ordenar_por_likes(posteos)
    elif opcion == -1:
        return
    else:
        print("Opción no válida.")

def ordenar_por_id(posteos):
    print("Elija el orden de clasificación por ID:")
    print("1. De menor a mayor")
    print("2. De mayor a menor")
    opcion = int(input("Seleccione una opción: "))

    encabezado = posteos[0]  
    datos = posteos[1:] 


    if opcion == 1:
        datos.sort(key=lambda x: int(x[0])) 
    elif opcion == 2:
        datos.sort(key=lambda x: int(x[0]), reverse=True)
    else:
        print("Opción no válida.")
        return

    posteos = [encabezado] + datos

    imprimir_posteos(posteos)  

def ordenar_por_likes(posteos):
    print("Elija el orden de clasificación por cantidad de likes:")
    print("1. De menor a mayor")
    print("2. De mayor a menor")
    opcion = int(input("Seleccione una opción: "))

    encabezado = posteos[0]
    datos = posteos[1:]

    for post in datos:
        post[2] = int(post[2])

    if opcion == 1:
        datos.sort(key=lambda x: x[2]) 
    elif opcion == 2:
        datos.sort(key=lambda x: x[2], reverse=True)
    else:
        print("Opción no válida.")
        return

    posteos = [encabezado] + datos

    imprimir_posteos(posteos)  
