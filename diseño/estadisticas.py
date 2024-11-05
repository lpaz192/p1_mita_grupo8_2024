from validez import obtener_opcion
#Diseño Estadisticas
def estadisticas():
    print("\n---Estadisticas---")
    print("1. Hashtag mas eficas")
    print("2. Seguidores ganados por publicación")
    print("-1. Volver al menu principal")
    opciones=[-1,1,2]
    return obtener_opcion(opciones)
