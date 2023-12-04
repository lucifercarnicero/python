
class Empleado:

    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

class Maquinista(Empleado):
    
        def __init__(self, nombre, dni, salario, rango):
            super().__init__(nombre, dni)
            self.salario = salario
            self.rango = rango

class Mecanico(Empleado):

    def __init__(self, nombre, dni, telefono, especialidad):
        super().__init__(nombre, dni)
        self.telefono = telefono
        self.especialidad = especialidad

class JefeEstacion(Empleado):

    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)

class Maquina:
    
        def __init__(self, matricula):
            self.matricula = matricula

class Vagon(Maquina):

    def __init__(self, matricula, capacidad_maxima, capacidad_actual, tipo_mercancia):
        super().__init__(matricula)
        self.capacidad_maxima = capacidad_maxima
        self.capacidad_actual = capacidad_actual
        self.tipo_mercancia = tipo_mercancia

class Locomotora(Maquina):

    def __init__(self, matricula, potencia_motor, antiguedad, mecanico_asignado):
        super().__init__(matricula)
        self.potencia_motor = potencia_motor
        self.antiguedad = antiguedad
        self.mecanico_asignado = mecanico_asignado

class Tren:

    def __init__(self, locomotora, vagones, maquinista_asignado):
        self.locomotora = locomotora
        self.vagones = vagones
        self.maquinista_asignado = maquinista_asignado

if __name__ == "__main__":
    # Crear algunos maquinistas
    maquinista1 = Maquinista("Carlos", "12345678A", 3000, "Principiante")
    maquinista2 = Maquinista("Laura", "98765432B", 3500, "Experto")

    # Crear algunos mecánicos
    mecanico1 = Mecanico("Pedro", "23456789C", "123456789", "Motores")
    mecanico2 = Mecanico("Ana", "87654321D", "987654321", "Frenos")

    # Crear algunos jefes de estación
    jefe1 = JefeEstacion("Juan", "34567890E")
    jefe2 = JefeEstacion("María", "56789012F")

    # Crear algunas máquinas
    locomotora1 = Locomotora("L123", 5000, 5, mecanico1)
    locomotora2 = Locomotora("L456", 6000, 3, mecanico2)

    vagon1 = Vagon("V001", 8000, 2000, "Carga general")
    vagon2 = Vagon("V002", 10000, 5000, "Líquidos")

    # Crear algunos trenes
    tren1 = Tren(locomotora1, [vagon1], maquinista1)
    tren2 = Tren(locomotora2, [vagon2], maquinista2)

    # Imprimir información de los maquinistas
    print("Información de Maquinistas:")
    print(f"Maquinista 1: {maquinista1.nombre}, DNI: {maquinista1.dni}, Salario: {maquinista1.salario}, Rango: {maquinista1.rango}")
    print(f"Maquinista 2: {maquinista2.nombre}, DNI: {maquinista2.dni}, Salario: {maquinista2.salario}, Rango: {maquinista2.rango}")

    # Imprimir información de las máquinas
    print("\nInformación de Máquinas:")
    print(f"Locomotora 1: Matrícula: {locomotora1.matricula}, Potencia Motor: {locomotora1.potencia_motor}, Antigüedad: {locomotora1.antiguedad}")
    print(f"Locomotora 2: Matrícula: {locomotora2.matricula}, Potencia Motor: {locomotora2.potencia_motor}, Antigüedad: {locomotora2.antiguedad}")
    print(f"Vagón 1: Matrícula: {vagon1.matricula}, Capacidad Máxima: {vagon1.capacidad_maxima}, Capacidad Actual: {vagon1.capacidad_actual}, Tipo Mercancía: {vagon1.tipo_mercancia}")
    print(f"Vagón 2: Matrícula: {vagon2.matricula}, Capacidad Máxima: {vagon2.capacidad_maxima}, Capacidad Actual: {vagon2.capacidad_actual}, Tipo Mercancía: {vagon2.tipo_mercancia}")

    # Imprimir información de los trenes
    print("\nInformación de Trenes:")
    print(f"Tren 1: Maquinista: {tren1.maquinista_asignado.nombre}, Locomotora: {tren1.locomotora.matricula}, Vagones: {[vagon.matricula for vagon in tren1.vagones]}")
    print(f"Tren 2: Maquinista: {tren2.maquinista_asignado.nombre}, Locomotora: {tren2.locomotora.matricula}, Vagones: {[vagon.matricula for vagon in tren2.vagones]}")
