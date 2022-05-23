from machine import UART


u2=UART(0,9600)#串口初始化
u2.readall()#读取串口全部数据
u2.write('hello')#写入串口数据
