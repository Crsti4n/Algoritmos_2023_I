# Definición de la clase Autor que hereda de Persona
from modelo.persona import Persona

class Autor(Persona):
    # Atributos adicionales de la clase Autor
    cod_autor=''
    pais=''
    editorial=''
    # Constructor de la clase Autor
    def __init__(self, cod_persona,cod_autor, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, pais, editorial):
        super().__init__(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial
# Métodos para obtener y establecer los atributos de la clase Autor (getters y setters)
   
    def get_cod_autor(self):
        return self.cod_autor
      
    def set_cod_autor(self,cod_autor):
        self.cod_autor=cod_autor
    
    def get_pais(self):
        return self.pais
    
    def set_pais(self,pais):
        self.pais=pais
    
    def get_editorial(self):
        return self.editorial  
      
    def set_editorial(self,editorial):
        self.editorial=editorial

# Método para mostrar información del autor
    def mostrar_datos(self):
        return f"Autor: {super().imprimir()}, País: {self.pais}, Editorial: {self.editorial}"