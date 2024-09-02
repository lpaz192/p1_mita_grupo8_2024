""" Notas: 

"""
import crud
import metricas
#Funciones
def eleccion():
    matriz_elegida=0
    while matriz_elegida!=1 and matriz_elegida!=2:
        print("En que matriz deseas realizar esta operación\n1. Usuarios\n2. Posteo")
        matriz_elegida=int(input("Seleccione: "))   #1 matriz de usuario   2. matriz de posteo
        if matriz_elegida !=1 and matriz_elegida !=2:
            print("Por favor ingrese un numero dentro de los solicitados")
    return matriz_elegida

usuario = [["Nombre", "Apellido", "Seguidores", "Seguidos"],
           ["Diego", "Lopez", "200", "340"],
           ["Carla","Aguilar","3000","800"]
           ]
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

        
    if menu==1:                   #agregar
        if eleccion()==1:
             usuario.append(crud.agregar(len(usuario[0])))  
        else:
            posteo.append(crud.agregar(len(posteo[0])))

    elif menu==2:                 #Leer
        crud.leer(usuario)  

    elif menu==3:                 #Actualizar
        contador=0
 
        if eleccion() == 1:        #Modificacion de usuarios
            usuario_modif=crud.seleccionar_usuario(usuario)
            while contador!=1:
                if contador==0:
                    print("Que elemento deseas modificar\n0. Nombre\n1.Apellido\n2. Seguidores")
                    modif=int(input("Seleccione: "))  #Se Solicita que elemento se quiere modificar comenzando desde 0
                    if modif<0 or modif>2:
                        print("Por favor ingrese un valor dentro del rango solicitado")
                    else:
                        contador+=1
            usuario[usuario_modif].pop(modif)         #Se elimina el elemento a modificar
            usuario[usuario_modif].insert(modif,crud.actualizar(usuario,usuario,modif))  #Se inserta el elemento modificado
        else:
            crud.actualizar(posteo)

    elif menu==4:                 #Eliminar
        if eleccion()==1:
            
            usuario_eliminar=crud.seleccionar_usuario(usuario)
            """
            crud.eliminar(usuario,usuario_eliminar)
            """
            usuario.pop(usuario_eliminar)
        else:
            crud.eliminar(posteo)
