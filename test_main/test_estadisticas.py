from metricas import calcular_metricas_posts, calcular_metricas_usuarios

usuarios_dict = {
        '001': {'Usuario': 'Martinn', 'Seguidores': 100, 'Seguidos': 150, 'Likes': 500},
        '002': {'Usuario': 'Diego.lopez', 'Seguidores': 200, 'Seguidos': 180, 'Likes': 800}
    }

posteos = [["ID-Post", "Fecha-de-publicación", "Cantidad-de-likes", "Cantidad-de-comentarios", "ID-Usuario", "Usuario",'Hashtag'],
        ['0001', '02-11-2012', '7000', '1000', '200', '0012', 'David_89','#Recetas'],
        ['0002', '15-05-2013', '5000', '1200', '300', '0020', 'Laura23', '#Viajes'],
        ['0003', '08-09-2020', '8500', '1500', '400', '0035', 'Carlos_G', '#Fitness'],
        ['0004', '23-03-2019', '9000', '1100', '500', '0048', 'Ana.P', '#Moda']
    ]

def test_mostrar_metricas_usuarios():
    assert calcular_metricas_usuarios(usuarios_dict) == {
            "total_usuarios"     : 2,
            "total_seguidores"   : 300,
            "total_seguidos"     : 330,
            "total_likes"        : 1300,
            "promedio_seguidores": 150.0,
            "promedio_seguidos"  : 165.0,
            "promedio_likes"     : 650.0,
        }

def test_mostrar_metricas_post():
    assert calcular_metricas_posts(posteos) == {
    'total_publicaciones' : 4,
    'total_likes'         : 29500,
    'total_comentarios'   : 4800,
    'promedio_likes'      : 7375.0,
    'promedio_comentarios': 1200.0
}
