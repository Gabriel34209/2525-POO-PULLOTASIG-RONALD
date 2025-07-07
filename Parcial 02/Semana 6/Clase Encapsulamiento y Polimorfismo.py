# employee_manager.py

class Persona:
    """
    Clase base para representar a una persona.
    Demuestra encapsulación con el atributo 'nombre'.
    """
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido para encapsulación
        self.edad = edad

    def get_nombre(self):
        """Método getter para acceder al nombre."""
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        """Método setter para modificar el nombre."""
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            print("El nombre debe ser una cadena no vacía.")

    def presentarse(self):
        """Método para que la persona se presente."""
        return f"Hola, soy {self._nombre} y tengo {self.edad} años."

class Empleado(Persona):
    """
    Clase derivada de Persona, representa a un empleado.
    Demuestra herencia.
    """
    def __init__(self, nombre, edad, id_empleado, cargo):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.id_empleado = id_empleado
        self.cargo = cargo

    def trabajar(self):
        """Método específico de Empleado."""
        return f"{self._nombre} (ID: {self.id_empleado}) está trabajando en su rol de {self.cargo}."

    def presentarse(self):
        """
        Método sobrescrito para demostrar polimorfismo.
        Añade información de empleado a la presentación.
        """
        return f"Hola, soy {self.get_nombre()}, tengo {self.edad} años y soy un empleado con ID {self.id_empleado} y cargo de {self.cargo}."

class Proyecto:
    """
    Clase para representar un proyecto.
    """
    def __init__(self, nombre_proyecto, descripcion):
        self.nombre_proyecto = nombre_proyecto
        self.descripcion = descripcion
        self.empleados_asignados = []

    def asignar_empleado(self, empleado):
        """Asigna un empleado al proyecto."""
        if isinstance(empleado, Empleado):
            self.empleados_asignados.append(empleado)
            print(f"{empleado.get_nombre()} ha sido asignado al proyecto '{self.nombre_proyecto}'.")
        else:
            print("Solo se pueden asignar instancias de la clase Empleado a un proyecto.")

    def mostrar_info_proyecto(self):
        """Muestra la información del proyecto y los empleados asignados."""
        info = f"--- Proyecto: {self.nombre_proyecto} ---\n"
        info += f"Descripción: {self.descripcion}\n"
        info += "Empleados asignados:\n"
        if not self.empleados_asignados:
            info += "  Ningún empleado asignado aún.\n"
        else:
            for emp in self.empleados_asignados:
                info += f"  - {emp.get_nombre()} (ID: {emp.id_empleado}, Cargo: {emp.cargo})\n"
        return info

def presentar_entidad(entidad):
    """
    Función que demuestra polimorfismo utilizando argumentos múltiples/variables.
    Puede recibir cualquier objeto que tenga un método 'presentarse()'.
    """
    print(entidad.presentarse())

# --- Demostración del programa ---
if __name__ == "__main__":
    print("--- Creando instancias y demostrando funcionalidad ---")

    # Demostración de Herencia y Encapsulación
    print("\n## Demostración de Herencia y Encapsulación ##")
    persona1 = Persona("Ana López", 30)
    print(f"Nombre inicial de persona1 (getter): {persona1.get_nombre()}")
    persona1.set_nombre("Ana María López")
    print(f"Nombre modificado de persona1: {persona1.get_nombre()}")
    persona1.set_nombre("") # Intento de establecer un nombre inválido
    print(f"Nombre después de intento inválido: {persona1.get_nombre()}")

    empleado1 = Empleado("Juan Pérez", 25, "EMP001", "Desarrollador Senior")
    empleado2 = Empleado("María García", 35, "EMP002", "Gerente de Proyectos")

    print(f"\nEmpleado 1: {empleado1.get_nombre()}, Cargo: {empleado1.cargo}")
    print(empleado1.trabajar())

    # Demostración de Polimorfismo (método sobrescrito y función polimórfica)
    print("\n## Demostración de Polimorfismo ##")
    print("Presentación de Persona:")
    presentar_entidad(persona1) # Llama al presentarse() de Persona

    print("\nPresentación de Empleado (método sobrescrito):")
    presentar_entidad(empleado1) # Llama al presentarse() de Empleado
    presentar_entidad(empleado2)

    # Demostración de uso de clases
    print("\n## Demostración de Gestión de Proyectos ##")
    proyecto_web = Proyecto("Sitio Web Corporativo", "Desarrollo de un nuevo sitio web interactivo.")
    proyecto_app = Proyecto("Aplicación Móvil", "Creación de una aplicación para iOS y Android.")

    proyecto_web.asignar_empleado(empleado1)
    proyecto_web.asignar_empleado(empleado2)
    proyecto_web.asignar_empleado("Esto no es un empleado") # Demuestra validación

    print("\n" + proyecto_web.mostrar_info_proyecto())

    proyecto_app.asignar_empleado(empleado1)
    print("\n" + proyecto_app.mostrar_info_proyecto())