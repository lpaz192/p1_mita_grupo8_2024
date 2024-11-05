import json

def clasificar_cuentas(publicaciones, bots, index=0, cuentas_spam=None, cuentas_seguras=None):
    if cuentas_spam is None:
        cuentas_spam = {}
    if cuentas_seguras is None:
        cuentas_seguras = {}
        
    # si se recorrio todas las publicaciones, dar los resultados
    if index >= len(publicaciones):
        return cuentas_spam, cuentas_seguras

    publicacion = publicaciones[index]
    id_usuario = publicacion[4]  # los id se guardan en el 4
    hashtag_encontrado = publicacion[6]  # los # se guardan en el 6

    if hashtag_encontrado in bots:
        # clasifica la cuenta como spam
        cuentas_spam[id_usuario] = cuentas_spam.get(id_usuario, 0) + 1 
    else:
        # clasifica como cuenta segura si no ha sido marcada como spam
        if id_usuario not in cuentas_spam:  
            cuentas_seguras[id_usuario] = cuentas_seguras.get(id_usuario, 0) + 1 

    # llama recursivamente a la función para la siguiente publicación
    return clasificar_cuentas(publicaciones, bots, index + 1, cuentas_spam, cuentas_seguras)

def leer_y_clasificar(publicaciones_json, bots_txt):
    with open(publicaciones_json, 'r') as f:
        publicaciones = json.load(f)

    with open(bots_txt, 'r') as f:
        bots = set(line.strip() for line in f if line.strip())  # lee y limpia líneas

    # llama a la función recursiva para clasificar cuentas
    cuentas_spam, cuentas_seguras = clasificar_cuentas(publicaciones, bots)

    # mostrar resultados
    print("Cuentas clasificadas como spam:")
    for cuenta, cantidad in cuentas_spam.items():
        print(f"Usuario ID: {cuenta}, Cantidad de publicaciones spam: {cantidad}")

    print("\nCuentas clasificadas como seguras:")
    for cuenta, cantidad in cuentas_seguras.items():
        print(f"Usuario ID: {cuenta}, Cantidad de publicaciones seguras: {cantidad}")

