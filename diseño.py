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

#Diseño de tablas usuario
parte_superior=lambda: print(f"┌{'─'*6}┬{'─'*17}┬{'─'*12}┬{'─'*12}┬{'─'*12}┬{'─'*42}┐")
encabezado_usuarios=lambda: print(f"│ {'Id':<4} │ {'Usuarios':<15} │ {'Seguidores':<10} │ {'Seguidos':<10} │ {'Likes':<10} │ { 'Correos':<40} │")
mostrar_usuario=lambda id, datos: print(f"│ {id:<4} │ {datos['Usuario']:<15} │ {datos['Seguidores']:<10} │ {datos['Seguidos']:<10} │ {datos['Likes']:<10} │ {datos['Correo']:<40} │")
parte_conectiva=lambda: print(f"├{'─'*6}┼{'─'*17}┼{'─'*12}┼{'─'*12}┼{'─'*12}┼{'─'*42}┤")
parte_inferior=lambda:  print(f"└{'─'*6}┴{'─'*17}┴{'─'*12}┴{'─'*12}┴{'─'*12}┴{'─'*42}┘")

#Diseño de tablas hashtag
parte_superior_hashtag=lambda: print(f"┌{'─'*17}┬{'─'*15}┬{'─'*18}┬{'─'*14}┐")
encabezado_hashtags=lambda: print(f"│ {'Hashtags':<15} │ {'Cant. posteos':<13} │ {'Veces compartido':<16} │ {'Likes':<12} │")
mostrar_hashtag=lambda fil: print(f"│ {fil[0]:<15} │ {fil[1]:<12}  │ {fil[2]:<12}     │ {fil[3]:<12} │")
parte_conectiva_hashtag=lambda: print(f"├{'─'*17}┼{'─'*15}┼{'─'*18}┼{'─'*14}┤")
parte_inferior_hashtag=lambda: print(f"└{'─'*17}┴{'─'*15}┴{'─'*18}┴{'─'*14}┘")