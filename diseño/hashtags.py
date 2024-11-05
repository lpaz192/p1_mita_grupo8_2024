from validez import obtener_opcion
#Diseño CRUD Hashtags

def crud_hashtags():
    print("\n---Gestion de hashtags---")
    print("1. Agregar hashtags")
    print("2. Eliminar hashtags")
    print("3. Actualizar hashtags")
    print("4. Leer hashtags")
    print("-1. Volver al menu principal")
    opciones=[-1,1,2,3,4]
    return obtener_opcion(opciones)

#Diseño de tablas hashtag
parte_superior=lambda: print(f"\n┌{'─'*17}┬{'─'*15}┬{'─'*18}┬{'─'*12}┐")
encabezado=lambda:          print(f"│ {'Hashtags':<15} │ {'Cant. posteos':<13} │ {'Veces compartido':<16} │ {'Likes':<10} │")
mostrar=lambda hashtag, fil: print(f"│ {hashtag:<15} │ {fil['Cant. posteos']:<13} │ {fil['Veces compartido']:<16} │ {fil['Likes']:<10} │")
parte_conectiva=lambda: print(f"├{'─'*17}┼{'─'*15}┼{'─'*18}┼{'─'*12}┤")
parte_inferior=lambda: print(f"└{'─'*17}┴{'─'*15}┴{'─'*18}┴{'─'*12}┘")
