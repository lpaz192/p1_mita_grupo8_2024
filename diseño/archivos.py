from validez import obtener_opcion
# Diseño menu archivos

def menu_archivos():
    print("\n---Menu Archivos---")
    print("1.  Formatear arvhivos usuarios")
    print('2.  Formatear archivos hashtags')
    print('3.  Formatear archivos posteos')
    print("-1. Para cancelar")
    opciones=[-1,1,2,3]
    return obtener_opcion(opciones)

def confrimar_formateo(tipo):
    x = input(f'Estas seguro que deseas formatear {tipo} (y/n): ')
    patron = ['n','N','y','Y']
    while not x in patron:
        x = input('Por favor ingrese uno de los valores solicitados: ')
    if x == 'n' or x == 'N':
        return False
    else:
        return True