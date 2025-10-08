from machine import Pin
import time

#LED part
led = Pin(0, Pin.OUT) # 0
# motion sensor part
sensor = Pin(15, Pin.IN)
ruch = 0
# interrupt
def motion_detected(pin):
    global ruch
    ruch = 1
# przypisanie przerwania do pinu
sensor.irq(trigger=Pin.IRQ_RISING, handler=motion_detected)
while True:
    if ruch == 1:
        led.value(1)
        print("wykryto ruch")
        ruch = 0
        time.sleep(2)
        led.value(0)
    time.sleep(2)
    print("nie wykryto ruchu")