print("Verificacion de acceso")

nota_alumno= int(input("Introduce tu nota: "))

if nota_alumno<5:
	print("Insuficiente")
elif nota_alumno<6:
	print("Suficiente")
elif nota_alumno<7:
	print("Bien")
elif nota_alumno<9:
	print("Notable")
else:
	print("Sobresaliente")
	
print("El programa a finalizado")