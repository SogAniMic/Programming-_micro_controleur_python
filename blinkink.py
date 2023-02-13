from machine import Pin
import time

p = Pin(2,Pin.OUT)
for i in range(10):
    p.on()
    time.sleep(1)
    p.off()
    time.sleep_ms(500)