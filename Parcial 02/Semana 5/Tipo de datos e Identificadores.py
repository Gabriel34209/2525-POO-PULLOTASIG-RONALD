# Este programa convierte una longitud de metros a diferentes unidades (kilómetros, centímetros, pulgadas).
# Permite al usuario introducir un valor en metros y luego muestra las conversiones.

def convertir_unidades_longitud():
    """
    Función principal para convertir unidades de longitud.
    Solicita al usuario una longitud en metros y realiza las conversiones.
    """
    print("--- Convertidor de Unidades de Longitud ---")

    # Solicitar la longitud al usuario (tipo de dato: string inicialmente)
    longitud_metros_str = input("Introduce la longitud en metros (ej. 10.5): ")

    # Validar si la entrada es un número (tipo de dato: boolean para el control)
    es_numero_valido = False
    try:
        longitud_metros = float(longitud_metros_str) # Convertir a float
        es_numero_valido = True
    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número.")
        # No continuamos con las conversiones si la entrada no es un número
        return

    # Asegurarse de que la longitud sea positiva
    if not es_numero_valido or longitud_metros < 0:
        print("Error: La longitud debe ser un número positivo.")
        return

    # Definir factores de conversión (tipo de dato: float)
    FACTOR_METROS_A_KILOMETROS = 0.001 # 1 metro = 0.001 kilómetros
    FACTOR_METROS_A_CENTIMETROS = 100 # 1 metro = 100 centímetros
    FACTOR_METROS_A_PULGADAS = 39.3701 # 1 metro = 39.3701 pulgadas

    # Realizar las conversiones (operaciones con float)
    longitud_kilometros = longitud_metros * FACTOR_METROS_A_KILOMETROS
    longitud_centimetros = longitud_metros * FACTOR_METROS_A_CENTIMETROS
    longitud_pulgadas = longitud_metros * FACTOR_METROS_A_PULGADAS

    # Mostrar los resultados al usuario (tipo de dato: string para la salida formateada)
    print(f"\n--- Resultados de la Conversión ---")
    print(f"Longitud original: {longitud_metros:.2f} metros") # .2f para formatear a 2 decimales
    print(f"En kilómetros: {longitud_kilometros:.4f} km") # .4f para más precisión en km
    print(f"En centímetros: {longitud_centimetros:.2f} cm")
    print(f"En pulgadas: {longitud_pulgadas:.2f} in")

    # Ejemplo de uso de un booleano para una condición simple (aunque no estrictamente necesario aquí)
    es_longitud_grande = longitud_metros > 1000 # Si la longitud es mayor a 1000 metros
    if es_longitud_grande:
        print("\n¡Es una longitud considerable!")
    else:
        print("\nEs una longitud menor.")

# Punto de entrada del programa
if __name__ == "__main__":
    convertir_unidades_longitud()