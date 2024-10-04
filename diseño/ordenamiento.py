#Diseño Ordenamiento
def obtener_opcion():
    opciones=[-1,1]
    while True:
        try:
            opcion=int(input('Selecione una opcion valida: '))
            if not opcion in opciones:
                print('Opcion invalida.')
                continue
            return opcion
        except ValueError:
            print('Entrada no valida.')

def mostrar_ordenamiento():
    print("\n--- Ordenar ---")
    print("1. Ordenar publicaciones")
    print("-1. Volver al menú principal")
    return obtener_opcion()
