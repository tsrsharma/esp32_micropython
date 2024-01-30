#controlling the neopixel led

import machine
import time
import neopixel

#object for neopixel LED
np = neopixel.NeoPixel(machine.Pin(48),1)

while True:
    try:
        np[0] = [255,0,0]
        np.write()
        time.sleep(0)
        np[0] = [0,255,0]
        np.write()
        time.sleep(0)
        np[0] = [0,0,255]
        np.write()
        time.sleep(0)
        np[0] = [200,100,0]
        np.write()
        time.sleep(2)
    except  KeyboardInterrupt:
        print("Exit")
        break