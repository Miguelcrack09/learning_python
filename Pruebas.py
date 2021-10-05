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

"""

#while
"""
i = 1
while i <=5:
    print(i)
    i=i+1

#segundo ejemplo

manzanas = 5
cont_manzanas = 0

print("Se ha iniciado el carrito. En total hay " + str(cont_manzanas) + " manzanas.")

while cont_manzanas < manzanas:
    cont_manzanas = cont_manzanas + 1
    print("Se ha agregado una manzana a la canasta. Ahora hay " + str(cont_manzanas) + " manzanas")
"""
#for
"""
for i in range(3):
    print(i)

#segundo ejemplo

print("Se ha iniciado el carrito. En total hay: 0 manzanas.")

for i in range(1, 6):
    print("Se ha agregado una manzana a la canasta. Ahora hay " + str(i) + " manzanas")
"""

#Ejercicios
#primero
"""
n = int(input("Digite un número natural\n"))
suma = 0
for x in  range (1, n+1):
    suma = suma + x

print(suma)
"""
#segundo
"""
n = int(input("Digite un numero:\n"))

for i in range (1, 11):
    mul = n * i
    print(n, " * ", i ," = ", mul)
"""
#tercero
"""
numero = int(input("Digite un numero a revisar:\n"))
contador = 0
verificar=False
if numero >= 2:
    for i in range(1, numero+1):
        if numero%i==0:
            contador=contador + 1
        elif contador >= 3:
            verificar=True
       
    if contador == 2 and verificar == False:
        print("El numero", numero, "es primo")
    else:
        print("El numero", numero, "no es primo")    
else:
    print("El numero 1 no es considerado un numero primo")
"""
#cuarto
"""
i = 1
cont_par=0
cont_impar=0
while i<=10:
    i = i + 1
    cont_numero = int(input("Digite un numero:\n")) 
    if cont_numero % 2 == 0:
        print("El número", cont_numero," es par\n")
        cont_par=cont_par+1
    else:
        print("El número", cont_numero," no es par\n")
        cont_impar=cont_impar+1
print("En total selecciono", cont_par, "números pares")
print("En total selecciono", cont_impar, "números impares")
"""

#Reto 3
"""
usuario = "admin"
contraseña = "MisionTic2021"
intento = 1
opcion = 5
empleados = str([ ])
lis_empleado = str( )
visitantes = str([])
lis_visitantes = str( )
while opcion > 0 and intento <= 3:
    usu = str(input( ))
    con = str(input( ))
    if usu == usuario and con == contraseña:
        print ("Usuario: "+usu)
        print ("Contraseña: "+con+"")
        while opcion != 0:
                print("\n------Menú de registro de personal-----\n1. Registrar ingreso de empleado.\n2. Ver empleados ingresados.\n3. Registrar ingreso de visitantes.\n4. Ver visitantes ingresados.\n\n0. Salir\n")
                opcion = int(input("Ingresa un número válido de opción del menú: "))
                if opcion == 1:
                    while empleados != "SALIR":
                        empleados = input("Ingresa el nombre del empleado (Si no desea agregar más, oprime la tecla SALIR): ")
                        if empleados != "SALIR":
                            lis_empleado=lis_empleado+empleados+","
                elif opcion == 2:
                       print("Los empleados registrados son: " + lis_empleado + "\n") 
                elif opcion == 3:
                    while visitantes != "SALIR":
                        visitantes = input("Ingresa el nombre del visitante (Si no desea agregar más, oprime la tecla SALIR): ")
                        if visitantes != "SALIR":
                            lis_visitantes=lis_visitantes+visitantes+","  
                elif opcion == 4:
                    print("Los visitantes registrados son: " + lis_visitantes + "\n")                
                elif opcion == 0:
                    print("¡Hasta luego!")          
    else:
        intento = intento + 1
        print("(Error en las credenciales)")
    if intento > 3:
        print ("Lo sentimos ya alcanzo el limite de tres intentos")
"""

#Ejercicios de acumuladores

#Primero

"""
acumulador = 0
for i in range (1, 1000):
    i = int(input("Ingrese número: "))
    if i > 0:
        acumulador=acumulador+i
    else:
        break
print ("La suma es: ", acumulador)
"""

#Segundo

"""
acumulador=0
numero = 1
while  numero != 0:
    numero = int(input("Ingrese un numero: "))
    acumulador = acumulador+numero
print("La suma es: ", acumulador)      
"""

#Interes mio

"""
veces = int(0)
numero = int(input("Numero de veces que desea doblar: "))
dato = int(input("Cual es el dato inical que desea aumentar: "))
while veces <= numero:
    dato = dato * 2
    veces = veces + 1
    print (veces," = ",dato)
"""  
#67108864
#18.446.744.073.709.551.616

#Clase

"""
def kms_to_ms(velocity_kms):
    kilometer_in_meter = 1000
    seconds_in_hour = 3600
    return velocity_kms * kilometer_in_meter / seconds_in_hour
print(kms_to_ms(50))


def factorial (n):
    if n == 1:
        return n
    elif n < 1:
        return (" No existe")
    else:
        return n *factorial (n-1)
a=int(input("Digite un número: "))

res = factorial(a)
print (a," != ", res)

num_mayor = 0
num_menor = 0
for i in range(0 ,6):
    numero = int(input("Ingrese un numero:"))
    i = i + 1
    if numero > num_mayor:
        num_mayor = numero
        num_menor = numero
    elif numero < num_menor:
        num_menor = numero
print (num_mayor)
print (num_menor)    
"""

#Ejercicios para contadores: 
# 1. Cuenta los pares que existen entre dos números ingresados por el usuario. 
"""
numero_pri=int(input("Dijite el primer numero a revizar: "))
numero_seg=int(input("Digite el segundo número que desea revizar: "))
i = numero_pri
contador = 0
for i in range(numero_pri,(numero_seg-1)):
    i = i + 1
    num_par = i % 2
    if num_par == 0:
        contador = contador + 1
print ("Hay",contador,"números pares entre",numero_pri,"y",numero_seg)
"""
# 2.Cuenta la cantidad de estudiantes que aprobaron la materia con un valor mayor a 3.5 de 20 datos ingresados
"""
contador = 0
no_paso = 0
for i in range (1,20):
    nota = float(input("Digite la nota del estudiante:"))
    if nota >= 3.5 and nota <=5.0:
        contador = contador + 1
    elif nota < 3.5 and nota > 0:
        no_paso = no_paso + 1
    else:
        print("La nota ingresada no corresponde")

print ("La cantidad de estudiantes aprovados es:", contador)
"""
#Ejercicios para acumuladores: 
# 1.Programa en Python que suma los pares que existen entre dos números ingresados por el usuario. 
"""
numero_pri=int(input("Dijite el primer numero a revizar: "))
numero_seg=int(input("Digite el segundo número que desea revizar: "))
i = numero_pri
acumulador= 0
for i in range(numero_pri,(numero_seg-1)):
    i = i + 1
    num_par = i % 2
    if num_par == 0:
        acumulador = acumulador + i
print ("La suma de los números pares entre",numero_pri,"y",numero_seg,"es:",acumulador)
"""
# 2. Sumar las notas obtenidas en un curso por un alumno para después determinar su promedio
#  y si es menor a 3.5 mostrar un mensaje que diga “Reprobó”
"""
veces = int(input("Cuantas notas tiene el estudiante?: "))
notas = 0
for i in range (veces+1):
    nota = float(input("Digite las notas del estudiante:"))
    notas = notas + nota
    i = i + 1
    if i == veces:
        promedio = notas / veces
        if promedio <= 3.5:
            print("Reprobó", promedio)
"""
#Ejercicio para bandera: Programa en Python que calcula suma de los primeros 10 números pares 
# y el producto de los primeros 10 números impares simultáneamente.
"""
bandera = True
contador = 0
suma_impar = 0
prod_par =1
while bandera == True:
    contador = contador + 1
    par = contador%2
    if par != 0:
        suma_impar = suma_impar + contador
    elif par == 0:
        prod_par = prod_par * contador    
    elif contador == 22:
        bandera = False
print (suma_impar)
print (prod_par)
"""

#Reto 3 para coderunner

"""
usuario = "admin"
contraseña = "MisionTic2021"
lis_empleado = str( )
lis_visitantes = str( )
intento = 0
opcion = 10
while opcion > 0 and intento <= 3:
    usu = str(input( ))
    con = str(input( ))
    if usu == usuario and con == contraseña:
        print ("Usuario: "+usu)
        print ("Contraseña: "+con)
        while opcion != 0:
                print("\n------Menú de registro de personal-----\n1. Registrar ingreso de empleado.\n2. Ver empleados ingresados.\n3. Registrar ingreso de visitantes.\n4. Ver visitantes ingresados.\n\n0. Salir\n")
                opcion = int(input())
                print("Ingresa un número válido de opción del menú:",opcion)
                if opcion >= 0 and opcion <=4:
                    empleados = str([ ])
                    visitantes = str([])
                    if opcion == 1:
                        while empleados != "SALIR":
                            empleados = input()
                            print("Ingresa el nombre del empleado (Si no deseas agregar más, oprime la tecla SALIR):", empleados)
                            if empleados != "SALIR":
                                lis_empleado=lis_empleado+empleados+","
                    elif opcion == 2:
                           print("Los empleados registrados son: " + lis_empleado) 
                    elif opcion == 3:
                        while visitantes != "SALIR":
                            visitantes = input()
                            print("Ingresa el nombre del visitante (Si no deseas agregar más, digite SALIR):",visitantes)
                            if visitantes != "SALIR":
                                lis_visitantes=lis_visitantes+visitantes+","  
                    elif opcion == 4:
                        print("Los visitantes registrados son: " + lis_visitantes)       
                    elif opcion == 0:
                        print("¡Hasta luego!")         
                else:
                    print("Por favor ingresa una opción válida")
    else:
        intento = intento + 1
        print ("Usuario: "+usu)
        print ("Contraseña: "+con)
        print("Credenciales incorrectas")
    if intento > 3:
        print ("Has agotado la cantidad de intentos, por favor inicie de nuevo el programa")

"""

#reto 4 



"""
def calcular_badejas(int,str):
        if str == "BC" or str == "A":
            bandejas=int/30
        elif str == "AA":
            bandejas=int/24
        elif str == "AAA":
            bandejas=int/12
        return bandejas


def clasificacion_huevos(list):
        conC=0
        conB=0
        conA=0
        conAA=0
        conAAA=0
        can=len(list)
        for i in range(can):
            if list[i]<46:
                conC=conC+1
            elif list[i]<53:
                conB=conB+1
            elif list[i]<60:
                conA=conA+1
            elif list[i]<67:
                conAA=conAA+1
            elif list[i]>=67:
                conAAA=conAAA+1
        bandeja_bc= int(calcular_badejas(conC+conB,"BC"))
        bandeja_a= int(calcular_badejas(conA,"A"))
        bandeja_aa= int(calcular_badejas(conAA,"AA"))
        bandeja_aaa= int(calcular_badejas(conAAA,"AAA"))
        datos = ("Tipo_huevos: A, numero_huevos: "+str(conA)+", numero_bandejas: "+str(bandeja_a)+"\nTipo_huevos: AA, numero_huevos: "+str(conAA)+", numero_bandejas: "+str(bandeja_aa)+"\nTipo_huevos: AAA, numero_huevos: "+str(conAAA)+", numero_bandejas: "+str(bandeja_aaa)+"\nTipo_huevos: BC, numero_huevos: "+str(conB+conC)+", numero_bandejas: "+str(bandeja_bc))
        return datos
import random
list=[]
for i in range(500):
    a= random.uniform(30,80)
    list.append(a)

print(list)
print (clasificacion_huevos(list))
#return print("Tipo_huevos:A, numero_huevos: "+str(new_lista[2])+", numero_bandejas:",bandejaA,"\nTipo_huevos:AA, numero_huevos: "+str(new_lista[3])+", numero_bandejas:",bandejaAA,"\nTipo_huevos:AAA, numero_huevos: "+str(new_lista[4])+", numero_bandejas:",bandejaAAA,"\nTipo_huevos:BC, numero_huevos: "+str(suma)+", numero_bandejas:",bandejabc)
#Tipo_huevos:A, numero_huevos:",new_lista[0],", numero_bandejas:",bandejaA    

"""

#calcular_bandejas
#todo el primer dato y le sumo el segundo
#al resultado lo divido en 30 y tomo la parte entera
#Para obterner las bandejas de la cadegoria A divido el dato almacenado en la casilla 2 de la lista new_lista en 30


#Función un elemento guardado

"""
multiplicacion = 0
def ejemplo (multiplicacion):  
    if numero > 10: 
        return numero*22
    elif numero <= 10:
        return numero / 6
print("funciono")        


for i in range(1,5):
    i+=1
    numero = int(input("Digite un valor: "))
    print (ejemplo(multiplicacion))
"""

#Ejemplos de lista y tuplas

"""
objetos = ["Celular","Vehiculos","Escritorio"]
numeros = [2,22,333,4444,55555]
elementos = ("Apartamento","Ascender","Bateria","Libro","Alfombra")
numero = (1,2,3,4,55)

print("Lista: ")
for i in range(3):
    print (objetos[i])
  
print ("Tupla: ")
for i in range (5):
    print (elementos[i])


A = {0,8,3,4,5}
B = {1,2,6,0,8}

print (A ^ B)
"""

#Reto 5
"""

def calculadoraMes(ahorros,persona):
    lista = ahorros.split(";")
    lista1 = calculo(lista [0].split(","))
    lista2 = calculo(lista [1].split(","))
    lista3 = calculo(lista [2].split(","))
    lista4 = calculo(lista [3].split(","))
    diccionario = {"Enero":lista1,"Febrero":lista2,"Marzo":lista3,"Abril":lista4}
    return persona,diccionario

def calculo(meses):
    suma = 0
    if meses[0] == "Enero":
        for i in range (1,len(meses)):
            suma = suma + int(meses[i])
    elif meses[0] == "Febrero":
        for i in range (1,len(meses)):
            suma = suma + int(meses[i])
    elif meses[0] == "Marzo":
        for i in range (1,len(meses)):
            suma = suma + int(meses[i])
    elif meses[0] == "Abril":
        for i in range (1,len(meses)):
            suma = suma + int(meses[i])
    return suma
print (calculadoraMes("Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4","daniel"))

"""
#Diccionarios

"""
diccionario ={"azul":"blue",
"rojo":"red",
"verde":"green",
"indentacion":"Organización",
"estadistica":"tablas",
"matematicas":"Multiplicación"}

# la estructura para agregar datos a un diccionario es: nombre[clave]=valor
diccionario["One piece"]="Anime favorito"
diccionario["Sakura"]="flor de cerezo"
diccionario["estado"]="condicion actual"
#.keys muestra solo las claves del diccionario
print (diccionario.keys())
#.values muestra solo los valores de las claves
print (diccionario.values())
#.items muestra toda la infromacion, separando cada clave y valor dentro de una tupla
print (diccionario.items())
"""

#la estructura funcion = def nombre(parametros)

"""
def mate (num1,num2):
    suma = num1 + num2 
    return suma

print (mate(1,2))
"""
def calcular_bandejas(A,AA,AAA,BC):
    #aqui tienes que poner los valores en tipo integer(int) de manera que solo te arroge un dato entero, sin decimales
    #que te quede asi por ejemplo:bandA=int(A/30), haces eso mismo con todos, y listo, solo le agregar el int
    bandA=A/30
    bandAA=AA/24
    bandAAA=AAA/12
    bandBC=BC/30
    return bandA,bandAA,bandAAA,bandBC
def clasificacion_huevos(lista):
    contA=0
    contAA=0
    contAAA=0
    contBC=0
    for i in lista:
        peso=i
        if peso>=53 and peso<60:
            contA=contA+1
        elif peso>=60 and peso<67:
            contAA+=1
        elif peso>=67:
            contAAA+=1
        elif peso <53:
            contBC+=1
    print('A:',contA)
    print('AA:',contAA)
    print('AAA:',contAAA)
    print('BC:',contBC)
    #En la linea que tienes aqui abajo ya haces perfectamente el llamado de las variables, ignora lo que te envie por el chat
    bandA,bandAA,bandAAA,bandBC = calcular_bandejas(contA,contAA,contAAA,contBC)
    #desde aqui para abajo debes colocar todo en una variable
    #aqui puedes ingresar al enunciado del reto y mirar la estructura de lo que debes imprimir, te guias por eso y los colocas 
    #que te quede asi:variable ="Tipo_huevos:A, numero_huevos: "+contA+", numero_bandejas:",bandA lo repites con todos los datos contAA etc y los asi pones los de todos los huevos
    print('Bandejas')
    print('A:',bandA)
    print('AA:',bandAA)
    print('AAA:',bandAAA)
    print('BC:',bandBC)
    #una vez ya tengas todo en varibales
    #usas el return, para poder devolver ese dato
    #que te quede asi:retun "variable"
    #y listo


print(clasificacion_huevos([46.5,50,60,65,47,80,12,43,34,67,65,64,66,55,54,50.65, 60.8, 58.7, 70.0, 49.8]))        

#FIN DE LA CLASES EN PYTHON



""""Prueba por interes"""














