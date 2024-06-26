class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


uno = Carro('Uno')
fiat = Fabricante('Fiat')
motor1 = Motor('1.0')
uno.fabricante = fiat
uno.motor = motor1
print(uno.nome, uno.fabricante.nome, uno.motor.nome)

gol = Carro('Gol')
volkswagen = Fabricante('Volkswagen')
motor2 = Motor('2.0')
gol.fabricante = volkswagen
gol.motor = motor2
print(gol.nome, gol.fabricante.nome, gol.motor.nome)
# motor1.inserir_carros_motor('Polo', 'Up')
# motor1.listar_carros_motor()

# uno.motor = motor1

# fabricante1 = Fabricante('Fiat')
# fabricante1.inserir_carros_fabri('Uno', 'Mobi')
# fabricante1.listar_carros_fabri()
