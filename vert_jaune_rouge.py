from machine import Pin
import time


vert = Pin(5,Pin.OUT)
jaune = Pin(18, Pin.OUT)
rouge = Pin(19, Pin.OUT)


vert.on()
jaune.off()
rouge.off()
time.sleep(5)
    
vert.off()
jaune.on()
rouge.off()
time.sleep(5)

vert.off()
jaune.off()
rouge.on()
time.sleep(5)


