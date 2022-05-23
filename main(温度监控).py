import network
import utime
import urequests
import dht
import machine
from machine import Pin
import time
import os


pdcn = network.WLAN(network.STA_IF)
pdcn.active(True)
pdcn.connect('CMCC-pjrg', '18375324628')
utime.sleep(5)
if pdcn.isconnected():
    print("WiFi is connected %s."%pdcn.ifconfig()[0])
else:
    pdcn.active(False)
    utime.sleep(5)
    print("WiFi cannot connect.")

class AlarmSystem:
    def __init__(self):
        self.d = dht.DHT11(machine.Pin(5))

    def dht11(self):
        try:
            self.d.measure()
            return '温度:'+str(self.d.temperature())+'°C---湿度:'+str(self.d.humidity())+'%'

        except:
            return '0'

    def push(self, result):
        title = "小太阳提示您:注意天气变化保持健康心情"
        content = 'text='+title+'&'+'desp='+result
        url="https://sc.ftqq.com/SCU102184T62a17441b05f23c05e520523105c0f1b5eecbde27e488.send?%s" % content
        r = urequests.get(url)
        r.close()

p2=Pin(2,Pin.OUT)
a = AlarmSystem()

def SendData():
    p2.value(not p2.value())
    data_= a.dht11()
    if(data_!='0'):
        print(data_)
        a.push(data_)
    else:
        print('GET Data Fail')

if __name__ == '__main__':

    while True:
        SendData()
        time.sleep(300)
