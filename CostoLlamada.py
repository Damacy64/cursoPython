print("Programa costo de llamada")

duracion=0
precio=0
costo=0

precio=int(input("Cual es el precio de la llamada por minuto: "))
duracion=int(input("De cuanto fue la duracion de su llamada(ingrese en minutos): "))
costo= precio*duracion

print("El costo de la llamada es de: $" + str(costo))