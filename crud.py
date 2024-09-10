"""  Notas  """
#Funciones secundarias
import json,validez,re

def seleccionar_usuario(matriz):
    aux=0
    while aux!=-1:
        print("¿Que usuario deseas modificar?\nIngrese el numero de la fila: ",end="")
        aux=int(input())       #Se soliicita que usuario se quiere modificar comenzando desde 0
        if aux<0 or aux>len(matriz):     
            print("Usuario no encontrado")
        else:
            return aux

def seleccionar_elemento_usuario():
    modif=-1
    while modif<0 or modif>2:
        print("Que elemento deseas modificar\n0. Usuario\n1.Seguidores\n2. Seguidos\n3. Likes\n4. Correo")
        modif=int(input("Seleccione: "))  #Se Solicita que elemento se quiere modificar comenzando desde 0
        if modif<0 or modif>2:
           print("Por favor ingrese un valor dentro del rango solicitado")
        return modif
"""
def seleccionar_elemento():
"""      

# Funciones principales del CRUD
def agregar(eleccion):
    lista,aux=[],""
    if eleccion==1:
        comparacion= lambda nombre:re.match(r"^[a-zA-Z_]{2,20}",nombre)
        x =["Usuario: ","Seguidores: ","Seguidos: ","Likes: ","Correo: "]
        for col in range(5):
            if col == 0:
                aux=input(f"Ingrese {x[col]}")
                while comparacion(aux)==None:
                    aux=input("Ingrese un nombre valido: ")
            elif col == 4:
                aux=input(f"Ingrese {x[col]}")
                while validez.validar_mail(aux)==None:
                    aux=input("Ingrese un mail valido: ")
                lista.append(aux)  
            else:   
                lista.append(input(f"Ingrese {x[col]}"))
    else:
        x =["Hashtag: ","Cantidad de posteos: ","Veces compartidos: ","Likes: "]
        comparacion= lambda palabra:re.match(r"^#[a-zA-Z0-9-_.]{1,20}",palabra)
        for col in range(4):  
            if col == 0:
                aux=input(f"Ingrese {x[col]}")
                while comparacion(aux)==None:
                    aux=input("Ingrese un Hashtag valido: ")
                lista.append(aux)
            else: 
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

def actualizar(modif):
    if modif == 0:
        comparacion= lambda palabra:re.match(r"[a-zA-Z-_.]{1,20}",palabra)
        aux=input("Ingrese el nuevo usuario: ")
        while comparacion(aux)==None:
            aux=input("Ingrese un nuevo nombre valido: ")
        return aux
    elif modif ==1:
        aux=int(input("Ingrese el nueva cantidad seguidores: "))
        return aux
    elif modif==2:
        aux=int(input("Ingrese la nueva cantidad de seguidos: "))
        return aux
    elif modif==3:
        aux=int(input("Ingrese la nueva cantidad de likes: "))
        return aux 
    else:
        aux=input("Ingrese el nuevo correo: ")
        while validez.validar_mail(aux)==None:
            aux=input("Ingrese un mail valido: ")
        return aux

def eliminar(matriz):
    print()