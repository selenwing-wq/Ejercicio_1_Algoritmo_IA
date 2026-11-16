# Prompt estructurado · Reto "Ordenar tres números"

Copia todo lo que está dentro del bloque y pégalo en cualquier asistente de IA.

````
# ROL
Eres un instructor de programación en Python para principiantes. Explicas con claridad y verificas tu propio trabajo.

# CONTEXTO
Estoy en un bootcamp de programación (Riwi). El reto consiste en ordenar tres números enteros de menor a mayor usando solo decisiones (if/else). Parto de esta plantilla, que ordena dos números:

```python
a = int(input("Primer número: "))
b = int(input("Segundo número: "))

if a <= b:
    print(a, b)
else:
    print(b, a)
```

# TAREA
Extiende la plantilla para que pida un tercer número `c` y muestre los tres números de menor a mayor.

# RESTRICCIONES (obligatorias)
- Permitido: `input`, `int`, `print`, `if`, `else` y operadores de comparación.
- Prohibido: listas, ciclos (`for`, `while`), `sorted()`, `sort()`, `min()`, `max()`, funciones recursivas y librerías externas.
- Debe funcionar con números repetidos, negativos y todos iguales (usa `<=` donde corresponda).
- Salida: los tres números en una sola línea, separados por un espacio, de menor a mayor.

# ENTRADA Y SALIDA
- Entrada: tres enteros, pedidos uno por uno con `input`.
- Salida: `x y z`, con x <= y <= z.

# CASOS DE PRUEBA (todos deben pasar)
| Entrada | Salida esperada |
|---|---|
| 7, 2, 5 | 2 5 7 |
| 9, 5, 1 | 1 5 9 |
| 5, 1, 5 | 1 5 5 |
| -3, 5, -1 | -3 -1 5 |
| 4, 4, 4 | 4 4 4 |

# FORMATO DE RESPUESTA
Responde en este orden exacto:
1. **Código** completo en un solo bloque de Python, con comentarios breves.
2. **Cómo funciona** en exactamente tres líneas.
3. **Verificación:** recorre mentalmente cada caso de prueba y escribe la salida que produce tu código, marcando ✅ o ❌.
4. **Chequeo de restricciones:** confirma en una línea que no usaste nada prohibido.

# CRITERIOS DE CALIDAD
- Cubre los 6 órdenes posibles de tres números, sin ramas repetidas ni faltantes.
- Código legible: nombres claros, indentación consistente, comentarios útiles.
- Si encuentras un caso que falla, corrígelo antes de responder.
````

## Variante corta (la instrucción original del reto)

Para la comparación entre modelos, usa exactamente esta instrucción, igual en ambos:

> Escribe un programa en Python que pida tres números enteros y los muestre de menor a mayor. Usa solo input, if, else y comparaciones: sin listas, ciclos ni sorted(). Explica en tres líneas cómo funciona.
