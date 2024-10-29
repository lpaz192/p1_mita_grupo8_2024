import json
def inicializar_diccionairo_archivo(nombre_archivo, diccionario):
    try:
        with open(nombre_archivo, 'r', encoding='UTF-8') as archivo:
            datos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(nombre_archivo, 'w', encoding='UTF-8') as archivo:
            json.dump(diccionario, archivo, indent=4)