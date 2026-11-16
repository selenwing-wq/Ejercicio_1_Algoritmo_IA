# Reto de IA · Ordenar tres números

Reto de Riwi: extender un programa que ordena dos números para que ordene **tres números enteros de menor a mayor**, usando solo `input`, `if`, `else` y comparaciones. Después, comparar nuestra solución con la de dos modelos de IA y decidir cuál es la mejor.

## Objetivo de aprendizaje

- Razonar las comparaciones de forma lógica (árbol de decisiones).
- Comprobar lo que propone una IA con casos de prueba, sin confiar en una respuesta solo porque suena segura.

## Restricciones

| Permitido | Prohibido |
|---|---|
| `input`, `int`, `print` | Listas |
| `if`, `else` | Ciclos (`for`, `while`) |
| Comparaciones (`<=`, `<`, `>`, `>=`) | `sorted()`, `sort()`, `min()`, `max()` |

## Estructura del proyecto

```
reto-ordenar/
├── ordenar.py     # Algoritmo propio (tres números)
├── README.md      # Este archivo
└── PROMPT.md      # Prompt estructurado para cualquier IA
```

## Cómo ejecutarlo

```bash
python ordenar.py
```

Ejemplo:

```
Primer número: 7
Segundo número: 2
Tercer número: 5
2 5 7
```

## Cómo funciona el algoritmo

1. Se comparan `a` y `b`.
2. Según el resultado, se compara el tercer número `c` contra el que quede en medio o al final.
3. Cada rama termina en uno de los **6 órdenes posibles** de tres números.
4. Se usa `<=` en lugar de `<` para que los **repetidos** no rompan el orden.

```
a <= b ?
├─ sí: b <= c ?
│   ├─ sí → a b c
│   └─ no: a <= c ?
│       ├─ sí → a c b
│       └─ no → c a b
└─ no: a <= c ?
    ├─ sí → b a c
    └─ no: b <= c ?
        ├─ sí → b c a
        └─ no → c b a
```

## La instrucción para los modelos de IA

Se copia igual en dos asistentes distintos:

> Escribe un programa en Python que pida tres números enteros y los muestre de menor a mayor. Usa solo input, if, else y comparaciones: sin listas, ciclos ni sorted(). Explica en tres líneas cómo funciona.

## Registro de pruebas

Marcar ✅ o ❌ según el resultado de cada solución.

| Caso | Entrada | Esperado | Mi algoritmo | Modelo A | Modelo B |
|---|---|---|---|---|---|
| Desordenados | 7, 2, 5 | 2, 5, 7 | ✅ | | |
| Desordenados (al revés) | 9, 5, 1 | 1, 5, 9 | ✅ | | |
| Repetidos | 5, 1, 5 | 1, 5, 5 | ✅ | | |
| Negativos | -3, 5, -1 | -3, -1, 5 | ✅ | | |
| Todos iguales | 4, 4, 4 | 4, 4, 4 | ✅ | | |

> Las columnas de los modelos se completan después de ejecutar el código que cada IA entregó.

## Discusión y elección

Responder de forma breve:

1. ¿Cuál solución pasó todas las pruebas?
2. ¿Alguna usó algo prohibido (listas, ciclos, `sorted()`, `min`/`max`)?
3. ¿Cuál es más fácil de leer?
4. **Solución elegida y por qué:** _(escribir aquí)_

## Nota

Ordenar una cantidad variable de números se resuelve más adelante con ciclos y listas. En este reto lo importante es razonar las comparaciones y verificar el trabajo de la IA.
