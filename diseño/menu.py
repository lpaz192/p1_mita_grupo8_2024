# Diseño menu principal
def obtener_opcion():
    opciones=[-1,1,2,3,4,5]
    while True:
        try:
            opcion=int(input('Selecione una opcion valida: '))
            if not opcion in opciones:
                print('Opcion invalida.')
                continue
            return opcion
        except ValueError:
            print('Entrada no valida.')

def mostrar_menu():
    print("\n---Menu Principal---")
    print("1.  Gestion de usuarios")
    print("2.  Gestion de hastags")
    print("3.  Gestion de publicaciones")
    print("4.  Ordenamiento")
    print("5.  Estadisticas")
    print("-1. Para cancelar")
    return obtener_opcion()