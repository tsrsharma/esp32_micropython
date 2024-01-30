#controlling the neopixel led

import machine
import time
import neopixel

#object for neopixel LED
np = neopixel.NeoPixel(machine.Pin(48),1)
#object for button
button = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)
value = 0
#interrupt service routine
def toggle_led(p):
    
    global value
    
    if value == 0:
        value = 255
    elif value == 255:
        value = 0
    np[0] = (0,value,0)
    np.write()
    
button.irq(trigger=machine.Pin.IRQ_FALLING,handler=toggle_led)

while True:
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        print("Exit")
        break
