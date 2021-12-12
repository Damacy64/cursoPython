print("Programa del estacionamiento")

tiempo=0
costo=0

tiempo=int(input("Cuanto tiempo ocupo el estacionamiento? Ingrese el valor en horas: "))

if tiempo<=2 and tiempo>0:
	costo=tiempo*5.00
	print("El costo del boleto es de $" + str(costo) + " c/u.")
elif tiempo>=3 and tiempo<5:
	costo=tiempo*4.00
	print("El costo del boleto es de $" + str(costo) + " c/u.")
elif tiempo>=5 and tiempo<=10:
	costo=tiempo*3.00
	print("El costo del boleto es de $" + str(costo) + " c/u.")
else:
	costo=tiempo*2.00
	print("El costo del boleto es de $" + str(costo) + " c/u.")