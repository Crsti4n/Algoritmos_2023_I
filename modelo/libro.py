# Definición de la clase Libro
class Libro:
    # Atributos de la clase Libro
    codigo_libro=''
    titulo=''
    año=''
    tomo=''
    categoria=''
    
    # Constructor de la clase Libro
    def __init__(self, codigo_libro, titulo, año, tomo):
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.año = año
        self.tomo = tomo
    
    # Métodos para obtener y establecer los atributos de la clase Libro (getters y setters)
    def get_codigo_libro(self):
        return self.codigo_libro
    
    def set_codigo_libro(self,codigo_libro):
        self.codigo_libro=codigo_libro
    
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self,titulo):
        self.titulo=titulo
    
    def get_año(self):
        return self.año
    
    def set_año(self,año):
        self.año=año
    
    def get_tomo(self):
        return self.tomo
    
    def set_tomo(self,tomo):
        self.tomo=tomo
    
# Método para asignar una categoría al libro
    def asignar_categoria(self, categoria):
        self.categoria = categoria

# Método para asignar un autor al libro
    def asignar_autor(self, autor):
        self.autor = autor
        
# Método para mostrar información del libro
    def imprimir(self):
        titulo = self.titulo
        codigo_libro = self.codigo_libro
        año = self.año
        tomo = self.tomo
        categoria = self.categoria
        return f"Título:{titulo},Código={codigo_libro} Año: {año}, Tomo: {tomo}, Categoría:{categoria} "
