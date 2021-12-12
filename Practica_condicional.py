print("Asignaturas optativas en el año 2021")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesabilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in("informatica grafica", "pruebas de software","usabilidad y accesabilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura escogida no esta contemplada")