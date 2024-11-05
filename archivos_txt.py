def inicializar_txt(nombre_archivo, matriz):
    '''Crea el archivo de texto para la matriz de posteos
    '''
    with open(nombre_archivo, 'w', encoding='UTF-8') as arch:
        for fila in matriz:
            linea = ''.join([str(dato).ljust(24, ' ') for dato in fila])
            arch.write(linea + '\n')
    