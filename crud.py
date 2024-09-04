"""  Notas  """
#Funciones secundarias

def seleccionar_usuario(matriz):
    aux=0
    while aux!=-1:
        print("¿Que usuario deseas modificar?\nIngrese el numero de la fila: ",end="")
        aux=int(input())       #Se soliicita que usuario se quiere modificar comenzando desde 0
        if aux<0 or aux>len(matriz):     
            print("Usuario no encontrado")
        else:
            return aux

"""
def seleccionar_elemento():
"""      

# Funciones principales del CRUD
def agregar(eleccion):
    lista=[]
    if eleccion==1:
        x=["Usuario: ","Seguidores: ","Seguidos: ","Likes: ","Correo: "]
        for col in range(5):
            if col==0 or col==4:
                y=input(f"Ingrese {x[col]}")
                lista.append(y)
            else:
                y=int(input(f"Ingrese {x[col]}"))
                list.append
    else:
        x =["Hashtag: ","Cantidad de posteos: ","Veces compartido: ","Likes: ","s"]
        for col in range(4):
            y=input(f"Ingrese {x[col]}")
            lista.append(y)
    return lista


def leer(matriz):
    for fil in range(len(matriz)):
        print()
        for col in range(len(matriz[0])):
            print(f"|{matriz[fil][col]:^12}|",end="")
    print()
    return 0

def actualizar(matriz,usuario,modif):
    if modif == 0:
        x=input("Ingrese el nuevo usuario: ")
    elif modif ==1:
        x=input("Ingrese el nueva cantidad seguidores: ")
    elif modif==2:
        x=input("Ingrese la nueva cantidad de seguidos: ")
    else:
        x=input("Ingrese la nueva cantidad de likes: ")
    return x

def eliminar(matriz):
    print()





"""
def leer(matriz):
    seleccion = int(input("Que matriz deseas visualizar\n1. Para usuarios\n2. Para hashtags\n3. Para publicaciones\n"))
    while seleccion<=0 or seleccion>3:    
        print("el numero ingresado no está dentro de los numeros solicitados\n Por favor ingrese el numero nuevamente: ",end="")
        seleccion=int(input())
    cont=0
    if seleccion==1:
        for fil in range(len(matriz)):
            print()
            for col in range(len(matriz[0])):
                print(f"|{matriz[fil][col]:^12}|",end="")
        print()
    elif seleccion==2:
        for fil in range(len(matriz)):
            print()
            for col in range(len(matriz[0])):
                print(f"|{matriz[fil][col]:^12}|",end="")
        print()
    else:
        print()
    return 0
  """