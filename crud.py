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
    if eleccion==5:
        y = input("Ingrese el nombre del usuario: ")
        lista.append(y)
        y= input("Ingrese los seguidores del usuario: ")
        lista.append(y)
        y=(input("Ingrese los seguidos del usuario: "))
        lista.append(y)
        y=(input("Ingrese los likes del usuario: "))
        lista.append(y)
        y=input("Ingrese el correo del usuario")
        lista.append(y)
    else:
        x =["nombre","cantidad","s","2","s"]
        for col in range(eleccion):
            lista.append(input("Ingrese ",x[col]))
        y= input("Ingrese ek nombre del hashtag: ")
        lista.append(y)
        y=input("Ingrese la cantidad de posteos hechos: ")
        lista.append(y)
        y=input("Ingrese ")
    return lista


def leer(matriz):
    seleccion = int(input("Que matriz queres visualizar\n1. Para usuarios\n2. Para hashtags\n3. Para publicaciones\n"))
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
        print()
    else:
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