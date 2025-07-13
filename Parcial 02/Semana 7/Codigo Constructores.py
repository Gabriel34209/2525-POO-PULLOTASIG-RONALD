class Producto:
    """
    Clase que demuestra el uso de un constructor (__init__).
    """
    def __init__(self, nombre, precio):
        """
        Constructor de la clase Producto.

        Se ejecuta automáticamente cuando se crea una nueva instancia de Producto.
        Inicializa los atributos 'nombre' y 'precio' del objeto.
        """
        self.nombre = nombre
        self.precio = precio
        print(f"--- CONSTRUCTOR: Producto '{self.nombre}' con precio ${self.precio:.2f} creado.")

# --- Demostración del Constructor ---

print("Creando dos objetos de la clase Producto:")

# Se crea el primer producto. El constructor __init__ se invoca aquí.
mi_producto1 = Producto("Laptop", 1200.50)

# Se crea el segundo producto. El constructor __init__ se invoca aquí.
mi_producto2 = Producto("Ratón inalámbrico", 25.99)

print("\nObjetos creados exitosamente.")
# Los objetos 'mi_producto1' y 'mi_producto2' ahora existen con sus atributos inicializados.
print(f"El primer producto es: {mi_producto1.nombre}")
print(f"El segundo producto es: {mi_producto2.nombre}")