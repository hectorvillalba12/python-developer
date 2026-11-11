#PRINCIPIO ABIERTO / CERRADO

#las entidades de software(clases,modulos,funciones, etc) tienen que esta abiertas para la extencion pero cerradas para la modificacion

class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"enviando un mensaje por mail a {self.usuario.email}")
        

class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando un sms a {self.usuario.sms}")
        
        
class NotificadorWhatsapp(Notificador):
    def Notificar(self):
        print(f"Enviando un whatsapp a {self.usuario.whatsapp}")