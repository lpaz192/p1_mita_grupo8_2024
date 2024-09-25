# Diseño menu principal
def mostrar_menu():
    print("\n---Menu Principal---")
    print("1.  Gestion de usuarios")
    print("2.  Gestion de hastags")
    print("3.  Gestion de publicaciones")
    print("4.  Ordenamiento")
    print("5.  Estadisticas")
    print("-1. Para cancelar")
    menu = input("Seleccione una opcción: ")
    while True:
        if menu.isdigit() or menu=='-1':
            if int(menu)>=1 and int(menu)<=5 or int(menu)==-1:
                return int(menu)
        menu=input('Opcion no valida, por favor ingrese un numero dentro del rango solicitado: ')
