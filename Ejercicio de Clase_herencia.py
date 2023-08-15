class Persona:
    nombre=''
    def __init__(self, nombre):
        self.nombre = nombre

class Docente(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

class Curso:
    codigo=''
    nombre=''
    docente=''
    notas=[]
    def __init__(self, codigo, nombre, docente):
        self.codigo = codigo
        self.nombre = nombre
        self.docente = docente
        self.notas = []

    def ingresar_nota(self, nota):
        self.notas.append(nota)

    def hallar_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def reporte(self):
        promedio = self.hallar_promedio()
        return f"Curso: {self.nombre}\nDocente: {self.docente.nombre}\nPromedio: {promedio}"

class Alumno(Persona):
    cursos=[]
    def __init__(self, nombre):
        super().__init__(nombre)
        self.cursos = []

    def agregar_curso(self, curso):
            self.cursos.append(curso)

# Crear objetos
docente1 = Docente("Juan Perez")
docente2 = Docente("Anna Méndez")
docente3 = Docente("Pedro Santos")
docente4 = Docente("Emilia Quiñones")
alumno = Alumno("Maria Rodriguez")


# Crear cursos

curso1 = Curso("C001", "Matemáticas", docente1)
curso2 = Curso("C002", "Historia", docente2)
curso3 = Curso("C003", "Física", docente4)
curso4 = Curso("C004", "Literatura", docente4)
curso5 = Curso("C005", "Química", docente1)
curso6 = Curso("C006", "Inglés", docente3)

# Agregar notas a los cursos
curso1.ingresar_nota(15)
curso2.ingresar_nota(14)
curso3.ingresar_nota(17)
curso4.ingresar_nota(13)
curso5.ingresar_nota(16)
curso6.ingresar_nota(20)

# Agregar cursos al alumno
alumno.agregar_curso(curso1)
alumno.agregar_curso(curso2)
alumno.agregar_curso(curso3)
alumno.agregar_curso(curso4)
alumno.agregar_curso(curso5)
alumno.agregar_curso(curso6)

# Mostrar reporte de todos los cursos del alumno
for curso in alumno.cursos:
    print(f'Alumno: {alumno.nombre}')
    print(curso.reporte())
    print("-" * 30)


    
     
        
