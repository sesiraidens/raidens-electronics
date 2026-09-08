<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" width="80">

# raidens-electronics

Biblioteca de eletronica: resistores, capacitores, LEDs, transistores e displays.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-d9333b?style=flat)
![Status](https://img.shields.io/badge/Status-Active-2ea043?style=flat)

</div>

---

## Sobre

O **raidens-electronics** fornece classes para simulacao e calculo de componentes eletronicos comuns em robotica.

---

## Componentes

### Passivos

| Classe | Descricao |
|---|---|
| Resistor | Resistencia com calculos |
| Capacitor | Capacitor com carga/descarga |

### Ativos

| Classe | Descricao |
|---|---|
| LED | LED com cor e resistor serie |
| TransistorNPN | Transistor NPN (BC547, 2N2222) |

### Entrada

| Classe | Descricao |
|---|---|
| Potenciometro | Potenciometro analogico |
| SensorLDR | Sensor de luminosidade |

### Saida

| Classe | Descricao |
|---|---|
| Buzzer | Buzzer piezoeletrico |
| Display7Segmentos | Display de 7 segmentos |

---

## Uso

### Resistor

`python
from src.componentes import Resistor

r1 = Resistor("R1", 1000, tolerancia=5)
print(f"Valor: {r1.ohms} ohms")
print(f"Minimo: {r1.valor_minimo()}")
print(f"Maximo: {r1.valor_maximo()}")

# Calculos
v = r1.tensao(0.01)  # 10V com 10mA
i = r1.corrente(5)   # 5mA com 5V
p = r1.potencia(5)   # 25mW com 5V

# De faixa de cores
r2 = Resistor.de_faixa(["marrom", "preto", "vermelho", "dourado"])
`

### Capacitor

`python
from src.componentes import Capacitor

c1 = Capacitor("C1", 100, tensao_max=25)  # 100uF
print(f"Carga: {c1.carga(12)} uC")
print(f"Energia: {c1.energia(12)} mJ")
print(f"Tau: {c1.tempo_carga(1000)}s")
print(f"Impedancia: {c1.impedancia(1000)} ohms @ 1kHz")
`

### LED

`python
from src.componentes import LED

led = LED("LED1", cor="vermelho", pin=13)
resistor = led.resistor_serie(5)  # Calcula resistor para 5V
print(f"Resistor serie: {resistor} ohms")

led.ligar()
led.piscar(vezes=5, intervalo=0.5)
`

### Transistor

`python
from src.componentes import TransistorNPN

t1 = TransistorNPN("Q1")
t1.ligar(corrente_base=0.0001)  # 100uA
print(f"Corrente coleitor: {t1.corrente_coleitor*1000:.1f}mA")
`

### Potenciometro

`python
from src.componentes import Potenciometro

pot = Potenciometro("P1", pin="A0", ohms=10000)
pot.definir_posicao(0.7)  # 70%
print(f"Tensao: {pot.tensao(5):.2f}V")
`

### Display

`python
from src.componentes import Display7Segmentos

display = Display7Segmentos()
for i in range(10):
    display.mostrar(i)
`

---

## Calculos Eletronicos

### Lei de Ohm

`python
V = I * R  # Tensao
I = V / R  # Corrente
R = V / I  # Resistencia
`

### Potencia

`python
P = V * I
P = V^2 / R
P = I^2 * R
`

### RC (Resistor-Capacitor)

`python
tau = R * C           # Constante de tempo
Vc = V * (1 - e^-t/tau)  # Carga
Vc = V * e^-t/tau         # Descarga
`

---

## Equipe

**RAIDENS - SESI Aluminio 192**

Desenvolvido para uso interno da equipe. Licenciado sob MIT.