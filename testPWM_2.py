from machine import Pin,PWM
import time

pwm = PWM(Pin(2))
pwm.freq(50)

for i in range(1024):
    time.sleep_ms(100)
    pwm.duty(i)
    
pwm.duty(0)
    