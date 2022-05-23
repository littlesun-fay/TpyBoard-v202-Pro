from necir import NecIr
from bm import necbm
from bm import nec_cb
from machine import Pin

def main():
      nec = NecIr(pin=Pin(4))
      while True:
              nec.callback(nec_cb)
              if necbm():
                      print("bm=",necbm())

main()
