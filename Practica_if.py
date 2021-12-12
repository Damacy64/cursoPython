print("Programa de calificaciones")

C_alumno=input("Ingrese la calificacion del alumno: ")

def evaluacion(nota):
	calificacion="Aprobado"
	if nota<=5:
		calificacion="Rerobado"
	return calificacion

print(evaluacion(int(C_alumno)))