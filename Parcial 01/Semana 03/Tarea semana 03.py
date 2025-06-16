# Programación Tradicional
# Ejemplo: Gestión de temperaturas diarias y cálculo del promedio semanal

# Definición de una variable global para almacenar las temperaturas
# La inicializamos como una lista vacía para ir añadiendo las temperaturas de cada día.
temperatures = []


# Función para registrar la temperatura de un día
def record_daily_temperature(temperature):
    global temperatures
    temperatures.append(temperature)
    print(f"Temperatura {temperature}°C registrada.")


# Función para calcular el promedio semanal de las temperaturas registradas
def calculate_weekly_average():
    global temperatures
    if not temperatures:  # Verificamos si la lista está vacía para evitar división por cero
        return 0

    total_temperature = sum(temperatures)
    average = total_temperature / len(temperatures)
    return average


# Uso de las funciones en la programación tradicional para el ejemplo de temperaturas

# Entrada de datos diarios (temperaturas)
record_daily_temperature(20)  # Lunes
record_daily_temperature(22)  # Martes
record_daily_temperature(21)  # Miércoles
record_daily_temperature(23)  # Jueves
record_daily_temperature(20)  # Viernes
record_daily_temperature(24)  # Sábado
record_daily_temperature(25)  # Domingo

# Calcular el promedio semanal
weekly_average = calculate_weekly_average()

# Imprimir el promedio semanal final
print("\nTemperaturas registradas:", temperatures)
print("Promedio semanal de temperatura (Tradicional):", weekly_average, "°C")