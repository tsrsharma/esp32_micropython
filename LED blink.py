import machine
import time

led = machine.Pin(8,machine.Pin.OUT) #object for LED pin

while True:
    try:
        led.value(not led.value())
        print ("LED is on" if led.value() else "LED is off")
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exit")
        break