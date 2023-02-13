from machine import Pin,PWM
import time

pwm = PWM(Pin(2))
pwm.duty(50)
pwm.freq(50)