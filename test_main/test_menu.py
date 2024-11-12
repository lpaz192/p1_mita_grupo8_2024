from validez import obtener_opcion

def test_opcion():
    lista=[1,2,3,4]
    assert obtener_opcion(lista) == True

'''
def pruebas_unitarias_metricas():
    usuarios_dict = {
        '001': {'Usuario': 'Martinn', 'Seguidores': 100, 'Seguidos': 150, 'Likes': 500},
        '002': {'Usuario': 'Diego.lopez', 'Seguidores': 200, 'Seguidos': 180, 'Likes': 800}
    }
    posteos = [
        ['2024-11-01', 'Post 1', '10', '5', '001'],
        ['2024-11-02', 'Post 2', '20', '10', '001'],
        ['2024-11-03', 'Post 3', '15', '7', '002']
    ]

    total_usuarios = len(usuarios_dict)
    total_seguidores = sum(user['Seguidores'] for user in usuarios_dict.values())
    total_likes = sum(user['Likes'] for user in usuarios_dict.values())
    promedio_seguidores = total_seguidores / total_usuarios if total_usuarios else 0
    promedio_likes = total_likes / total_usuarios if total_usuarios else 0

    total_publicaciones = len(posteos)
    total_likes_posteos = sum(int(post[2]) for post in posteos)
    promedio_likes_posteos = total_likes_posteos / total_publicaciones if total_publicaciones else 0

    assert total_usuarios == 2
    assert total_seguidores == 300
    assert total_likes == 1300
    assert promedio_seguidores == 150.0
    assert promedio_likes == 650.0
    assert total_publicaciones == 3
    assert total_likes_posteos == 45
    assert promedio_likes_posteos == 15.0
    
    return True

'''