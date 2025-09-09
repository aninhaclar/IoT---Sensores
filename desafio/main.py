from machine import Pin, time_pulse_us
import time

print("Sistema de contagem de caixas iniciado!")

PINO_TRIG = 25
PINO_ECHO = 27
PINO_LED = 26


trig = Pin(PINO_TRIG, Pin.OUT)
echo = Pin(PINO_ECHO, Pin.IN)
led = Pin(PINO_LED, Pin.OUT)


contador = 0
caixas = 0
dist_limite = 10 
objeto_presente = False 

def obter_distancia():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000) 
    if duracao < 0: 
        return None

    distancia = (duracao / 2) * 0.0343
    return distancia

while True:
    dist = obter_distancia()

    if dist is not None and dist < dist_limite:
        print("Distância:", dist, "cm")

        if not objeto_presente:
            contador += 1
            objeto_presente = True
            print("Objeto detectado! Total objetos:", contador)

            if contador >= 10:
                caixas += 1
                contador = 0
                print("Caixa completa! Total de caixas:", caixas)
                led.value(1)  
                time.sleep(2)
                led.value(0)  
    else:
        if objeto_presente:
            print("Objeto saiu do sensor")
        objeto_presente = False

    time.sleep(0.5)

