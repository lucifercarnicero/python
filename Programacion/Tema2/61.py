#61. Diseñar la clase Hora que representa un instante de tiempo compuesto por una hora y los minutos. Dispone de los métodos:
#a. Constructor con parámetros hora y minuto
#b. Método que incrementa la hora en un minuto
#c. Setters y getters de los atributos hora y minuto.
#d. toString, que devuelve un string con la representación del reloj e implica la redefinición de este método de Object en la clase Hora

class Hora:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def incrementar_minuto(self):
        if self.minuto == 59:  # Si los minutos son 59, resetear a 0 y aumentar la hora
            self.minuto = 0
            self.hora = (self.hora + 1) % 24  # Asegura que la hora se resetee a 0 después de 23
        else:
            self.minuto += 1  # Incrementa los minutos normalmente

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, valor):
        if 0 <= valor < 24:
            self._hora = valor
        else:
            raise ValueError("Hora debe estar entre 0 y 23")

    @property
    def minuto(self):
        return self._minuto

    @minuto.setter
    def minuto(self, valor):
        if 0 <= valor < 60:
            self._minuto = valor
        else:
            raise ValueError("Minuto debe estar entre 0 y 59")

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"

# Ejemplo de uso
if __name__ == "__main__":
    hora_actual = Hora(14, 59)
    print(hora_actual)  # Muestra 14:59

    hora_actual.incrementar_minuto()
    print(hora_actual)  # Muestra 15:00
