"""  Notas  """

def agregar(x):
    lista=[]
    if x==4:
        y = input("Ingrese el nombre del usuario: ")
        lista.append(y)
        y= input("Ingrese el apellido del usuario: ")
        lista.append(y)
        y=int(input("Ingrese los seguidores del usuario: "))
        lista.append(y)
        y=int(input("Ingrese los seguidos del usuario: "))
        lista.append(y)
    return lista
        
        


 
def leer(matriz):
    seleccion = int(input("Que matriz queres visualizar\n1. Para usuarios\n2. Para publicaciones\n3. Para post publicación\n"))
    while seleccion<=0 or seleccion>3:    
        print("el numero ingresado no está dentro de los numeros solicitados\n Por favor ingrese el numero nuevamente: ",end="")
        seleccion=int(input())
    if seleccion==1:
        print()
    elif seleccion==2:
        print()
    else:
        print()
    return 0
"""  
def actualizar():

def eliminar():

"""