from machine import Pin
from time import sleep

led = Pin(2,Pin.OUT)
led_state = True

while True:
    led_state = not led_state
    led.value(led_state)
    print("LED turned on" if led_state else "LED turned off")
    sleep(.5)