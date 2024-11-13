from crud import cargar_usuarios, cargar_publicaciones
import json
from CuentasSPAM import clasificacion
from CuentasSPAM.clasificacion import analizar_spam_hashtags


def cargar_datos():
    usuarios_dict = cargar_usuarios()
    
    posteos = cargar_publicaciones()
    
    return usuarios_dict, posteos

def mostrar_metricas_usuarios(usuarios_dict):
    if not usuarios_dict:
        print("No hay usuarios registrados.")
        return
    
    total_usuarios   = len(usuarios_dict)
    total_seguidores = sum(user['Seguidores'] for user in usuarios_dict.values())
    total_seguidos   = sum(user['Seguidos'] for user in usuarios_dict.values())
    total_likes      = sum(user['Likes'] for user in usuarios_dict.values())
    
    promedio_seguidores = total_seguidores / total_usuarios if total_usuarios else 0
    promedio_seguidos   = total_seguidos / total_usuarios if total_usuarios else 0
    promedio_likes      = total_likes / total_usuarios if total_usuarios else 0
    
    print("\n** Métricas de Usuarios **")
    print(f"Total de usuarios:     {total_usuarios}")
    print(f"Total de seguidores:   {total_seguidores}")
    print(f"Total de seguidos:     {total_seguidos}")
    print(f"Total de likes:        {total_likes}")
    print(f"Promedio de seguidores por usuario:  {promedio_seguidores:.2f}")
    print(f"Promedio de seguidos por usuario:    {promedio_seguidos:.2f}")
    print(f"Promedio de likes por usuario:       {promedio_likes:.2f}")

def mostrar_metricas_posts(posteos):
    if not posteos:
        print("No hay publicaciones registradas.")
        return
    
    total_publicaciones =  len(posteos)
    total_likes =          sum(int(post[2]) for post in posteos)
    total_comentarios =    sum(int(post[3]) for post in posteos)
    
    promedio_likes       = total_likes / total_publicaciones if total_publicaciones else 0
    promedio_comentarios = total_comentarios / total_publicaciones if total_publicaciones else 0
    
    print("\n** Métricas de Publicaciones **")
    print(f"Total de publicaciones:  {total_publicaciones}")
    print(f"Total de likes:          {total_likes}")
    print(f"Total de comentarios:    {total_comentarios}")
    print(f"Promedio de likes por publicación:       {promedio_likes:.2f}")
    print(f"Promedio de comentarios por publicación: {promedio_comentarios:.2f}")

def menu_estadisticas(usuarios_dict, posteos):
    """
    Muestra un menú interactivo recursivo para que el usuario seleccione qué métricas desea ver.
    """
    print("\n** Menú de Estadísticas **")
    print("1. Métricas de Usuarios")
    print("3. Análisis de Hashtags de Spam")  
    print("4. Volver al Menú Principal")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            mostrar_metricas_usuarios(usuarios_dict)
            menu_estadisticas(usuarios_dict, posteos)  # Llamada recursiva
        elif opcion == 2:
            mostrar_metricas_posts(posteos)
            menu_estadisticas(usuarios_dict, posteos)  # Llamada recursiva
        elif opcion == 3:
            print("\n** Análisis de Hashtags de Spam **")
            analizar_spam_hashtags()  # Llamada a la función de análisis de spam
            menu_estadisticas(usuarios_dict, posteos)  # Llamada recursiva
        elif opcion == 4:
            return  # Sale del menú de estadísticas
        else:
            print("Opción no válida, por favor seleccione una opción válida.")
            menu_estadisticas(usuarios_dict, posteos)  # Llamada recursiva
    except ValueError:
        print("Entrada no válida, por favor ingrese un número.")
        menu_estadisticas(usuarios_dict, posteos)  # Llamada recursiva

def main_metricas():
    usuarios_dict, posteos = cargar_datos()
    
    if usuarios_dict and posteos:
        menu_estadisticas(usuarios_dict, posteos)
    else:
        print("No se pudieron cargar los datos. Asegúrate de que los archivos existan y contengan información válida.")