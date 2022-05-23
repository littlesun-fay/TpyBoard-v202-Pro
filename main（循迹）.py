from machine import Pin
import time
import machine
from machine import Timer



p4 = Pin(4, Pin.OUT)
p5 = Pin(5, Pin.OUT)
p13 = Pin(13, Pin.OUT)
p12 = Pin(12, Pin.OUT)

def left():
    p4.value(0)
    p5.value(1)
    p13.value(1)
    p12.value(0)

def back():
    p4.value(1)
    p5.value(0)
    p13.value(1)
    p12.value(0)

def right():
    p4.value(1)
    p5.value(0)
    p13.value(0)
    p12.value(1)

def forword():
    p4.value(0)
    p5.value(1)
    p13.value(0)
    p12.value(1)
	
def s():
    p4.value(0)
    p5.value(0)
    p13.value(0)
    p12.value(0)
	
print('3')
Trig = Pin(10,Pin.OUT)
Echo = Pin(15,Pin.IN)
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
while True:
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
                        if distance >=30:
                            forword()
                            
                        if distance < 30:
                            s()
                            time.sleep_ms(500)
                            back()
                            time.sleep_ms(500)
                            left()
                            time.sleep_ms(50)
                            

                flag=0
                run=0
