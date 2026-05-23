# ============================================================
# Curso: Fundamentos de Programacion - Codigo: 213022
# Fase 5 - Evaluacion Final POA
# Problema 2: Gestion de precios con promocion - Menu restaurante
# ============================================================

# Datos iniciales: matriz con 6 productos
# Formato: [Nombre del Producto, Categoria, Precio Base]
menu = [
    ["Cafe Americano",    "Bebidas",   8500],
    ["Jugo de Naranja",   "Bebidas",   12000],
    ["Hamburguesa Clasica","Comidas",  25000],
    ["Ensalada Caesar",   "Ensaladas", 18000],
    ["Limonada Natural",  "Bebidas",   15000],
    ["Brownie de Chocolate","Postres", 9000],
]

# Parametros de la promocion
CATEGORIA_OBJETIVO = "Bebidas"
UMBRAL_PRECIO = 10000   # precio base debe ser mayor a este valor
DESCUENTO = 0.15        # 15% de descuento


# ============================================================
# Modulo (funcion): calcular precio final de un producto
# ============================================================
def calcular_precio_final(nombre, categoria, precio_base):
    """
    Calcula el precio final de un producto aplicando descuento si corresponde.

    Parametros:
        nombre      (str): Nombre del producto.
        categoria   (str): Categoria del producto.
        precio_base (int): Precio original del producto en pesos.

    Retorna:
        tuple: (precio_final, descuento_aplicado)
            precio_final       (float): Precio despues de la promocion.
            descuento_aplicado (bool): True si se aplico descuento, False si no.
    """
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        precio_final = precio_base * (1 - DESCUENTO)
        descuento_aplicado = True
    else:
        precio_final = precio_base
        descuento_aplicado = False

    return precio_final, descuento_aplicado


# ============================================================
# Programa principal: recorre la matriz y muestra resultados
# ============================================================
def main():
    print("=" * 60)
    print("   MENU DEL RESTAURANTE - PROMOCION ACTIVA")
    print(f"   Descuento: {int(DESCUENTO*100)}% en '{CATEGORIA_OBJETIVO}' con precio > ${UMBRAL_PRECIO:,}")
    print("=" * 60)
    print(f"{'Producto':<25} {'Categoria':<12} {'Precio Base':>12} {'Precio Final':>13} {'Promo':>6}")
    print("-" * 72)

    for producto in menu:
        nombre    = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        precio_final, descuento_aplicado = calcular_precio_final(nombre, categoria, precio_base)

        promo_texto = "SI" if descuento_aplicado else "No"

        print(f"{nombre:<25} {categoria:<12} ${precio_base:>10,} ${precio_final:>11,.0f} {promo_texto:>6}")

    print("=" * 60)
    print("  Programa finalizado correctamente.")
    print("=" * 60)


# Punto de entrada del programa
if __name__ == "__main__":
    main()