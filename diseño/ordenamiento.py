from validez import obtener_opcion
#Diseño Ordenamiento
def mostrar_ordenamiento():
    print("\n--- Ordenar ---")
    print("1. Ordenar publicaciones")
    print("-1. Volver al menú principal")
    opciones=[-1,1]
    return obtener_opcion(opciones)
