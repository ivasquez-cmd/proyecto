Documentación — Calculadora en Python
🧾 Descripción general

Esta aplicación es una calculadora de consola desarrollada en Python que permite realizar operaciones matemáticas básicas y algunas avanzadas mediante un menú interactivo.

El usuario selecciona una opción, introduce los valores solicitados y obtiene el resultado inmediatamente.

⚙️ Requisitos

Tener Python instalado (Python 3 recomendado)

Ejecutar el archivo desde la terminal o un entorno como VS Code, IDLE o PyCharm

▶️ Ejecución del programa

Abrir la terminal o consola

Ubicarse en la carpeta donde está el archivo

Ejecutar:

python nombre_del_archivo.py

Al iniciar, aparecerá el título:

=== CALCULADORA EN PYTHON ===
🧮 Menú de opciones

El programa muestra continuamente un menú hasta que el usuario decida salir.

--- MENÚ ---
1. Suma
2. Resta
3. Multiplicación
4. División
5. Raíz cuadrada
6. Potencia
7. Porcentaje
8. Módulo
9. Promedio
0. Salir
📊 Operaciones disponibles
➕ 1. Suma

Suma dos números enteros.

Entrada:

Primer número

Segundo número

Resultado:
La suma de ambos valores.

➖ 2. Resta

Resta el segundo número al primero.

✖️ 3. Multiplicación

Multiplica dos números.

➗ 4. División

Divide el primer número entre el segundo.

⚠️ Si el segundo número es 0, el programa mostrará:

Error: No se puede dividir entre 0
√ 5. Raíz cuadrada

Calcula la raíz cuadrada de un número.

⚠️ Si el número es negativo:

Error: No se puede sacar raíz de número negativo
🔼 6. Potencia

Eleva un número a la potencia indicada.

Ejemplo:
2 elevado a 3 = 8

📉 7. Porcentaje

Calcula el porcentaje de un número.

Fórmula utilizada:

(a * b) / 100

Ejemplo:
20% de 150 = 30

🔁 8. Módulo

Obtiene el residuo de una división.

Ejemplo:
10 % 3 = 1

📊 9. Promedio

Calcula el promedio de varios números.

Entrada:
Los números deben escribirse separados por espacios.

Ejemplo:

10 20 30 40

⚠️ Si no se ingresan números:

Error: Lista vacía
🚪 0. Salir

Finaliza la ejecución del programa y muestra:

Gracias por usar la calculadora 😊
