"""
Programa controle_de_um_led.py.

Exemplo executado num ambiente Linux
"""
from pyfirmata import Arduino

PORTA = "/dev/ttyACM0"

uno = Arduino(PORTA)
led = uno.get_pin('d:13:o')

while True:
    estado = int(input('Digite 1 para ligar o LED e 0 para desligar: '))
    if estado == 0 or estado == 1:
        led.write(estado)
    else:
        print('ERRO: Digite apenas 0 ou 1!')
