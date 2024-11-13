import json
def inicializar_diccionairo_archivo(nombre_archivo, diccionario):
    '''Crea o llena el archivo con los valores pasados
    '''
    with open(nombre_archivo, 'w', encoding='UTF-8') as archivo:
        json.dump(diccionario, archivo, indent=4)