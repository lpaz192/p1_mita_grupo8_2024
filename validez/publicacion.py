from datetime import datetime

def validar_fecha(fecha):
    try:
        # Cambiar strtime por strptime
        datetime.strptime(fecha, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    except Exception as e:
        print(f'Error inesperado: {e}')
