import socket                 #导入socket通信库
import machine
from machine import Pin
import network
import os
import time


g5 = Pin(5,Pin.OUT)
g5.value(1)


SSID="CMCC-pjrg"                                         #set the wifi ID 
PASSWORD="18375324628"                                 #set the wifi password

wlan=network.WLAN(network.STA_IF)                     #create a wlan object
wlan.active(True)                                     #Activate the network interface
wlan.disconnect()                                     #Disconnect the last connected WiFi
wlan.connect(SSID,PASSWORD)                             #connect wifi
while(wlan.ifconfig()[0]=='0.0.0.0'):
	time.sleep(1)                        #connect wifi


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create stream socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #Set the value of the given socket option
s.bind((wlan.ifconfig()[0], 80))            #绑定地址
s.listen(5)             #设置允许连接的客户端数量
print('listening on:')
print(wlan.ifconfig()[0]+str(80))
while True:
    cl, addr = s.accept()
    print('client connected from:', addr)
    cl_file = cl.makefile('rwb', 0) 
    req = b''
    while True:
        line = cl_file.readline() 
        if not line or line == b'\r\n':
            break
        req += line
    print("Request:")
    req=req.decode('utf-8').split('\r\n')
    req_data=req[0].lstrip().rstrip().replace(' ','').lower()
    print(req_data)
    if req_data.find('favicon.ico')>-1:
        cl.close()
        continue
    else:
        req_data=req_data.replace('get/?','').replace('http/1.1','')
        index = req_data.find('key=')
        value = req_data[index+4:index+6].lstrip().rstrip()
        print('key:',value)
        if value == 'on':
            g4 = Pin(13,Pin.OUT)
            g4.value(1)
            print('have on')
        
        if value == 'of':
            g4 = Pin(13,Pin.OUT)
            g4.value(0)
            print('have off')
    with open("control_light.html", 'r') as f:
        for line in f:
            cl.send(line)
    cl.close()
