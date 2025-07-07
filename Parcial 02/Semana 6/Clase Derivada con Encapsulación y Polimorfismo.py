# src/vehiculo.py

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        """
        Constructor de la clase Vehiculo.

        Args:
            marca (str): La marca del vehículo.
            modelo (str): El modelo del vehículo.
            anio (int): El año de fabricación del vehículo.
        """
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        """
        Método para mostrar información general del vehículo.
        """
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"

    def arrancar(self):
        """
        Método para simular el arranque del vehículo.
        """
        return f"El {self.marca} {self.modelo} está arrancando."