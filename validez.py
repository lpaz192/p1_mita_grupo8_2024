import re
from datetime import datetime

patron_mail = r"^[a-zA-Z0-9_]{2,20}+@[a-zA-Z]{2,10}+\.[a-zA-Z]{2,10}"


#Funciones
def validar_mail(mail):
    return re.match(patron_mail, mail)

def validar_fecha(fecha):
    try: 
        datetime.strtime(fecha, '%Y-%m-%d')
        return True 
    except ValueError:
        return False