# exercici 1
# “Un programa "hola món" és un programa d'ordinador que simplement
# imprimeix el text “¡Hola, món!" (en anglès "Hello, world!") a un dispositiu
# de sortida (normalment el monitor). En algunes tradicions, especialment
# en el món anglosaxó, és el primer exercici típic per a estudiants
# d'un llenguatge de programació. ”

print("Exercici 1:\n")
print("Hola Món!")
input("\nPolsa intro per continuar.")

# exercici 2
# a)Realitza un programa en Python en el qual es declaren les variables
# senceres x i y. Assigna'ls els valors 144 i 999 respectivament. A
# continuació, mostra per pantalla el valor de cada variable,
# la suma, la resta, la multiplicació, la divisió,
# la divisió sencera i la resta de la divisió sencera.

x = 144
y = 999

print("Exercici 2:\na)\n")

print("Valor de x:", x)
print("Valor de y:", y, "\n")

print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicació:", x * y)
print("Divisió:", x / y)
print("Divisió sencera:", x // y)
print("Resta de la divisió:", x % y)

input("\nPolsa intro per continuar.")

# b) Modifica el programa anterior per a demanar
# els valors de les variables x i y a l'usuari.

print("b)")

x = int(input("Posa-li un valor a x:\n"))
y = int(input("Posa-li un valor a y:\n"))

print("Valor de x:", x)
print("Valor de y:", y, "\n")

print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicació:", x * y)
print("Divisió:", x / y)
print("Divisió sencera:", x // y)
print("Resta de la divisió:", x % y)

input("\nPolsa intro per continuar.")

# exercici 3
# Un col·legi desitja saber el percentatge de xiquets i el percentatge de
# xiquetes que hi ha al curs actual.
# L’usuari introduirà el número de xiquets i de xiquetes.
# Realitza un programa en Python per a este propòsit.

print("Exercici 3:\n")

xiquets = int(input("Introdueix el nombre de xiquets:\n"))
xiquetes = int(input("Introdueix el nombre de xiquetes:\n"))

total = xiquets + xiquetes
percentatge_xiquets = (xiquets / total) * 100
percentatge_xiquetes = (xiquetes / total) * 100

print("\nEl percentatge de xiquets és:", round(percentatge_xiquets), "%")
print("El percentatge de xiquetes és:", round(percentatge_xiquetes), "%")

input("\nPolsa intro per continuar.")

# exercici 4
# Realitza un convertidor d'euros a dòlars.
# La quantitat d'euros que es vol convertir a dòlars ha de ser introduïda per
# teclat.

print("Exercici 4:\n")
euros = float(
    input("Introdueix la quantitat " "d'euros que vols convertir a dòlars:\n")
)
dollars = euros * 1.18
print("\n", euros, "euros són", round(dollars, 2), "dòlars.")
input("\nPolsa intro per continuar.")

# exercici 5
# Realitza un programa en Python que calcule la nota que fa falta obtindre al
# segon examen de l’assignatura Introducció a la Programació per obtindre la
# nota mitjana desitjada.
# S’ha que tindre en compte que la nota del primer examen és el 40% de la
# nota final i la del segon examen un 60%.

print("Exercici 5:\n")
nota1 = float(input("Introdueix la nota del primer examen:\n"))
nota_final_desejada = float(
    input("Introdueix la nota " "final que desitges obtindre:\n")
)
nota2 = (nota_final_desejada - (nota1 * 0.4)) / 0.6
print(
    "\nPer obtindre una nota final de",
    nota_final_desejada,
    "necessites una nota de",
    round(nota2, 2),
    "en el segon examen.",
)
input("\nPolsa intro per continuar.")

# exercici 6
# Realitza un programa en Python que, suposant que les variables x, y, z són
# de tipus float, assigne a z el valor que indica la fórmula:
# z = (1 + (x^2 / y)) / (x^3 / (1 + y))

print("Exercici 6:\n")

x = float(input("Introdueix el valor de x:\n"))
y = float(input("Introdueix el valor de y:\n"))
z = float((1 + (x**2 / y)) / (x**3 / (1 + y)))

print("\nEl valor de z és:", z)

input("\nPolsa intro per continuar.")

# exercici 7
# Realitza un programa en Python que, donades dos variables numèriques A i
# B, que l’usuari deu teclejar, intercanvie els valors de les dos variables i
# mostre per pantalla el que valen al final les dos variables.

print("Exercici 7:\n")

A = input("Introdueix el valor de A:\n")
B = input("Introdueix el valor de B:\n")
print("\nAbans de l'intercanvi:")
print("A =", A)
print("B =", B)
A, B = B, A
print("\nDesprés de l'intercanvi:")
print("A =", A)
print("B =", B)

input("\nPolsa intro per continuar.")

# exercici 8
# Sense executar el programa, ¿que s’imprimix per consola? Fes una traça del
# programa (debug) per comprovar-ho.

print("Exercici 8:\n")

a, b, c = 12, 8, 6
print(a, b, c)

a = c
print(a, b, c)

c += b
print(a, b, c)

a = b + c
print(a, b, c)

a += 1
b += 1
print(a, b, c)

c = a + b
a += 1
b += 1
print(a, b, c)

print("\nPolsa intro per continuar.")

# exercici 9
# si s'executa el següent block d'instruccions,
# ¿es produïx una divisió per zero?

print("Exercici 9:\n")

j = -2
b = (j > 0) and (1 / (j + 2) > 10)

print(b)

print(
    "\nNo es produeix una divisió per zero perquè la primera "
    "condició és falsa, per tant, no s'executa la segona condició."
)

input("\nPolsa intro per continuar.")

# exercici 10
# Sense executar el programa, ¿que s’imprimix per consola?

print("Exercici 10:\n")

print(str(123456 // 10) + " " + str(123456 % 10))
print(str(123456 // 100) + " " + str(123456 % 100))
print(str(123456 // 1000) + " " + str(123456 % 1000))
print(str(123456 // 10000) + " " + str(123456 % 10000))
print(str(123456 // 100000) + " " + str(123456 % 100000))

input("\nPolsa intro per continuar.")

# exercici 11
# Determinar el valor, true o false, de cada una de las següents expressions
# lògiques, assumint que el valor de las variables cont y limit és 10 y 20,
# respectivament

print("Exercici 11:\n")

cont = 10
limit = 20
print("a) (cont == 0) && (limit < 20)\nFalse")
print(
    "b) (limit >= 20) || (cont < 5)\nTrue (en python es fa servir 'or' "
    "en lloc de '||')"
)
print("c) ((limit / (cont - 10)) > 7) || (limit < 20)")
print("ZeroDivisionError, i false")
print("d) (limit <= 20) || ((limit / (cont - 10)) > 7)\nTrue")
print("e) ((limit / (cont - 10)) > 7) && (limit < 0)")
print("ZeroDivisionError, i false")
print("f) (limit < 0) && ((limit / (cont-10)) > 7)\nFalse")

input("\nPolsa intro per acabar.")
