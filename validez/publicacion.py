
from datetime import datetime

def validar_fecha(fecha):
    try:
        # Cambiar strtime por strptime
        datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False