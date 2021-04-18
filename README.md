# Projetos com Python e Arduino

## Integração entre o Python e Arduino
> Para que seja possível que os programas em Python se comuniquem com o Arduino é necessário a utilização do protocolo Firmata, que é carregado no Arduino e instalação da biblioteca [pyFirmata](https://pypi.org/project/pyFirmata/) no programa Python.

<img src=images/firmata.png width=50%>

O primeiro passo é **carregar** o protocolo Firmata no Arduino.

É preciso instalar a biblioteca Python pyFirmata: ```pip install pyFirmata```

## Entradas e Saídas Digitais

### Pisca-Pisca - Primeiro exemplo
