# Definimos la clase Persona
class Persona:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def get_nombre(self):
    return self.nombre

  def get_apellido(self):
    return self.apellido

# Definimos la clase Cuenta
class Cuenta:

    def __init__(self, titular, cantidad=0.0):
        
        if not isinstance(titular, Persona):
            raise TypeError("El titular debe ser una instancia de Persona")
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular):
        
        if not isinstance(titular, Persona):
            raise TypeError("El titular debe ser una instancia de Persona")
        self.titular = titular

    def set_cantidad(self, cantidad):
        
        self.cantidad = cantidad

    def get_titular(self):
        
        return self.titular

    def get_cantidad(self):
        
        return self.cantidad

    def mostrar(self):
        
        print(f"Titular: {self.titular.get_nombre()} {self.titular.get_apellido()}")
        print(f"Cantidad: {self.cantidad:.2f}")

    def ingresar(self, cantidad):
       
        if cantidad <= 0:
            print("No se puede ingresar una cantidad negativa.")
        else:
            self.cantidad += cantidad
            print(f"Se han ingresado {cantidad:.2f}$ a la cuenta.")

    def retirar(self, cantidad):
       
        if cantidad <= 0:
            print("No se puede retirar una cantidad negativa.")
        elif cantidad > self.cantidad:
            print(f"No hay suficiente saldo para retirar {cantidad:.2f}$.")
        else:
            self.cantidad -= cantidad
            print(f"Se han retirado {cantidad:.2f}$ de la cuenta.")

# Creamos una instancia de Persona y una instancia de Cuenta
persona_ejemplo = Persona("Juan", "Perez")
cuenta_ejemplo = Cuenta(persona_ejemplo, 1000)

# Ejemplo de uso de los métodos
cuenta_ejemplo.mostrar()
cuenta_ejemplo.ingresar(500)
cuenta_ejemplo.retirar(200)

