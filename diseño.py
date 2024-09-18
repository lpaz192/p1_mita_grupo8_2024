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

#Diseño Ordenamiento
def ordenamiento():
    print("\n--- Ordenar ---")
    print("1. Ordenar usuarios")
    print("2. Ordenar hashtags")
    print("3. Ordenar publicaciones")
    print("-1. Volver al menú principal")
    return int(input("Seleccione una opción: "))

#Diseño Estadisticas
def estadisticas():
    print("\n---Estadisticas---")
    print("1. Hashtag mas eficas")
    print("2. Seguidores ganados por publicación")
    print("-1. Volver al menu principal")
    return int(input("Seleccione una opcción: "))

#Diseño de tablas usuario
parte_superior=lambda: print(f"┌{'─'*6}┬{'─'*17}┬{'─'*12}┬{'─'*12}┬{'─'*12}┬{'─'*32}┐")
encabezado_usuarios=lambda: print(f"│ {'Id':<4} │ {'Usuarios':<15} │ {'Seguidores':<10} │ {'Seguidos':<10} │ {'Likes':<10} │ { 'Correos':<30} │")
mostrar_usuario=lambda id, datos: print(f"│ {id:<4} │ {datos['Usuario']:<15} │ {datos['Seguidores']:<10} │ {datos['Seguidos']:<10} │ {datos['Likes']:<10} │ {datos['Correo']:<30} │")
parte_conectiva=lambda: print(f"├{'─'*6}┼{'─'*17}┼{'─'*12}┼{'─'*12}┼{'─'*12}┼{'─'*32}┤")
parte_inferior=lambda:  print(f"└{'─'*6}┴{'─'*17}┴{'─'*12}┴{'─'*12}┴{'─'*12}┴{'─'*32}┘")

#Diseño de tablas hashtag
parte_superior_hashtag=lambda: print(f"┌{'─'*17}┬{'─'*15}┬{'─'*18}┬{'─'*12}┐")
encabezado_hashtags=lambda:          print(f"│ {'Hashtags':<15} │ {'Cant. posteos':<13} │ {'Veces compartido':<16} │ {'Likes':<10} │")
mostrar_hashtag=lambda hashtag, fil: print(f"│ {hashtag:<15} │ {fil['Cant. posteos']:<13} │ {fil['Veces compartido']:<16} │ {fil['Likes']:<10} │")
parte_conectiva_hashtag=lambda: print(f"├{'─'*17}┼{'─'*15}┼{'─'*18}┼{'─'*12}┤")
parte_inferior_hashtag=lambda: print(f"└{'─'*17}┴{'─'*15}┴{'─'*18}┴{'─'*12}┘")

#Diseño de tablas publicaciones 
parte_superior_publicacion = lambda: print(f"┌{'─'*12}┬{'─'*20}┬{'─'*10}┬{'─'*15}┬{'─'*25}┬{'─'*12}┐")
encabezado_publicacion = lambda: print(f"│ {'ID':<10} │ {'Fecha':<18} │ {'Likes':<8} │ {'Comentarios':<13} │ {'ID Usuario':<12} │ {'Usuario':<20} │")
mostrar_publicacion = lambda id_post, fecha, likes, comentarios, id_usuario, usuario: print(f"│ {id_post:<10} │ {fecha:<18} │ {likes:<8} │ {comentarios:<13} │ {id_usuario:<12} │ {usuario:<20} │")
parte_conectiva_publicacion = lambda: print(f"├{'─'*12}┼{'─'*20}┼{'─'*10}┼{'─'*15}┼{'─'*12}┼{'─'*20}┤")
parte_inferior_publicacion = lambda: print(f"└{'─'*12}┴{'─'*20}┴{'─'*10}┴{'─'*15}┴{'─'*12}┴{'─'*20}┘")
