from validez import obtener_opcion
# Diseño menu archivos

def menu_archivos():
    print("\n---Menu Archivos---")
    print("1.  Recetear arvhivos usuarios")
    print('2.  Recetear archivos hashtags')
    print('3.  Recetear archivos posteos')
    print("-1. Para cancelar")
    opciones=[-1,1,2,3]
    return obtener_opcion(opciones)

def confrimar_formateo(tipo):
    '''Esta funcion pide una validación extra antes de realizar una operacion
    devuelve True si la respues es Y/y
    devuelve False si la respuesta es N/n
    '''
    respuesta = input(f'¿Estas seguro que deseas recetear los {tipo}? (y/n): ').lower()
    while not respuesta in ('y','n'):
        respuesta = input('Por favor ingrese uno de los valores solicitados: ').lower()
    if respuesta == 'n':
        return False
    else:
        return True