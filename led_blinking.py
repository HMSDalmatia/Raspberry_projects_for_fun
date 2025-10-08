from machine import Pin
import time
led = Pin(0, Pin.OUT) # 0
while True:
    led.value(1)
    time.sleep(2)
    led.value(0)
    time.sleep(2)