SalarioI=int(input("¿Cual es su salario inicial? "))
años=int(input("¿Cuantos años lleva en la empresa? "))
contador=0

while contador<=años:
	SalarioI=((SalarioI/100)*10)+SalarioI
	contador+=1

print("El salario despues de "+ str(años)+" años es de "+ str(SalarioI))