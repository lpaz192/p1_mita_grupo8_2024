""" Notas: 

"""
import crud
import metricas
import json

#Funciones
def eleccion():
    matriz_elegida=0
    while matriz_elegida!=1 and matriz_elegida!=2:
        print("En que matriz deseas realizar esta operación\n1. Usuarios\n2. Hashtags")
        matriz_elegida=int(input("Seleccione: "))                          #1 matriz de usuario   2. matriz de posteo
        if matriz_elegida !=1 and matriz_elegida !=2:
            print("Por favor ingrese un numero dentro de los solicitados")
    return matriz_elegida

def ordenamiento(matriz):
    matriz.sort()
    return matriz

#Matrices
usuario = [["Usuario",     "Seguidores", "Seguidos", "Likes",  "Correo"],
           ["Diego.lopez", 2000,       800,       1000,  "diegolopez@gmail.com"],  #Estos son ejemplos aleatorios
           ["carlitaa",    5000,       500,       8000,  "carlaguilar@gmail.com"]]

hashtags = [["hashtag","Cantidad de posteos","Veces compartido","Likes"],
            ["#UADELabs","2000","10000","50000"]]                          #Estos son ejemplos aleatorios  

posteos = [[]]

""" Validador de email
import re

def validar_email(email):
    # Expresión regular para validar un correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(patron, email):
        return True
    else:
        return False

# Ejemplo de uso
emails = [
    "usuario@dominio.com",
    "usuario@dominio",        # Inválido
    "usuario@dominio.co.uk",  # Válido
    "usuario@dominio..com",   # Inválido
    "usua@rio@dominio.com",   # Inválido
    "usuario@dominio.c",      # Inválido
    "usuario@dominio.corporate" # Válido
]

for email in emails:
    if validar_email(email):
        print(f"'{email}' es un correo electrónico válido.")
    else:
        print(f"'{email}' no es un correo electrónico válido.")

"""

#Menu 
menu=0
while menu!=-1:
    print("1. Para agregar")
    print("2. Para leer ")
    print("3. Para actualizar")
    print("4. Para eliminar ")
    print("5. Para ordenar")
    print("-1. Para cancelar")
    menu=int(input("Ingrese un numero: "))

        
    if menu==1:                   #agregar
        matriz_elegida = eleccion()
        if matriz_elegida == 1:
            usuario.append(crud.agregar(matriz_elegida))  
        else:
            hashtags.append(crud.agregar(matriz_elegida))

    elif menu==2:                 #Leer
        seleccion = int(input("Que matriz deseas visualizar\n1. Para usuarios\n2. Para hashtags\n3. Para publicaciones\n"))
        while seleccion<=0 or seleccion>3:    
            print("el numero ingresado no está dentro de los numeros solicitados\n Por favor ingrese el numero nuevamente: ",end="")
            seleccion=int(input())
        if seleccion==1:
            crud.leer(seleccion,usuario) 
        elif seleccion==2:
            crud.leer(seleccion,hashtags) 
        else:
            crud.leer(seleccion,posteos)

    elif menu==3:                 #Actualizar
        contador=0
 
        if eleccion() == 1:        #Modificacion de usuarios
            usuario_modif=crud.seleccionar_usuario(usuario)
            usuario_elemnto_modif=crud.seleccionar_elemento_usuario()        #Se elimina el elemento a modificar
            usuario[usuario_modif][usuario_elemnto_modif]=crud.actualizar(usuario,usuario_modif,usuario_elemnto_modif)  #Se inserta el elemento modificado
        else:
            crud.actualizar(hashtags)

    elif menu==4:                 #Eliminar
        if eleccion()==1:
            
            usuario_eliminar=crud.seleccionar_usuario(usuario)
            """
            crud.eliminar(usuario,usuario_eliminar)
            """
            usuario.pop(usuario_eliminar)
        else:
            crud.eliminar(hashtags)



