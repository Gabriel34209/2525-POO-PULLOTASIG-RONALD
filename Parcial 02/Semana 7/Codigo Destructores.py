import time

class ArchivoTemporal:
    """
    Clase que demuestra el uso de un destructor (__del__) para la limpieza de recursos.
    Simula la apertura y cierre de un archivo temporal.
    """
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase ArchivoTemporal.

        Abre (simula) un archivo temporal y lo prepara para su uso.
        """
        self.nombre_archivo = nombre_archivo
        print(f"--- CONSTRUCTOR: Archivo '{self.nombre_archivo}' abierto para escritura.")
        # Simulación de recursos o preparación inicial
        self.contenido = []

    def agregar_linea(self, linea):
        """Método para simular la escritura en el archivo."""
        self.contenido.append(linea)
        print(f"  > Añadida línea: '{linea}' al archivo '{self.nombre_archivo}'")

    def __del__(self):
        """
        Destructor de la clase ArchivoTemporal.

        Se ejecuta automáticamente justo antes de que la instancia del objeto
        sea destruida por el recolector de basura de Python. Se utiliza para
        realizar tareas de limpieza, como cerrar el archivo (simulado) y liberar
        recursos.
        """
        print(f"--- DESTRUCTOR: Cerrando y eliminando (simulado) el archivo '{self.nombre_archivo}'.")
        # Simulación de la liberación de recursos o cierre del archivo
        time.sleep(0.2) # Pequeña pausa para simular el proceso de cierre
        print(f"--- DESTRUCTOR: Archivo '{self.nombre_archivo}' cerrado y recursos liberados.")

# --- Demostración del Destructor ---

print("Paso 1: Creando una instancia de ArchivoTemporal.")
# El constructor __init__ se activa aquí.
mi_log_file = ArchivoTemporal("log_sistema.txt")

print("\nPaso 2: Agregando algunas líneas al archivo.")
mi_log_file.agregar_linea("Inicio de la sesión.")
mi_log_file.agregar_linea("Error crítico detectado.")
mi_log_file.agregar_linea("Sesión finalizada.")

print("\nPaso 3: Terminando el uso del archivo.")
print("Eliminando explícitamente la instancia 'mi_log_file'...")
# Al usar 'del', se elimina la referencia al objeto, lo que provoca que
# el destructor __del__ se active inmediatamente para esta instancia.
del mi_log_file

print("\nPaso 4: La instancia ha sido eliminada.")
print("Fin del programa. El destructor ya se ejecutó para el archivo log_sistema.txt.")

# Nota: Si no se usa 'del mi_log_file' explícitamente, el destructor se ejecutaría
# automáticamente cuando el programa finalizara y la instancia dejara de tener referencias.