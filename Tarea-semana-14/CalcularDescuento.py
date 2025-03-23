def calcular_descuento(precio, porcentaje):
    """
    Calcula el descuento y el precio final basado en el precio original y el porcentaje de descuento.

    Parámetros:
        precio (float): El precio original del producto.
        porcentaje (float): El porcentaje de descuento a aplicar.

    Retorna:
        tuple: Contiene el monto del descuento y el precio final después de aplicar el descuento.
    """
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return descuento, precio_final


def main():
    # ============================================================
    # CONFIGURACIÓN: Modifica estos valores para calcular el descuento.
    # ============================================================
    precio_producto = 600  # Precio original del producto en dólares.
    porcentaje_descuento = 20  # Porcentaje de descuento a aplicar.

    # ============================================================
    # FIN DE LA CONFIGURACIÓN
    # ============================================================

    # Cálculo del descuento y el precio final utilizando la función definida.
    descuento, precio_final = calcular_descuento(precio_producto, porcentaje_descuento)

    # Muestra de resultados en la consola con formato.
    print("Resumen del cálculo de descuento:")
    print(f"Precio original: ${precio_producto:.2f}")
    print(f"Porcentaje de descuento: {porcentaje_descuento}%")
    print(f"Monto descontado: ${descuento:.2f}")
    print(f"Precio final: ${precio_final:.2f}")


if __name__ == "__main__":
    main()