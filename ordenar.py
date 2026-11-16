# ordenar.py · ordenar tres números de menor a mayor
# Restricciones del reto: solo input, if, else y comparaciones.
# Sin listas, ciclos ni sorted().

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

# Usamos <= (y no <) para que los números repetidos queden bien ordenados.
if a <= b:
    if b <= c:
        # a <= b <= c
        print(a, b, c)
    else:
        # b > c, falta ubicar a respecto de c
        if a <= c:
            # a <= c < b
            print(a, c, b)
        else:
            # c < a <= b
            print(c, a, b)
else:
    # a > b
    if a <= c:
        # b < a <= c
        print(b, a, c)
    else:
        # a > b y a > c: a es el mayor, falta comparar b con c
        if b <= c:
            # b <= c < a
            print(b, c, a)
        else:
            # c < b < a
            print(c, b, a)
