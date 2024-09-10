import re
patron_mail = r"^[a-zA-Z0-9_]{2,20}+@[a-zA-Z]{2,10}+\.[a-zA-Z]{2,10}"


#Funciones
def validar_mail(mail):
    return re.match(patron_mail, mail)

