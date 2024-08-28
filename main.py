""" Notas: 

"""
import crud
import metricas

usuario = [["Nombre", "Apellido", "Seguidores", "Seguidos"]]
posteo = [[]]
post_publicacion = [[]]



# menu 
menu=0
while menu!=-1:
    print("1. para agregar")
    print("2. para leer ")
    print("3. para actualizar")
    print("4. para eliminar ")
    print("-1. para cancelar")
    menu=input("Ingrese un nemero: ")

    if menu==1:
        usuario.append(crud.agregar(len(usuario[0])))
        print(usuario)
    elif menu==2:
        crud.leer

