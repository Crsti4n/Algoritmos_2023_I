# from openpyxl import Workbook, load_workbook
from alumno import Alumno
from docente import Docente
from curso import Curso

lista_alumnos = []
# incluir los 5 registros por integrante
alumno1 = Alumno('juan', 'perez', 'rios', '86763456','0020200125', 'Informatica y Sistemas', 2020)
alumno2 = Alumno('karol', 'alvarado', 'obregon', '23457456','0020190105', 'Informatica y Sistemas', 2029)
alumno3 = Alumno('luis', 'gimenez', 'alvarez', '93457345','0020170112', 'Informatica y Sistemas', 2017)
alumno4 = Alumno('Miguel', 'Obama', 'Gomez', '12345678', '0020200845', 'Informatica y Sistemas', 2020)
alumno5 = Alumno('Maria', 'Lopez', 'Garcia', '87654321', '0020210572', 'Informatica y Sistemas', 2021)
alumno6 = Alumno('Carlos', 'Gonzalez', 'Rodriguez', '56789012', '0020190321', 'Informatica y Sistemas', 2019)
alumno7 = Alumno('Ana', 'Fernandez', 'Martinez', '78901234', '0020220102', 'Ingenieria Civil', 2022)
alumno8 = Alumno('Luis', 'Ramirez', 'Lopez', '23456789', '0020200976', 'Arquitectura', 2020)
alumno9 = Alumno('Laura', 'Sanchez', 'Perez', '45678901', '0020210847', 'Derecho', 2021)
alumno10 = Alumno('Diego', 'Rojas', 'Gutierrez', '34567890', '0020190849', 'Economia', 2019)
alumno11 = Alumno('Isabella', 'Cruz', 'Gomez', '56789012', '0020220950', 'Psicologia', 2022)
alumno12 = Alumno('Mariana', 'Fernandez', 'Diaz', '67890123', '0020201053', 'Medicina', 2020)
alumno13 = Alumno('Pedro', 'Santos', 'Morales', '89012345', '0020211156', 'Biologia', 2021)

lista_alumnos.append(alumno1)
lista_alumnos.append(alumno2)
lista_alumnos.append(alumno3)
lista_alumnos.append(alumno4)
lista_alumnos.append(alumno5)
lista_alumnos.append(alumno6)
lista_alumnos.append(alumno7)
lista_alumnos.append(alumno8)
lista_alumnos.append(alumno9)
lista_alumnos.append(alumno10)
lista_alumnos.append(alumno11)
lista_alumnos.append(alumno12)
lista_alumnos.append(alumno13)

#Docentes
lista_docente = []

docente1 = Docente('Ana', 'González', 'Martínez', '12345678', 'D12345', 'FIIS')
docente2 = Docente('Luis', 'Sánchez', 'Rodríguez', '98765432', 'D23456', 'FIIS')

lista_docente.append(docente1)
lista_docente.append(docente2)
#Cursos
lista_curso = []
curso1 = Curso('C001', 'Fundamentos de Investigación')
curso2 = Curso('C002', 'Gestión de Bases de Datos')
curso3 = Curso('C003', 'Estructura de datos y Algoritmos')
curso4 = Curso('C004', 'Redes I')

lista_curso.append(curso1)
lista_curso.append(curso2)
lista_curso.append(curso3)
lista_curso.append(curso4)


band = 0
for curso in lista_curso:
    if (band < 2):
        curso.asignar_docente(docente1)
    else:
        curso.asignar_docente(docente2)
    band += 1

for curso in lista_curso:
    docente = curso.mostrar_docente()
    print(docente.imprimir())

#for alumno in lista_alumnos:
#    for curso in lista_curso:
#        alumno.agregar_curso(curso)
#2da Forma
for curso in lista_curso:
    lista_alumnos[1].agregar_curso(curso)

# Mostrar cursos asignados 
for alumno in lista_alumnos:
    cursos_asignados = alumno.mostrar_cursos_asignados()
    print(f"Cursos asignados a {alumno.get_nombre()}: {cursos_asignados}\n")

# Ingresar notas al alumno
# Alumno 1
alumno1.ingresar_nota(curso1, 13)
alumno1.ingresar_nota(curso2, 16)
alumno1.ingresar_nota(curso3, 20)
alumno1.ingresar_nota(curso4, 14)

# Alumno 2
alumno2.ingresar_nota(curso1, 16)
alumno2.ingresar_nota(curso2, 18)
alumno2.ingresar_nota(curso3, 14)
alumno2.ingresar_nota(curso4, 16)

# Alumno 3
alumno3.ingresar_nota(curso1, 17)
alumno3.ingresar_nota(curso2, 14)
alumno3.ingresar_nota(curso3, 19)
alumno3.ingresar_nota(curso4, 18)

# Alumno 4
alumno4.ingresar_nota(curso1, 14)
alumno4.ingresar_nota(curso2, 15)
alumno4.ingresar_nota(curso3, 18)
alumno4.ingresar_nota(curso4, 17)

# Alumno 5
alumno5.ingresar_nota(curso1, 20)
alumno5.ingresar_nota(curso2, 12)
alumno5.ingresar_nota(curso3, 16)
alumno5.ingresar_nota(curso4, 19)

# Alumno 6
alumno6.ingresar_nota(curso1, 13)
alumno6.ingresar_nota(curso2, 19)
alumno6.ingresar_nota(curso3, 17)
alumno6.ingresar_nota(curso4, 15)

# Alumno 7
alumno7.ingresar_nota(curso1, 18)
alumno7.ingresar_nota(curso2, 14)
alumno7.ingresar_nota(curso3, 15)
alumno7.ingresar_nota(curso4, 13)

# Alumno 8
alumno8.ingresar_nota(curso1, 16)
alumno8.ingresar_nota(curso2, 20)
alumno8.ingresar_nota(curso3, 13)
alumno8.ingresar_nota(curso4, 17)

# Alumno 9
alumno9.ingresar_nota(curso1, 19)
alumno9.ingresar_nota(curso2, 17)
alumno9.ingresar_nota(curso3, 12)
alumno9.ingresar_nota(curso4, 18)

# Alumno 10
alumno10.ingresar_nota(curso1, 15)
alumno10.ingresar_nota(curso2, 13)
alumno10.ingresar_nota(curso3, 18)
alumno10.ingresar_nota(curso4, 14)

# Alumno 11
alumno11.ingresar_nota(curso1, 14)
alumno11.ingresar_nota(curso2, 16)
alumno11.ingresar_nota(curso3, 19)
alumno11.ingresar_nota(curso4, 20)

# Alumno 12
alumno12.ingresar_nota(curso1, 17)
alumno12.ingresar_nota(curso2, 18)
alumno12.ingresar_nota(curso3, 14)
alumno12.ingresar_nota(curso4, 15)

# Alumno 13
alumno13.ingresar_nota(curso1, 14)
alumno13.ingresar_nota(curso2, 18)
alumno13.ingresar_nota(curso3, 16)
alumno13.ingresar_nota(curso4, 17)

# Ingresar notas a los cursos de un alumno (Alumno 2)
#for curso in alumno2.Curso:
#    nota = float(input(f"Ingrese la nota para {alumno2.get_nombre()} en el curso {curso.get_nombre()}: "))
#    alumno2.ingresar_nota(curso, nota)

# Ingresar notas a los cursos de todos los alumnos
#for alumno in lista_alumnos:
#    for curso in alumno.Curso:
#        nota = float(input(f"Ingrese la nota para {alumno.get_nombre()} en el curso {curso.get_nombre()}: "))
#        alumno.ingresar_nota(curso, nota)

# Calcular el promedio de un alumno (Alumno 2)
promedio_alumno2 = alumno2.calcular_promedio()
print(f"Promedio de notas de {alumno2.get_nombre()}: {promedio_alumno2:.2f}")

# Calcular y mostrar el promedio de notas de todos los alumnos
#for alumno in lista_alumnos:
#    promedio_alumno = alumno.calcular_promedio()
#    print(f"Promedio de notas de {alumno.get_nombre()}: {promedio_alumno:.2f}")


