import machine
import time

led = machine.Pin(8,machine.Pin.OUT)

button = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)
count = 0

while True:
    try:
        if button.value() == 0:
            led.value(not led.value())
            print(f"led is on{count}" if led.value() else f"led is off{count}")
            count = count + 1
            while button.value() == 0:
                time.sleep_ms(20)
            
    except KeyboardInterrupt:
        print("Exit")
        break