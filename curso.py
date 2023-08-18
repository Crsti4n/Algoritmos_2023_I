from docente import Docente

class Curso:
    codigo = ''
    nombre = ''
    notas = []

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_codigo(self):
        return self.codigo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def calcularPromedio(self, notas):
        if len(notas) > 0:
            return sum(notas) / len(notas)
        else:
            print("el Tamano del arreglo es igual a 0")

    def ingresar_notas(self, nota):
        if (len(self.notas) <= 4):
            self.notas.append(nota)

        else:
            print('se registraron todas las notas')
    
    def asignar_docente(self, docente):
        self.docente = docente
    
    def mostrar_docente(self):
        return self.docente
    
    def reporte(self):
        promedio = self.calcularPromedio(self.notas)
        return f"Reporte del curso {self.nombre}\nPromedio de notas: {promedio:.2f}"
