"""
Biblioteca de eletronica para robotica.

Contem classes para componentes eletronicos comuns
em robos: resistores, capacitores, LEDs, transistores.
"""
import math


class Componente:
    """
    Classe base para componentes eletronicos.
    """
    
    def __init__(self, nome, pins=None):
        self.nome = nome
        self.pins = pins or []
        self.estado = False
        
    def ligar(self):
        """Liga o componente."""
        self.estado = True
        
    def desligar(self):
        """Desliga o componente."""
        self.estado = False
        
    def toggle(self):
        """Alterna estado."""
        self.estado = not self.estado
        
    def __str__(self):
        estado_str = "LIGADO" if self.estado else "DESLIGADO"
        return f"{self.nome}: {estado_str}"


class Resistor(Componente):
    """
    Resistor com valor e tolerancia.
    """
    
    def __init__(self, nome, ohms, tolerancia=5):
        super().__init__(nome)
        self.ohms = ohms
        self.tolerancia = tolerancia
        
    def tensao(self, corrente):
        """Calcula tensao: V = R * I"""
        return self.ohms * corrente
        
    def corrente(self, tensao):
        """Calcula corrente: I = V / R"""
        return tensao / self.ohms
        
    def potencia(self, tensao=None, corrente=None):
        """Calcula potencia: P = V * I = V^2 / R = I^2 * R"""
        if tensao is not None and corrente is not None:
            return tensao * corrente
        elif tensao is not None:
            return (tensao ** 2) / self.ohms
        elif corrente is not None:
            return (corrente ** 2) * self.ohms
        return 0
        
    def valor_minimo(self):
        """Retorna valor minimo considering tolerancia."""
        return self.ohms * (1 - self.tolerancia / 100)
        
    def valor_maximo(self):
        """Retorna valor maximo considering tolerancia."""
        return self.ohms * (1 + self.tolerancia / 100)
        
    @staticmethod
    def de_faixa(cores):
        """
        Calcula valor a partir das cores da faixa.
        
        Args:
            cores: Lista de cores ["marrom", "preto", "vermelho", ...]
        """
        codigo_cores = {
            "preto": 0, "marrom": 1, "vermelho": 2, "laranja": 3,
            "amarelo": 4, "verde": 5, "azul": 6, "violeta": 7,
            "cinza": 8, "branco": 9
        }
        
        multiplicadores = {
            "preto": 1, "marrom": 10, "vermelho": 100, "laranja": 1000,
            "amarelo": 10000, "verde": 100000, "azul": 1000000,
            "violeta": 10000000, "cinza": 100000000, "branco": 1000000000
        }
        
        tolerancias = {
            "dourado": 5, "prata": 10, "nenhum": 20
        }
        
        if len(cores) < 3:
            raise ValueError("Minimo 3 cores necessarias")
            
        digito1 = codigo_cores.get(cores[0], 0)
        digito2 = codigo_cores.get(cores[1], 0)
        mult = multiplicadores.get(cores[2], 1)
        tol = tolerancias.get(cores[3], 20) if len(cores) > 3 else 20
        
        valor = (digito1 * 10 + digito2) * mult
        return Resistor(f"R_{valor}", valor, tol)


class Capacitor(Componente):
    """
    Capacitor com valor em microfarads.
    """
    
    def __init__(self, nome, uf, tensao_max=25):
        super().__init__(nome)
        self.uf = uf
        self.tensao_max = tensao_max
        self.carga_atual = 0
        
    def carga(self, tensao):
        """Calcula carga: Q = C * V (em microculombs)"""
        return self.uf * tensao
        
    def energia(self, tensao):
        """Calcula energia armazenada: E = 0.5 * C * V^2"""
        return 0.5 * self.uf * (tensao ** 2) / 1000000
        
    def tempo_carga(self, resistencia_ohms):
        """Calcula constante de tempo: tau = R * C"""
        return resistencia_ohms * self.uf / 1000000
        
    def impedancia(self, frequencia_hz):
        """Calcula impedancia: Xc = 1 / (2 * pi * f * C)"""
        c_farads = self.uf / 1000000
        return 1 / (2 * math.pi * frequencia_hz * c_farads)
        
    def carregar(self, percentual=100):
        """Simula carga do capacitor."""
        self.carga_atual = min(self.tensao_max, self.tensao_max * percentual / 100)
        
    def descarregar(self):
        """Simula descarga."""
        self.carga_atual = 0


class LED(Componente):
    """
    LED com cor e corrente nominal.
    """
    
    COR_TENSAO = {
        "vermelho": 1.8,
        "amarelo": 2.0,
        "verde": 2.2,
        "azul": 3.2,
        "branco": 3.4,
        "infravermelho": 1.2,
        "ultravioleta": 3.5
    }
    
    def __init__(self, nome, cor="vermelho", pin=13):
        super().__init__(nome, [pin])
        self.cor = cor
        self.tensao = self.COR_TENSAO.get(cor, 2.0)
        self.corrente_nominal = 0.02  # 20mA
        
    def resistor_serie(self, tensao_fonte):
        """Calcula resistor serie necessario."""
        queda = tensao_fonte - self.tensao
        return int(queda / self.corrente_nominal)
        
    def ligar(self):
        """Liga o LED."""
        super().ligar()
        print(f"[{self.nome}] LED {self.cor} LIGADO")
        
    def desligar(self):
        """Desliga o LED."""
        super().desligar()
        print(f"[{self.nome}] LED {self.cor} DESLIGADO")
        
    def piscar(self, vezes=5, intervalo=0.5):
        """Faz o LED piscar."""
        import time
        for _ in range(vezes):
            self.ligar()
            time.sleep(intervalo)
            self.desligar()
            time.sleep(intervalo)


class TransistorNPN(Componente):
    """
    Transistor NPN (BC547, 2N2222).
    """
    
    def __init__(self, nome, pin_base=7, pin_coleitor=8, pin_emissor=9):
        super().__init__(nome)
        self.pin_base = pin_base
        self.pin_coleitor = pin_coleitor
        self.pin_emissor = pin_emissor
        self.ganho_beta = 200  # hFE tipico
        
    def ligar(self, corrente_base):
        """
        Liga o transistor (regiao de saturacao).
        
        Args:
            corrente_base: Corrente de base em amps
        """
        super().ligar()
        self.corrente_coleitor = corrente_base * self.ganho_beta
        print(f"[{self.nome}] Transistor LIGADO, Ic={self.corrente_coleitor*1000:.1f}mA")
        
    def resistor_base(self, tensao_fonte, tensao_be=0.7):
        """Calcula resistor de base necessario."""
        return int((tensao_fonte - tensao_be) / (self.corrente_coleitor / self.ganho_beta))


class Buzzer(Componente):
    """
    Buzzer piezoeletrico.
    """
    
    def __init__(self, nome="Buzzer", pin=8):
        super().__init__(nome, [pin])
        
    def tone(self, frequencia, duracao=200):
        """Toca uma nota."""
        import time
        print(f"[{self.nome}] Tone: {frequencia}Hz por {duracao}ms")
        time.sleep(duracao / 1000)
        
    def beep(self, duracao=100):
        """Emite beep."""
        self.tone(1000, duracao)
        
    def alarme(self, repeticoes=3):
        """Emite alarme."""
        import time
        for _ in range(repeticoes):
            self.tone(1000, 200)
            time.sleep(0.1)
            self.tone(500, 200)
            time.sleep(0.1)


class Potenciometro(Componente):
    """
    Potenciometro analogico.
    """
    
    def __init__(self, nome="Pot", pin="A0", ohms=10000):
        super().__init__(nome, [pin])
        self.ohms = ohms
        self.posicao = 0.5  # 0.0 a 1.0
        
    def ler(self):
        """Le posicao atual (0.0 - 1.0)."""
        return self.posicao
        
    def tensao(self, tensao_fonte):
        """Calcula tensao de saida."""
        return tensao_fonte * self.posicao
        
    def definir_posicao(self, posicao):
        """Define posicao (0.0 - 1.0)."""
        self.posicao = max(0.0, min(1.0, posicao))


class Display7Segmentos(Componente):
    """
    Display de 7 segmentos.
    """
    
    SEGMENTOS = {
        0: [1, 1, 1, 1, 1, 1, 0],
        1: [0, 1, 1, 0, 0, 0, 0],
        2: [1, 1, 0, 1, 1, 0, 1],
        3: [1, 1, 1, 1, 0, 0, 1],
        4: [0, 1, 1, 0, 0, 1, 1],
        5: [1, 0, 1, 1, 0, 1, 1],
        6: [1, 0, 1, 1, 1, 1, 1],
        7: [1, 1, 1, 0, 0, 0, 0],
        8: [1, 1, 1, 1, 1, 1, 1],
        9: [1, 1, 1, 1, 0, 1, 1]
    }
    
    def __init__(self, nome="Display", pins=None):
        super().__init__(nome, pins or list(range(7)))
        self.valor_atual = 0
        
    def mostrar(self, digito):
        """Mostra digito no display."""
        if 0 <= digito <= 9:
            self.valor_atual = digito
            segmentos = self.SEGMENTOS[digito]
            print(f"[{self.nome}] Display: {digito} -> {segmentos}")
            
    def limpar(self):
        """Limpa display."""
        self.valor_atual = 0
        print(f"[{self.nome}] Display: 0")


class SensorLDR(Componente):
    """
    Sensor de luminosidade LDR.
    """
    
    def __init__(self, nome="LDR", pin="A5"):
        super().__init__(nome, [pin])
        
    def ler(self):
        """Le luminosidade (0-1023)."""
        import random
        return random.randint(0, 1023)
        
    def escuro(self, limiar=200):
        """Verifica se esta escuro."""
        return self.ler() < limiar
        
    def claro(self, limiar=800):
        """Verifica se esta claro."""
        return self.ler() > limiar


class PotenciometroDigital(Componente):
    """
    Potenciometro digital (MCP4131).
    """
    
    def __init__(self, nome="PotDigital", pin_cs=10, ohms=10000):
        super().__init__(nome, [pin_cs])
        self.ohms = ohms
        self.posicao = 0
        
    def definir_posicao(self, posicao):
        """Define posicao (0-127)."""
        self.posicao = max(0, min(127, posicao))
        
    def resistencia(self):
        """Calcula resistencia atual."""
        return (self.posicao / 127) * self.ohms
        
    def attenuacao_db(self):
        """Calcula atenuacao em dB."""
        if self.posicao == 0:
            return float('-inf')
        return -20 * math.log10(127 / self.posicao)


