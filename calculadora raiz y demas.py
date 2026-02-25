print("=== CALCULADORA EN PYTHON ===")

import math

# ===== FUNCIONES =====

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b

def raiz(a):
    if a < 0:
        return "Error: No se puede sacar raíz de número negativo"
    return math.sqrt(a)

def potencia(a, b):
    return a ** b

def porcentaje(a, b):
    return (a * b) / 100

def modulo(a, b):
    return a % b

def promedio(lista):
    if len(lista) == 0:
        return "Error: Lista vacía"
    return sum(lista) / len(lista)


# ===== MENÚ PRINCIPAL =====

while True:
    print("\n--- MENÚ ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz cuadrada")
    print("6. Potencia")
    print("7. Porcentaje")
    print("8. Módulo")
    print("9. Promedio")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "0":
        print("Gracias por usar la calculadora 😊")
        break

    elif opcion == "5":
        a = int(input("Ingresa el número: "))
        print("Resultado:", raiz(a))

    elif opcion == "9":
        numeros = input("Ingresa los números separados por espacio: ")
        lista = list(map(int, numeros.split()))
        print("Resultado:", promedio(lista))

    elif opcion in ["1", "2", "3", "4", "6", "7", "8"]:
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            print("Resultado:", resta(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicacion(a, b))
        elif opcion == "4":
            print("Resultado:", division(a, b))
        elif opcion == "6":
            print("Resultado:", potencia(a, b))
        elif opcion == "7":
            print("Resultado:", porcentaje(a, b))
        elif opcion == "8":
            print("Resultado:", modulo(a, b))

    else:
        print("Opción no válida")

