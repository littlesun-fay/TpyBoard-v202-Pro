import dht
import machine
from machine import Pin
import time#声明用到的类库，尤其是dht的类库

d = dht.DHT11(machine.Pin(5))#声明用到类库中的函数，并设置参数
count=0
while True:#开始整个代码的大循环
    d.measure()#调用DHT类库中测量数据的函数
    temp_=str(d.temperature())#读取measure()函数中的温度数据
    hum_=str(d.humidity())#读取measure()函数中的湿度数据
    count+=1#计数变量+1
    print('eg:',temp_,'-',hum_)
    print('Count:',count)
    time.sleep(5)

