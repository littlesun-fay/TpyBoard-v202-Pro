import machine
from machine import Pin
import time

p4 = Pin(4,Pin.OUT)

while True:
    adc = machine.ADC(0)
    V = adc.read()
    print(V)
    if V <250:
        p4.value(1)
    if V > 250:
        p4.value(0)
    time.sleep(0.5) 
