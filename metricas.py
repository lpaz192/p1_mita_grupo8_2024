import json
from CuentasSPAM import clasificacion
from CuentasSPAM.clasificacion import analizar_spam_hashtags
from validez import obtener_opcion
def mostar_metricas_usuarios(metricas):
    print('\n--- Métricas de Usuarios ---')
    print(f'Total de usuarios:     {metricas['total_usuarios']}')
    print(f'Total de seguidores:   {metricas['total_seguidores']}')
    print(f'Total de seguidos:     {metricas['total_seguidos']}')
    print(f'Total de likes:        {metricas['total_likes']}')
    print(f'Promedio de seguidores por usuario:  {metricas['promedio_seguidores']:.2f}')
    print(f'Promedio de seguidos por usuario:    {metricas['promedio_seguidos']:.2f}')
    print(f'Promedio de likes por usuario:       {metricas['promedio_likes']:.2f}')
    input()

def mostrar_metricas_post(metricas):
    print('\n--- Métricas de Publicaciones ---')
    print(f'Total de publicaciones:  {metricas['total_publicaciones']}')
    print(f'Total de likes:          {metricas['total_likes']}')
    print(f'Total de comentarios:    {metricas['total_comentarios']}')
    print(f'Promedio de likes por publicación:       {metricas['promedio_likes']:.2f}')
    print(f'Promedio de comentarios por publicación: {metricas['promedio_comentarios']:.2f}')
    input()

def cargar_datos():
    from crud import cargar_usuarios, cargar_publicaciones
    usuarios_dict = cargar_usuarios()
    
    posteos = cargar_publicaciones()
    
    return usuarios_dict, posteos

def calcular_metricas_usuarios(usuarios_dict):
    if not usuarios_dict:
        print("No hay usuarios registrados.")
        return {
            "total_usuarios"     : 0,
            "total_seguidores"   : 0,
            "total_seguidos"     : 0,
            "total_likes"        : 0,
            "promedio_seguidores": 0,
            "promedio_seguidos"  : 0,
            "promedio_likes"     : 0,
        }
    
    total_usuarios   = len(usuarios_dict)
    total_seguidores = sum(user['Seguidores'] for user in usuarios_dict.values())
    total_seguidos   = sum(user['Seguidos'] for user in usuarios_dict.values())
    total_likes      = sum(user['Likes'] for user in usuarios_dict.values())
    
    promedio_seguidores = total_seguidores / total_usuarios if total_usuarios else 0
    promedio_seguidos   = total_seguidos / total_usuarios if total_usuarios else 0
    promedio_likes      = total_likes / total_usuarios if total_usuarios else 0
    
    return {
            "total_usuarios"     : total_usuarios,
            "total_seguidores"   : total_seguidores,
            "total_seguidos"     : total_seguidos,
            "total_likes"        : total_likes,
            "promedio_seguidores": promedio_seguidores,
            "promedio_seguidos"  : promedio_seguidos,
            "promedio_likes"     : promedio_likes,
        }

def calcular_metricas_posts(posteos):
    if not posteos:
        print("No hay publicaciones registradas.")
        return {
        'total_publicaciones' : 0,
        'total_likes'         : 0,
        'total_comentarios'   : 0,
        'promedio_likes'      : 0,
        'promedio_comentarios': 0
        }
    
    total_publicaciones =  len(posteos)-1
    total_likes =          sum(int(post[2]) for post in posteos[1:])
    total_comentarios =    sum(int(post[3]) for post in posteos[1:])
    
    promedio_likes       = total_likes / total_publicaciones if total_publicaciones else 0
    promedio_comentarios = total_comentarios / total_publicaciones if total_publicaciones else 0
    
    return {
        'total_publicaciones' : total_publicaciones,
        'total_likes'         : total_likes,
        'total_comentarios'   : total_comentarios,
        'promedio_likes'      : promedio_likes,
        'promedio_comentarios': promedio_comentarios
        }
    
def menu_estadisticas(usuarios_dict, posteos):
    """
    Muestra un menú interactivo recursivo para que el usuario seleccione qué métricas desea ver.
    """
    print('\n--- Menú de Estadísticas ---')
    print('1. Métricas de Usuarios')
    print('2. Métricas de Publicaciones')
    print('3. Análisis de Hashtags de Spam')  
    print('4. Volver al Menú Principal')
    opciones=[1,2,3,4]
    opcion = obtener_opcion(opciones)

    if opcion == 1:
        metricas = calcular_metricas_usuarios(usuarios_dict)
        mostar_metricas_usuarios(metricas)

    elif opcion == 2:
        metricas = calcular_metricas_posts(posteos)
        mostrar_metricas_post(metricas)

    elif opcion == 3:
        print("\n** Análisis de Hashtags de Spam **")
        analizar_spam_hashtags()  # Llamada a la función de análisis de spam
    
    elif opcion == 4:
        return  # Sale del menú de estadísticas # Llamada recursiva

def main_metricas():
    usuarios_dict, posteos = cargar_datos()
    
    if usuarios_dict and posteos:
        menu_estadisticas(usuarios_dict, posteos)
    else:
        print("No se pudieron cargar los datos. Asegúrate de que los archivos existan y contengan información válida.")