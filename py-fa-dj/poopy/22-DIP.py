#PRINCIPIO DE INVERSION DE DEPENDECIAS

#Establece que los modulos de alto nivel no tiene que depender de los de bajo nivel sino que los dos deben depender de las abstracciones.
#Las abstracciones no deben depeneder de los detalles sino que los detalles dependan de las absatracciones.

# class Diccionario:
#     def verificar_palabra(self,palabra):
#         #logica para verificar palabras
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
#     def corregir_texto(self, texto):
#         #usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificarOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass

class Diccionario(VerificarOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass
    
class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador = verificador
        
    def corregir_texto(self,texto):
    #usamos el verificador para corregir texto 