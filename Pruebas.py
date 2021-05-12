"""uno = 19;dos = 25;tres = 62;cuatro=52
suma = uno+dos+tres+cuatro
print ("Hola, la suma es",suma)
promedio = suma / 4
print ("hola, ya hicimos tu promedio, el cual es:", promedio)

cadena1 = 'comillas simples'
print (cadena1)

cadena2 = "comillas dobles"
print (cadena2)

n = "Aprender"
a = "Python"
na = n + " " + a
print (na)

salario = 1000000; veinte = 0.2; quince = 0.15; cinco = 0.05
porveinte = salario*veinte; porquince = salario*quince; porcinco = salario*cinco
suma = porveinte+(2*porquince)+porcinco; resta = salario-suma
print ("la suma de los gastos es:", int(suma), "\n Lo que le queda es:", int(resta))


b = ['2.36', 'elefante', 1010, 'rojo']
print(b)
catorce = b[0:3:2]
print(catorce)


nombre = input("Nombre del estudiante: ")
nota = float(input("cual es la nota del estudiante: "))

if nota > 0 and nota < 5:
    print("Lo sentimos ",nombre,"tu estado es: SUSPENDIDO")
elif nota < 7:
    print("Felicidades", nombre,"tu estado es: APROBADO - Sigue mejorando")
elif nota <9:
    print ("Felicitades",nombre,"su estado es: Notable")
elif nota <= 10:
    print ("Felicitades",nombre,"su estado es: SOBRESALIENTE")
else: 
    print("Lo sentimos, pero la nota ingresada no es valida")"""

primero = float(input("Digite su primer numero a revisar:"))
segundo = float(input("Digite su segundo numero a revisar:"))
tercero = float(input("Digite su tercer numero a revisar:"))

if primero > segundo and primero > tercero:
    print ("El numero mayor es: ",primero)
elif segundo > primero and segundo > tercero:
    print ("El numero mayor es: ", segundo)
elif tercero > primero and tercero > segundo:
    print ("El numero mayor es: ",tercero)
else:
    print ("Lo sentimos no hemos podido identificar cual es el numero mayor")

