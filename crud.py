"""  Notas  """
#Funciones secundarias
import json

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
        x =["Usuario: ","Seguidores: ","Seguidos: ","Likes: ","Correo: "]
        for col in range(5):
            lista.append(input(f"Ingrese {x[col]}"))
    else:
        x =["Hashtags: ","Cantidad de posteos: ","Veces compartidos: ","Likes: "]
        for col in range(4):
            lista.append(input(f"Ingrese {x[col]}"))
            
    return lista


def leer(seleccion,matriz):
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