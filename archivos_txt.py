def inicializar_txt(nombre_archivo, matriz):
    cadena = f'{matriz}'
    with open(nombre_archivo, 'w', encoding='UTF-8') as arch:
        arch.write(cadena + '\n')
    