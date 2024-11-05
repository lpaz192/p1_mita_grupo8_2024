import json

def cargar_datos(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def calcular_metricas(usuarios_file, hashtags_file):
    usuarios_data = cargar_datos(usuarios_file)
    hashtags_data = cargar_datos(hashtags_file)

    # calcular estadisticas de usuarios
    total_usuarios = len(usuarios_data)
    total_seguidores = sum(data['Seguidores'] for data in usuarios_data.values())
    total_seguidos = sum(data['Seguidos'] for data in usuarios_data.values())
    total_publicaciones = sum(len(data['Publicaciones']) for data in usuarios_data.values())

    # calcular estadisticas de hashtags
    total_hashtags = len(hashtags_data)
    total_uso_hashtags = sum(hashtags_data.values())

    print(f"Total de usuarios: {total_usuarios}")
    print(f"Total de seguidores: {total_seguidores}")
    print(f"Total seguidos: {total_seguidos}")
    print(f"Total de publicaciones: {total_publicaciones}")
    print(f"Total de hashtags: {total_hashtags}")
    print(f"Total de uso de hashtags: {total_uso_hashtags}")

if __name__ == '__main__':
    calcular_metricas('usuarios.json', 'hashtags.json')
