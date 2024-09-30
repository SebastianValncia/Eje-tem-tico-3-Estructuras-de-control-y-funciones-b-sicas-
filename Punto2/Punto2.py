def obtener_numeros_unicos():
    """Solicita al usuario ingresar tres números enteros únicos."""
    numeros = set()

    while len(numeros) < 3:
        try:
            numero = int(input("Ingrese un número entero: "))
            if numero in numeros:
                print("Número repetido, por favor ingrese un número diferente.")
            else:
                numeros.add(numero)
        except ValueError:
            print("Entrada inválida, por favor ingrese un número entero.")

    return list(numeros)


def realizar_analisis(numeros):
    """Realiza el análisis de los números ingresados y devuelve un resumen."""
    mayor = max(numeros)
    menor = min(numeros)
    suma = sum(numeros)
    promedio = suma / len(numeros)

    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    cantidad_pares = len(pares)
    cantidad_impares = len(impares)

    mas_pares = cantidad_pares > cantidad_impares
    mas_impares = cantidad_impares > cantidad_pares

    return {
        "mayor": mayor,
        "menor": menor,
        "suma": suma,
        "promedio": promedio,
        "pares": pares,
        "impares": impares,
        "cantidad_pares": cantidad_pares,
        "cantidad_impares": cantidad_impares,
        "mas_pares": mas_pares,
        "mas_impares": mas_impares
    }


def mostrar_resumen(analisis):
    """Muestra un resumen detallado del análisis realizado."""
    print("\n--- Resumen del Análisis ---")
    print(f"Números ingresados: {analisis['pares'] + analisis['impares']}")
    print(f"Número mayor: {analisis['mayor']}")
    print(f"Número menor: {analisis['menor']}")
    print(f"Suma de los números: {analisis['suma']}")
    print(f"Promedio de los números: {analisis['promedio']:.2f}")
    print(f"Números pares: {analisis['pares']}")
    print(f"Números impares: {analisis['impares']}")
    print(f"Cantidad de pares: {analisis['cantidad_pares']}")
    print(f"Cantidad de impares: {analisis['cantidad_impares']}")

    if analisis['mas_pares']:
        print("Hay más números pares que impares.")
    elif analisis['mas_impares']:
        print("Hay más números impares que pares.")
    else:
        print("El número de pares y impares es igual.")


def main():
    """Función principal del programa."""
    print("Bienvenido al programa de análisis de números.")
    numeros = obtener_numeros_unicos()
    analisis = realizar_analisis(numeros)
    mostrar_resumen(analisis)


if __name__ == "__main__":
    main()



