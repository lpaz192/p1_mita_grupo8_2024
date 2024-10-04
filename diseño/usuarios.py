#Diseño CRUD Usuarios
def obtener_opcion():
    opciones=[-1,1,2,3,4]
    while True:
        try:
            opcion=int(input('Selecione una opcion valida: '))
            if not opcion in opciones:
                print('Opcion invalida.')
                continue
            return opcion
        except ValueError:
            print('Entrada no valida.')

def crud_usuarios():
    print("\n---Gestion de Usuarios---")
    print("1. Agregar usuario")
    print("2. Eliminar usuario")
    print("3. Actualizar usuario")
    print("4. Leer usuario")
    print("-1. Volver al menu principal")
    return (obtener_opcion())


#Diseño de tablas usuario
parte_superior=lambda: print(f"\n┌{'─'*6}┬{'─'*17}┬{'─'*12}┬{'─'*12}┬{'─'*12}┬{'─'*32}┐")
encabezado=lambda: print(f"│ {'Id':<4} │ {'Usuarios':<15} │ {'Seguidores':<10} │ {'Seguidos':<10} │ {'Likes':<10} │ { 'Correos':<30} │")
mostrar=lambda id, datos: print(f"│ {str(id).zfill(4):<4} │ {datos['Usuario']:<15} │ {datos['Seguidores']:<10} │ {datos['Seguidos']:<10} │ {datos['Likes']:<10} │ {datos['Correo']:<30} │")
parte_conectiva=lambda: print(f"├{'─'*6}┼{'─'*17}┼{'─'*12}┼{'─'*12}┼{'─'*12}┼{'─'*32}┤")
parte_inferior=lambda:  print(f"└{'─'*6}┴{'─'*17}┴{'─'*12}┴{'─'*12}┴{'─'*12}┴{'─'*32}┘")
