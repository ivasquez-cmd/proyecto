🧾 1. Resumen

La presente aplicación es una calculadora interactiva desarrollada en Python, diseñada para ejecutarse en entorno de consola. Permite realizar operaciones matemáticas básicas y algunas avanzadas mediante un sistema de menú sencillo e intuitivo.

Este documento tiene un doble propósito:

✔ Presentar el sistema de forma profesional a un cliente o evaluador
✔ Servir como material de aprendizaje para comprender el porqué de cada componente del programa

🎯 2. Objetivo del Sistema

Desarrollar una herramienta ligera que permita realizar cálculos matemáticos de forma rápida, confiable y sin necesidad de interfaz gráfica, optimizando recursos y facilitando su uso en cualquier equipo con Python instalado.

🖥️ 3. Alcance del Proyecto

La aplicación permite:

Realizar operaciones aritméticas básicas

Ejecutar cálculos matemáticos comunes

Procesar múltiples números para promedios

Validar errores frecuentes del usuario

Mantener ejecución continua hasta que se indique salida

No incluye:

Interfaz gráfica

Almacenamiento de resultados

Soporte para números decimales (solo enteros)

Funciones científicas avanzadas

⚙️ 4. Requisitos del Sistema
Software

Python 3.x

Consola o terminal de comandos

Hardware

Cualquier equipo capaz de ejecutar Python

Bajo consumo de memoria y CPU

🧠 5. Arquitectura del Programa (Cómo está construido)

El sistema se basa en tres pilares fundamentales:

🔹 5.1 Funciones independientes

Cada operación matemática está implementada en una función propia.

Por qué se hace así:

Facilita mantenimiento

Permite reutilización del código

Mejora la claridad y organización

Sigue buenas prácticas de programación modular

Ejemplo conceptual:

“Una función = una tarea específica”

🔹 5.2 Menú interactivo

El programa presenta opciones numeradas para que el usuario seleccione la operación deseada.

Por qué se usa un menú:

Hace el sistema intuitivo

Evita errores de comandos escritos manualmente

Permite escalar el programa agregando nuevas funciones

🔹 5.3 Bucle infinito (while True)

Mantiene la calculadora funcionando continuamente.

Por qué se utiliza:

Sin este ciclo, el programa terminaría después de una sola operación.

El ciclo solo se rompe cuando el usuario elige salir.

🔧 6. Descripción Detallada de Funcionalidades
➕ Suma

Calcula la adición de dos valores.

Por qué existe:
Es la operación aritmética básica más utilizada.

➖ Resta

Obtiene la diferencia entre dos números.

✖️ Multiplicación

Calcula el producto entre dos valores.

➗ División

Divide un número entre otro.

Validación implementada:

No permite división entre cero.

Por qué:
Matemáticamente es indefinida y generaría error en el programa.

√ Raíz cuadrada

Calcula la raíz cuadrada de un número usando la librería matemática de Python.

Restricción:
No admite números negativos.

Por qué:
La raíz de un número negativo no pertenece a los números reales.

🔼 Potencia

Eleva un número a otro (base^exponente).

Uso común:
Cálculos exponenciales y científicos básicos.

📉 Porcentaje

Calcula qué porcentaje representa un valor respecto a otro.

Fórmula aplicada:

porcentaje = (valor × porcentaje) / 100

🔁 Módulo

Obtiene el residuo de una división.

Por qué es útil:
Se usa frecuentemente en programación para:

Determinar números pares o impares

Ciclos repetitivos

Distribuciones

📊 Promedio

Calcula la media aritmética de varios números.

El usuario introduce los valores separados por espacios.

Por qué se usa una lista:

Permite manejar múltiples datos de forma flexible.

🔄 7. Flujo Operativo del Sistema

El programa inicia y muestra el título

Se despliega el menú de opciones

El usuario selecciona una operación

Se solicitan los datos necesarios

Se ejecuta el cálculo mediante la función correspondiente

Se muestra el resultado

El sistema vuelve al menú principal

Finaliza solo si el usuario elige salir

❗ 8. Manejo de Errores y Validaciones

Se implementaron controles básicos para garantizar estabilidad:

División entre cero

Raíz de números negativos

Lista vacía en promedio

Opción inválida del menú

Por qué es importante:

Evita que el programa se detenga abruptamente y mejora la experiencia del usuario.

💡 9. Justificación Técnica de Decisiones
Decisión	Motivo
Uso de funciones	Organización y reutilización
Menú numérico	Interfaz simple y clara
Bucle infinito	Uso continuo
Validaciones	Prevención de fallos
Entrada por teclado	Interacción directa
Librería math	Precisión matemática
🚀 10. Ventajas del Sistema

✔ Fácil de usar
✔ Ligero y rápido
✔ Compatible con cualquier sistema
✔ Código claro y mantenible
✔ Ideal para aprendizaje de programación

⚠️ 11. Limitaciones Actuales

Solo admite números enteros

No posee interfaz gráfica

No guarda historial

No permite operaciones encadenadas

🔮 12. Posibles Mejoras Futuras

Soporte para números decimales

Interfaz gráfica (GUI)

Historial de cálculos

Modo científico

Validación avanzada de entradas

Exportación de resultados

🏁 13. Conclusión

La calculadora desarrollada cumple eficazmente con su propósito como herramienta matemática básica y como proyecto de aprendizaje en programación. Su diseño modular, controlado y validado permite un funcionamiento estable y comprensible, facilitando futuras ampliaciones.

Además, el proyecto demuestra la correcta aplicación de conceptos fundamentales de Python como funciones, estructuras de control, manejo de datos y validación de entradas.
