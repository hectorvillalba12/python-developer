#PRINCIPIO DE SUSTITUCION DE LISKOV

#Establece que las clases derivadas tienen que ser subtituibles por sus clases base.

#ejem: si la clase B es subclase de A, la clase A tendria que poder utilizarse en todos los lugares donde B pueda utilizarse.

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "estoy volando"
    
class AveNoVoladora(Ave):
    pass


