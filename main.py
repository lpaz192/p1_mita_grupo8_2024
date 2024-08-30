""" Notas: 

"""
import crud
import metricas

usuario = [["Nombre", "Apellido", "Seguidores", "Seguidos"],
           ["Diego", "Lopez", "200", "340"]]
posteo = [[]]
post_publicacion = [[]]



# menu 
menu=0
while menu!=-1:
    print("1. Para agregar")
    print("2. Para leer ")
    print("3. Para actualizar")
    print("4. Para eliminar ")
    print("-1. Para cancelar")
    menu=int(input("Ingrese un numero: "))

    if menu==1:
        usuario.append(crud.agregar(len(usuario[0])))
        print(usuario)
    elif menu==2:
        crud.leer(usuario)
    elif menu==3:
        print("que matriz deseas modificar\n1. Usuarios\n2. Posteo")
        lista=int(input("Seleccione: "))
        if lista ==1:
            print("Que elemento deseas modificar\n1. Nombre\n2.Apellido\n3. Seguidores")
            modif=int(input("Seleccione: "))
            crud.actualizar(usuario)

