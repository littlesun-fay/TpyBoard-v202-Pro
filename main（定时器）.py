import machine
from machine import Timer
from machine import Pin

"""p12 = Pin(12,Pin.IN)
while True:
    if p12.value() == 0:
        print('NO')
        time.sleep(5)
    if p12.value() == 1:
        print('yes')
        time.sleep(5)"""
start1 = Timer(-1)
start1.init(freq=0.2,mode=Timer.PERIODIC,callback=lambda t:print('yes'))
stop1 = Timer(0)
stop1.init(freq=0.1,mode=Timer.PERIODIC,callback=lambda t:print('no'))
