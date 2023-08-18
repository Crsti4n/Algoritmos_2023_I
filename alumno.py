from persona import Persona
from curso import Curso

class Alumno(Persona):
    codigo = ''
    facultad = ''
    año_ingreso = 0
    Curso = []

    def __init__(self, nombre, ap_paterno, ap_materno, dni, codigo, facultad, año_ingreso):
        super().__init__(nombre, ap_paterno, ap_materno, dni)
        self.codigo = codigo
        self.facultad = facultad
        self.año_ingreso = año_ingreso

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_facultad(self):
        return self.facultad

    def set_facultad(self, facultad):
        self.facultad = facultad

    def get_anio_ingreso(self):
        return self.año_ingreso

    def set_anio_ingreso(self, anio):
        self.año_ingreso = anio

    def imprimir(self):
        per_data = super().imprimir()
        codigo = self.codigo
        facultad = self.facultad
        año = self.año_ingreso
        return f'datos del alumno es : {per_data}, codigo de ingreso {codigo}, {facultad=}, el año de ingreso es: {año}'
    
    def agregar_curso(self, curso):
        self.Curso.append(curso)
    
    def remover_curso(self, curso_eliminar):
        for curso in self.Curso:
            if curso_eliminar.get_codigo() ==  curso.get_codigo():
                self.Curso.remove(curso)
            else:
                print('No se encuentra registrado el curso a eliminar')
        #2da forma
        if curso_eliminar in self.Curso:
                self.Curso.remove(curso_eliminar)
    
    #Mostrar cursos asignados
    def mostrar_cursos_asignados(self):
        cursos_asignados = [curso.get_nombre() for curso in self.Curso]
        return cursos_asignados

    #Ingresar notas
    def ingresar_nota(self, curso, nota):
        for curso_alumno in self.Curso:
            if curso_alumno.get_codigo() == curso.get_codigo():
                curso_alumno.ingresar_notas(nota)
                return f"Nota ingresada para el curso {curso.get_nombre()}"
        return "El alumno no está registrado en ese curso"
    
    #Calcular promedio
    def calcular_promedio(self):
        total_notas = 0
        total_cursos = 0
        for curso in self.Curso:
            total_notas += sum(curso.notas)
            total_cursos += len(curso.notas)
        if total_cursos > 0:
            promedio = total_notas / total_cursos
            return promedio
        else:
            return 0
        




