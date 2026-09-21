import machine
import time

led_verde = machine.Pin(15, machine.Pin.OUT)
led_amarelo = machine.Pin(14, machine.Pin.OUT)
led_vermelho = machine.Pin(13, machine.Pin.OUT)

def simular_recarga(geracao, consumo):
    energia_disponivel = geracao - consumo
    
    print("-" * 20)
    print(f"GERACAO: {geracao} W")
    print(f"CONSUMO: {consumo} W")
    print(f"DISPONIVEL: {energia_disponivel} W\n")
    
    print("STATUS:")
    if energia_disponivel >= 2500:
        print("RECARGA AUTORIZADA\n")
        led_verde.value(1); led_amarelo.value(0); led_vermelho.value(0)
    elif energia_disponivel > 0:
        print("RECARGA REDUZIDA\n")
        led_verde.value(0); led_amarelo.value(1); led_vermelho.value(0)
    else:
        print("RECARGA BLOQUEADA\n")
        led_verde.value(0); led_amarelo.value(0); led_vermelho.value(1)
        
    val_abs = abs(energia_disponivel)
    print("Representação da Potência Disponível (Valor Absoluto):")
    print(f"Decimal: {val_abs}")
    print(f"Binário: {bin(val_abs)}")
    print(f"Hexadecimal: {hex(val_abs)}")
    print("-" * 20)

simular_recarga(4000, 1500)
time.sleep(4)
simular_recarga(1800, 1500)
time.sleep(4)
simular_recarga(1000, 1800)