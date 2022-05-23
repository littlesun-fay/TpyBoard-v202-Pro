import network
import utime

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
