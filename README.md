<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="140">

# raidens-electronics

**Modelos e cálculos de componentes eletrônicos para projetos de robótica**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Sem dependências](https://img.shields.io/badge/depend%C3%AAncias-nenhuma-2EA043?style=flat-square)
![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-D9333B?style=flat-square)

[Sobre](#sobre) · [Instalação](#instalação) · [Componentes](#componentes) · [Uso](#uso) · [Fórmulas](#fórmulas-de-referência)

</div>

---

## Sobre

O **raidens-electronics** responde às perguntas que aparecem toda vez que alguém monta um circuito: *qual resistor vai com este LED?*, *quanto tempo o capacitor leva para carregar?*, *que valor é este resistor de faixas marrom, preto e vermelho?*

Cada componente é uma classe com os cálculos que importam para ele. Isso serve tanto para dimensionar o circuito do robô quanto como material de estudo para quem está começando em eletrônica.

## Instalação

```bash
git clone https://github.com/sesiraidens/raidens-electronics.git
cd raidens-electronics
```

Requer apenas Python 3.8 ou superior. Rode os scripts a partir da raiz do repositório.

## Componentes

| Tipo | Classe | O que calcula ou simula |
|---|---|---|
| Passivo | `Resistor` | Tensão, corrente, potência, tolerância e leitura pelas faixas de cor |
| Passivo | `Capacitor` | Carga, energia, constante de tempo RC e impedância |
| Ativo | `LED` | Resistor em série ideal para cada cor |
| Ativo | `TransistorNPN` | Corrente de coletor e resistor de base (BC547, 2N2222) |
| Entrada | `Potenciometro` | Tensão de saída conforme a posição |
| Entrada | `PotenciometroDigital` | Resistência e atenuação em dB |
| Entrada | `SensorLDR` | Claro ou escuro por limiar |
| Saída | `Buzzer` | Tons, bipes e alarmes |
| Saída | `Display7Segmentos` | Segmentos acesos para cada dígito |

## Uso

### Resistor

```python
from src.componentes import Resistor

r1 = Resistor("R1", 1000, tolerancia=5)
r1.valor_minimo(), r1.valor_maximo()   # faixa real pela tolerância
r1.corrente(5)                         # corrente com 5 V
r1.potencia(tensao=5)                  # potência dissipada

r2 = Resistor.de_faixa(["marrom", "preto", "vermelho", "dourado"])   # 1 kΩ ±5%
```

### Capacitor

```python
from src.componentes import Capacitor

c1 = Capacitor("C1", 100, tensao_max=25)   # 100 µF
c1.carga(12)              # µC
c1.energia(12)            # mJ
c1.tempo_carga(1000)      # τ com resistor de 1 kΩ
c1.impedancia(1000)       # Ω a 1 kHz
```

### LED e transistor

```python
from src.componentes import LED, TransistorNPN

led = LED("LED1", cor="vermelho", pin=13)
led.resistor_serie(5)                 # resistor para alimentar com 5 V

q1 = TransistorNPN("Q1")
q1.ligar(corrente_base=0.0001)        # 100 µA na base
q1.resistor_base(tensao_fonte=5)
```

## Fórmulas de referência

| Grandeza | Fórmula |
|---|---|
| Lei de Ohm | V = I · R |
| Potência | P = V · I = V² / R = I² · R |
| Constante de tempo RC | τ = R · C |
| Carga do capacitor | Vc = V · (1 − e^(−t/τ)) |
| Descarga do capacitor | Vc = V · e^(−t/τ) |

## Estrutura

```text
raidens-electronics/
└── src/
    └── componentes.py   # Componente base e todas as classes
```

## Ecossistema RAIDENS

Este repositório faz parte de um conjunto de bibliotecas da equipe. Elas usam os mesmos nomes de classes e convenções, então o que você aprende em uma serve nas outras.

| Repositório | Para quê |
|---|---|
| [`raidens-python`](https://github.com/sesiraidens/raidens-python) | Biblioteca principal em Python: sensores, motores e robôs prontos (seguidor, parede, resgate) |
| [`raidens-arduino`](https://github.com/sesiraidens/raidens-arduino) | As mesmas abstrações em C++ para rodar direto no Arduino |
| [`raidens-sensores`](https://github.com/sesiraidens/raidens-sensores) | Catálogo completo de sensores com calibração e filtragem |
| [`raidens-motores`](https://github.com/sesiraidens/raidens-motores) | Motores DC, servo, passo, driver L298N e rodas mecanum |
| [`raidens-pid`](https://github.com/sesiraidens/raidens-pid) | Controladores PID, PID avançado, cascata e sintonia Ziegler-Nichols |
| [`raidens-opencv`](https://github.com/sesiraidens/raidens-opencv) | Visão computacional: cores, linhas e navegação por câmera |
| [`raidens-lab`](https://github.com/sesiraidens/raidens-lab) | Calibração interativa de cores em HSV e LAB |
| [`raidens-obr`](https://github.com/sesiraidens/raidens-obr) | Robô completo para a OBR, integrando sensores, motores e missões |
| [`raidens-3d`](https://github.com/sesiraidens/raidens-3d) | Peças 3D paramétricas geradas em OpenSCAD |
| [`raidens-ros`](https://github.com/sesiraidens/raidens-ros) | Estrutura de nodes e tópicos ROS 2 |
| [`raidens-snippets`](https://github.com/sesiraidens/raidens-snippets) | Trechos de código prontos para copiar e colar |

---

<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="56">

**Equipe RAIDENS** · SESI 192 Alumínio/SP

[![Email](https://img.shields.io/badge/Email-sesiraidens%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:sesiraidens@gmail.com)
[![Linktree](https://img.shields.io/badge/Linktree-sesiraidens-39E06B?style=flat-square&logo=linktree&logoColor=white)](https://linktr.ee/sesiraidens)
[![GitHub](https://img.shields.io/badge/GitHub-sesiraidens-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sesiraidens)

<sub>Desenvolvido pela equipe RAIDENS para fins educacionais. Licenciado sob MIT.</sub>

</div>


