"""
Programa pisca.py.

Exemplo executado num ambiente Linux
"""
from pyfirmata import Arduino

PORTA = "/dev/ttyACM0"

uno = Arduino(PORTA)
led = uno.get_pin('d:13:o')


while True:
    led.write(1)
    uno.pass_time(0.5)
    led.write(0)
    uno.pass_time(0.5)
