class Asiento:
    coloresPosibles = ["rojo", "verde", "amarillo", "blanco", "negro"]
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro        
    
    def cambiarColor(self, nuevoColor, coloresPosibles):
        for i in coloresPosibles:
            if nuevoColor.lower() == i:
                self.color = nuevoColor

class Auto:
    cantidadCreados = 0
    
    def __init__(self, modelo, precio, Asientos, marca, Motor, registro):
         self.modelo = modelo
         self.precio = precio
         self.asientos = Asientos
         self.marca = marca
         self.motor = Motor
         self.registro = registro
        
    def cantidadAsientos(self, asientos):
        cantidad = 0
        for a in asientos:
             if isinstance(a, Asiento):
                  cantidad = cantidad + 1
        return cantidad

    def verificarIntegridad(self):
        for a in self.asientos:
            if isinstance(a, Asiento):
                if a.registro != self.motor.registro or a.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto original"
    
class Motor:
    def __init__ (self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro

    def asignarTipo(self, tipoMotor):
        if tipoMotor == "electrico" or tipoMotor == "gasolina":
            self.tipo = tipoMotor


