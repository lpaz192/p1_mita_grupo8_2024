import re
from datetime import datetime

patron_mail = r"^[a-zA-Z0-9_]{2,20}+@[a-zA-Z]{2,10}+\.[a-zA-Z]{2,10}"
patron_usuario = r"^[a-zA-Z_]{2,20}"


#Funciones labmda
validar_mail=lambda mail:re.match(patron_mail,mail)
validar_usuario= lambda nombre:re.match(patron_usuario,nombre)
"""
#Funciones
def validar_fecha(fecha):
    try: 
        datetime.strtime(fecha, '%Y-%m-%d')
        return True 
    except ValueError:
        return False
"""