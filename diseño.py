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
    while x==1:
        print("\n---CRUD Usuarios---")
        print("1. Agregar usuario")
        print("2. Eliminar usuario")
        print("3. Actualizar usuario")
        print("4. Leer usuario")
        print("-1. Volver al menu principal")
    return int(input("Seleccione una opcción: "))

def seleccionar_usuario():
    print("\n---Usuarios---")
    return int(input("Seleccione un usuario: "))
    
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

