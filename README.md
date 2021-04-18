# Projetos com Python e Arduino

## Integração entre o Python e Arduino
> Para que seja possível que os programas em Python se comuniquem com o Arduino é necessário a utilização do protocolo Firmata, que é carregado no Arduino e instalação da biblioteca [pyFirmata](https://pypi.org/project/pyFirmata/) no programa Python.

<img src=images/firmata.png width=50%>

O primeiro passo é **carregar** o protocolo Firmata no Arduino.

É preciso instalar a biblioteca Python pyFirmata: ```pip install pyFirmata```

## Entradas e Saídas Digitais

### Pisca-Pisca - Primeiro exemplo

#### Material necessário:
* 1 Arduino
* 1 resistor de 220 ohms ou de 330 ohms
* 1 LED
* 1 protoboard
* Cabos de ligação

#### Montagem
<img src=images/arduino_01.png width=50%>

O código python está no arquivo [pisca.py](01_pisca-pisca/pisca.py).

Com o código pronto basta executar: ```python pisca.py```

Somente como exemplo, o arquivo de como ficaria um programa similar para rodar no Arduino: [programa.ino](01_pisca-pisca/programa.ino).

