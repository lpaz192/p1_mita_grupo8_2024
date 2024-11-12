from validez import obtener_opcion
#Diseño CRUD Publicacion

def crud_publicacion():
    print("\n---Gestion de Publicaciones---")
    print("1. Agregar publicacion")
    print("2. Eliminar publicacion")
    print("3. Actualizar publicacion")
    print("4. Leer publicacion")
    print("-1. Volver al menu principal")
    opciones=[-1,1,2,3,4]
    return obtener_opcion(opciones)


#Diseño de tablas publicaciones 
parte_superior = lambda: print(
    f"┌{'─'*12}┬{'─'*20}┬{'─'*10}┬{'─'*15}┬{'─'*12}┬{'─'*20}┬{'─'*17}┐")

encabezado = lambda: print(
    f"│ {'ID':<10} │ {'Fecha':<18} │ {'Likes':<8} │ {'Comentarios':<13} │ {'ID Usuario':<10} │ {'Usuario':<18} │ {'Hashtag':<15} │")

mostrar = lambda id_post, fecha, likes, comentarios, id_usuario, usuario, hashtag: print(
    f"│ {id_post:<10} │ {fecha:<18} │ {likes:<8} │ {comentarios:<13} │ {str(id_usuario).zfill(4):<10} │ {usuario:<18} │ {hashtag:<15} │")

parte_conectiva = lambda: print(
    f"├{'─'*12}┼{'─'*20}┼{'─'*10}┼{'─'*15}┼{'─'*12}┼{'─'*20}┼{'─'*17}┤")

parte_inferior = lambda: print(
    f"└{'─'*12}┴{'─'*20}┴{'─'*10}┴{'─'*15}┴{'─'*12}┴{'─'*20}┴{'─'*17}┘")
