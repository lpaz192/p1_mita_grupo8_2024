import crud
# Diseño menu principal
def __menu__():
    print("\n---Menu Principal---")
    print("1.  CRUD usuarios")
    print("2.  CRUD hastags")
    print("3.  CRUD publicación")
    print("4.  Para ordenar")
    print("5.  Estadisticas")
    print("-1. Para cancelar")
    return int(input("Seleccione una opcción: "))

#Diseño CRUD Usuarios
def crud_usuarios():
    aux=0
    while aux==0 or aux>4:
        if aux==0 or aux>4:
            print("\n---CRUD Usuarios---")
            print("1. Agregar usuario")
            print("2. Eliminar usuario")
            print("3. Actualizar usuario")
            print("4. Leer usuario")
            print("-1. Volver al menu principal")
            aux = int(input("Seleccione una opcción: "))
        else: 
            print("Opcion no valida")
    return aux
   
#Diseño CRUD Hashtags
def crud_hashtags():
    print("\n---CRUD hashtags---")
    print("1. Agregar hashtags")
    print("2. Eliminar hashtags")
    print("3. Actualizar hashtags")
    print("4. Leer hashtags")
    print("-1. Volver al menu principal")
    return int(input("Seleccione una opcción: "))

#Diseño CRUD Publicacion
def crud_publicacion():
    print("\n---CRUD Publicacion---")
    print("1. Agregar publicacion")
    print("2. Eliminar publicacion")
    print("3. Actualizar publicacion")
    print("4. Leer publicacion")
    print("-1. Volver al menu principal")
    return int(input("Seleccione una opcción: "))

#Diseño Estadisticas
def estadisticas():
    print("\n---Estadisticas---")
    print("1. Hashtag mas eficas")
    print("2. Seguidores ganados por publicación")
    print("-1. Volver al menu principal")
    return int(input("Seleccione una opcción: "))

#Diseño de tablas
parte_superior=lambda: print(f"┌{'─'*4}┬{'─'*20}┬{'─'*8}┬{'─'*8}┬{'─'*8}┬{'─'*40}┐")
mostrar_usuario=lambda fil: print(f"│{fil[0]:^4}│{fil[1]:^20}│{fil[2]:^8}│{fil[3]:^8}│{fil[4]:^8}│{fil[5]:^40}│")
parte_inferior=lambda: print(f"└{'─'*4}┴{'─'*20}┴{'─'*8}┴{'─'*8}┴{'─'*8}┴{'─'*40}┘")
parte_conectiva=lambda: print(f"├{'─'*4}┼{'─'*20}┼{'─'*8}┼{'─'*8}┼{'─'*8}┼{'─'*40}┤")

#Diseño tablas
parte_superior_hashtag=lambda: print(f"┌{'─'*15}┬{'─'*8}┬{'─'*8}┬{'─'*8}┐")
mostrar_hashtag=lambda fil: print(f"│{fil[0]:15}│{fil[1]:^8}│{fil[2]:^8}│{fil[3]:^8}│")
parte_inferior_hashtag=lambda: print(f"└{'─'*15}┴{'─'*8}┴{'─'*8}┴{'─'*8}┘")
parte_conectiva_hashtag=lambda: print(f"├{'─'*15}┼{'─'*8}┼{'─'*8}┼{'─'*8}┤")