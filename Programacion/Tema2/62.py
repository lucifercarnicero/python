#62. Implementar la clase HoraExacta que hereda de Hora y que añade los segundos. Incluir los getters y setters necesarios, modificar inc() para que añada un segundo y modificar el constructor como corresponda.

class Hora:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def incrementar_minuto(self):
        if self.minuto == 59:
            self.minuto = 0
            self.hora = (self.hora + 1) % 24
        else:
            self.minuto += 1

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

class HoraExacta(Hora):
    def __init__(self, hora, minuto, segundo):
        super().__init__(hora, minuto)
        self.segundo = segundo

    @property
    def segundo(self):
        return self._segundo

    @segundo.setter
    def segundo(self, valor):
        if 0 <= valor < 60:
            self._segundo = valor
        else:
            raise ValueError("Segundo debe estar entre 0 y 59")

    def incrementar_segundo(self):
        self.segundo += 1
        if self.segundo >= 60:
            self.segundo = 0
            super().incrementar_minuto()

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

# Ejemplo de uso
if __name__ == "__main__":
    hora_exacta = HoraExacta(23, 59, 59)
   
print(hora_exacta) # Muestra 23:59:59