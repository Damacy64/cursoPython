print("Programa para determinar el promedio de los examenes")
print("Las calificaiones van del 0 al 10 por cada examen")

primer_examen=0
segundo_examen=0
tercer_examen=0
calificacion=0

primer_examen=int(input("Ingrese la calificacion del primer primer examen "))
segundo_examen=int(input("Ingrese la calificacion del segundo examen "))
tercer_examen=int(input("Ingrese la calificacion del tercer examen "))

primer_examen=(primer_examen/100)*25
segundo_examen=(segundo_examen/100)*25
tercer_examen=(tercer_examen/100)*50

calificacion=primer_examen+segundo_examen+tercer_examen
print("El promedio es de: " + str(calificacion))