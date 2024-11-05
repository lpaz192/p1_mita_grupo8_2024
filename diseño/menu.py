from validez import obtener_opcion
# Diseño menu principal

def mostrar_menu():
    print("\n---Menu Principal---")
    print("1.  Gestion de usuarios")
    print("2.  Gestion de hastags")
    print("3.  Gestion de publicaciones")
    print("4.  Ordenamiento")
    print("5.  Estadisticas")
    print('6.  Archivos')
    print("-1. Para cancelar")
    opciones=[-1,1,2,3,4,5,6]
    return obtener_opcion(opciones)