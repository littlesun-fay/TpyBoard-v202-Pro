import utime
import machine
from machine import Pin
import time
from machine import Timer



Trig = Pin(5,Pin.OUT)
Echo = Pin(4,Pin.IN)
num=0
flag=0
run=1
def start(t):
    global flag
    global num
    if(flag==0):
            num=0
    else:
            num=num+1
            
def stop(t):
    global run
    if(run==0):
            run=1
start1 = Timer(-1)
start1.init(freq=10000,mode=Timer.PERIODIC,callback=start)
stop1 = Timer(0)
stop1.init(freq=2,mode=Timer.PERIODIC,callback=stop)
if(run==1):
        Trig.value(1)
        time.sleep_us(100)
        Trig.value(0)
        while(Echo.value()==0):
                Trig.value(1)
                time.sleep_us(100)
                Trig.value(0)
                flag=0
        if(Echo.value()==1):
                flag=1
                while(Echo.value()==1):
                        flag=1
        if(num!=0):
                distance=num/10000*34000/2
        flag=0
        run=0
























