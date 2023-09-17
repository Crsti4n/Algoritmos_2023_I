# Definición de la clase Persona
class Persona:
    # Atributos de la clase Persona
    cod_persona=''
    nombre=''
    apellido_paterno=''
    apellido_materno=''
    fecha_nacimiento=''
    # Constructor de la clase Persona
    def __init__(self, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
    
    # Métodos para obtener y establecer los atributos de la clase Persona (getters y setters)
    def get_cod_persona(self):
        return self.cod_persona
    
    def set_cod_persona(self,cod_persona):
        self.cod_persona=cod_persona
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nombre):
        self.nombre=nombre
    
    def get_apellido_paterno(self):
        return self.apellido_paterno
    
    def set_apellido_paterno(self,apellido_paterno):
        self.apellido_paterno=apellido_paterno
    
    def get_apellido_materno(self):
        return self.apellido_materno
    
    def set_apellido_materno(self,apellido_materno):
        self.apellido_materno=apellido_materno
    
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def set_fecha_nacimiento(self,fecha_nacimiento):
        self.fecha_nacimiento=fecha_nacimiento
    
    # Método para mostrar información de la persona
    def imprimir(self):
        cod_persona=self.cod_persona
        nombre=self.nombre
        apellido_paterno=self.apellido_paterno
        apellido_materno=self.apellido_materno
        fecha_nacimiento=self.fecha_nacimiento
        
        return f"{cod_persona},{nombre} {apellido_paterno}, {apellido_materno}, {fecha_nacimiento}"
