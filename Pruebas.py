"""Suma basica"""

"""
uno = 19;dos = 25;tres = 62;cuatro=52
suma = uno+dos+tres+cuatro
print ("Hola, la suma es",suma)
promedio = suma / 4
print ("hola, ya hicimos tu promedio, el cual es:", promedio)
"""

"""Cadena de textos(internet)"""

"""
cadena1 = 'comillas simples'
print (cadena1)

cadena2 = "comillas dobles"
print (cadena2)

n = "Aprender"
a = "Python"
na = n + " " + a
print (na)
"""

"""Primer problema planteado en la UIS"""

"""
salario = 1000000; veinte = 0.2; quince = 0.15; cinco = 0.05
porveinte = salario*veinte; porquince = salario*quince; porcinco = salario*cinco
suma = porveinte+(2*porquince)+porcinco; resta = salario-suma
print ("la suma de los gastos es:", int(suma), "\n Lo que le queda es:", int(resta))
"""

"""Ejemplos 1 de internet"""

"""
b = ['2.36', 'elefante', 1010, 'rojo']
print(b)
catorce = b[0:3:2]
print(catorce)
"""

"""Ejercicio en clase"""


"""
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
    print("Lo sentimos, pero la nota ingresada no es valida")
"""

"""Ejecicio en clase 2"""


"""
primero = float(input("Digite su primer numero a revisar:\n"))
segundo = float(input("Digite su segundo numero a revisar:\n"))
tercero = float(input("Digite su tercer numero a revisar:\n"))

if primero > segundo and primero > tercero:
    print ("El numero mayor es: ",primero)
elif segundo > primero and segundo > tercero:
    print ("El numero mayor es: ", segundo)
elif tercero > primero and tercero > segundo:
    print ("El numero mayor es: ",tercero)
else:
    print ("Lo sentimos no hemos podido identificar cual es el numero mayor")
"""

"""Ejercicio en clase 3"""


"""
num1 = int(input("Ingrese por favor un numero:\n"))

if num1%2==0:
    print("El numero",num1, "es par")
else:
    print("El",num1,"es impar")
"""

"""Segundo problema planteado en la UIS"""


"""
peso = float(input("ingrese su peso en Kilos: \n"))
estatura = float(input("Ingrese su estatura en metros: \n"))
imc= peso/(estatura**2)

if imc < 18.5:
    print("Su estado es: Bajo peso",imc)
elif imc < 25:
    print("Su estado es: Normal", imc)
elif imc < 30:
    print("Su estado es: Sobrepeso", imc)
elif imc >= 30:
    print("Su estado es: Obeso", imc)
else:
    print("No se a podido validar.\n Revisa los datos ingresados")
"""

"""Ejemplos de internet"""


"""
key = "contraseña"
password = input("Introduce la contraseña:\n")

if key == password.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")
"""


""" Codigo copiado de internet"""


"""
print ("Bienvenidos a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres: \n")

if  tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t1- Albahaca\n\t2- Tofu\n")
    ingrediente = input ("Introduce el número del ingrediente que deseas agregar:\n")
    print("Pizza vegetariana con mozzarella, tomate y ", end=" ")
    if  ingrediente == "1":
        print("albahaca")
    else:
        print("tofu")
else:
    print("Ingrediente de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input ("Introduce el número del ingrediente que deseas agregar:\n")
    print("Pizza no vegetariana con mozzarella, tomate y ", end=" ")
    if  ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")    
"""
""" Codigo mio"""

#falta descubrir como llamar la informacion de \t, para que no aparezca solo el numero

print ("Bienvenidos a la pizzeria Bella Napoli.")
print("\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres: \n")
if  tipo == "1":
    print("Tamaños disponibles:\n\t1- Mediana - 6 porciones\n\t2- Grande - 8 porciones\n\t3- Extra grande - 12 porciones\n")
    tamaño = input("¿Seleccione el tamaño que desea?\n")
    print("Masas disponibles:\n\t1- Borde de queso\n\t2- Original\n\t3- Delgada crujiente\n\t4- Pan pizza")
    masa = input("¿Que tipo de masa desea?\n")
    print("¿Desea pasta de tomate?\n\t1- Si\n\t2- No")
    tomate = input()
    print("Quesos disponibles\n\t1- Mozarrella\n\t2- Doble crema")
    queso = input("¿Que queso desea?")
    print("Ingredientes de pizzas vegetarianas\n\t1- Albahaca\n\t2- Tofu\n")
    ingrediente = input ("Introduce el número del ingrediente que deseas agregar:\n")
    print("Su pedido es: Pizza vegetariana de tamaño ",tamaño,"con la masa ",masa,"con capa de tomate",tomate,"tipo de queso ",queso,"ingrediente", end=" ")
    if  ingrediente == "1":
        print("albahaca")
    else:
        print("tofu")
else:
    print("Tamaños disponibles:\n\t1- Mediana - 6 porciones\n\t2- Grande - 8 porciones\n\t3- Extra grande - 12 porciones\n")
    tamaño = input("¿Seleccione el tamaño que desea?\n")
    print("Masas disponibles:\n\t1- Borde de queso\n\t2- Original\n\t3- Delgada crujiente\n\t4- Pan pizza")
    masa = input("¿Que tipo de masa desea?\n")
    print("¿Desea pasta de tomate?\n\t1- Si\n\t2- No")
    tomate = input()
    print("Quesos disponibles\n\t1- Mozarrella\n\t2- Doble crema")
    queso = input("¿Que queso desea?")
    print("Ingrediente de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input ("Introduce el número del ingrediente que deseas agregar:\n")
    print("Su pedido es: Pizza no vegetariana de tamaño ",tamaño,"con la masa ",masa,"con capa de tomate",tomate,"tipo de queso ",queso,"ingrediente", end=" ")
    if  ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")