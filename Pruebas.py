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
"""
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
"""

"""Ejercicios de refuerzo"""
#Primero
"""
numero = int(input("Digite un numero entero:\n"))
result = abs(numero)
if numero > 0:
    print("El numero ",numero," es positivo.\nCuyo valor absoluto es:",result)
else:
    print("El numero", numero, "es negativo.\nCuyo valor absoluto es:",result)
"""

#segundo
"""
print("Digite cuatro numeros a comparar:")
primero = float(input("-"));segundo = float(input("-"));tercero = float(input("-"));cuarto = float(input("-"))
if primero < segundo and primero < tercero and primero < cuarto:
    print("El numero menor es:",primero)
elif segundo < tercero and segundo < cuarto:
    print("El numero menor es:",segundo)
elif tercero < cuarto:
    print("El numero menor es:",tercero)
else:
    print("El numero menor es:",cuarto)
"""

#tercero
"""
año = int(input("Digite el año que desea revizar:\n"))
if año%4==0 and año%100!=0:
    print("El año digitado es bisiesto")
else:
    print("El año digitado no es bisiesto")
"""

#cuarto
"""
dia = str(input("Digite la letra inicial del dia.\n"))
if dia.lower() == "s":
    print("El día es:\nSabado")
elif dia.lower() == "d":
    print("El día es:\nDomingo")
elif dia.lower() == "l":
    print("El día es:\nLunes")
elif dia.lower() == "m":
    print("El día es:\nMartes")
elif dia.lower() == "x":
    print("El día es:\nMiercoles")
elif dia.lower() == "j":
    print("El día es:\nJueves")
elif dia.lower() == "v":
    print("El día es:\nViernes")
else:
    print("No se reconoce la letra ingresada, intentalo nuevamente")
"""

#QUINTO
"""
salario = int(input("¿Cuanto gana al mes?\n"))

if salario < 1000000:
    print(salario + 175000)
else:
    print(salario-(salario*0.05))


pregunta = input("¡Realizo horas extra?\n\t1- SI\n\t2- NO")

if pregunta == 1 or pregunta.lower() == "si":
    horas = input("¿Cuantas horas trabajo.?\n")

else:
    
"""

#condicionales iterativos
#variables de control
#primer ejemplo

suma_realizada = False
total = 0
a = 5
b = 10
if suma_realizada == False:
    total = a + b
    suma_realizada = True

if suma_realizada == True:
    print("Se ha realizado una suma y su valor es: " + str(total))


#segundo ejemplo

contagio_validado = "No"
paciente = "Lisa"

if contagio_validado == "No":
    print("La paciente" + paciente +"aun no se ha realizado su prueba para validar si se encuentra contagiada, se recomienda aplicar la prueba PCR")
    print("Aplicando prueba...")
    contagio_validado = "Pendiente"

if contagio_validado == "Pendiente":
    print(paciente + ", por favor valide en su correo el resultado de la prueba")
    contagio_validado = "Si"
if contagio_validado == "Si":
    print(paciente + ", de acuerdo a su resultado, por favor mantengase alejado de las personas")

#acumuladores
#primer ejemplo

lista_compras = " "
print("La abuelita esta escribiendo la lista de compras...")
lista_compras = lista_compras+"5 manzanas"
print("---Lista de compras---")
print(lista_compras)
lista_compras = lista_compras+", 3 lb cilantro"
print("---Lista de compras---")
print(lista_compras)
lista_compras = lista_compras+", 3 lb perejil"
print("---Lista de compras---")
print(lista_compras)


precio_manzana = 1200
cant_manzanas = 5
precio_cilantro = 200
cant_cilantro = 3
precio_perejil = 300
cant_perejil = 3
subtotal = 0
print ("Calculando el total de tu mercado...")
total_manzana = precio_manzana*cant_manzanas
print ("El valor total de las manzanas es: $"+str(total_manzana))
subtotal = subtotal + total_manzana
print("...El subtotal seria: $"+str(subtotal))
total_cilantro = precio_cilantro*cant_cilantro
print ("El valor total del cilantro es: $"+str(total_cilantro))
subtotal = subtotal + total_cilantro
print("...El subtotal seria: $"+str(subtotal))
total_perejil = precio_perejil*cant_perejil
print ("El valor total del perejil es: $"+str(total_perejil))
subtotal = subtotal + total_perejil
print("...El subtotal seria: $"+str(subtotal))

#contadores

cont_manzanas = 0
print("Se ha iniciado el carrito. En total hay: "+ str(cont_manzanas) + "manzanas.")
cont_manzanas = cont_manzanas + 1
print("Se ha agregado una manzana a la canasta. ahora hay " + str(cont_manzanas) + " manzanas.")
cont_manzanas = cont_manzanas + 1
print("Se ha agregado una manzana a la canasta. ahora hay " + str(cont_manzanas) + " manzanas.")
cont_manzanas = cont_manzanas + 1
print("Se ha agregado una manzana a la canasta. ahora hay " + str(cont_manzanas) + " manzanas.")
cont_manzanas = cont_manzanas + 1
print("Se ha agregado una manzana a la canasta. ahora hay " + str(cont_manzanas) + " manzanas.")
cont_manzanas = cont_manzanas + 1
print("Se ha agregado una manzana a la canasta. ahora hay " + str(cont_manzanas) + " manzanas.")