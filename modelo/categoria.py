# Definición de la clase Categoria
class Categoria:
 # Atributos de la clase Categoria
    cod_categoria=''
    categoria=''
    # Constructor de la clase Categoria
    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria
    # Métodos para obtener y establecer los atributos de la clase Categoria (getters y setters)
    
    def get_cod_categoria(self):
        return self.cod_categoria 
      
    def set_cod_categoria(self,cod_categoria):
        self.cod_categoria=cod_categoria
    
    def get_categoria(self):
        return self.categoria  
      
    def set_categoria(self,categoria):
        self.categoria=categoria
        
        
    # Método para mostrar información de la categoría
    def mostra_datos(self):
        return f"Categoría: {self.categoria} {self.cod_categoria}"