import machine
from hcsr04 import HCSR04
from i2c_lcd import I2cLcd
from machine import I2C,Pin
import time
import dht


sensor = HCSR04(trigger_pin=5,echo_pin=18)
distance = sensor.distance_mm()


d = dht.DHT11(machine.Pin(19))
d.measure()
temp = d.temperature()
hum = d.humidity()

address = 0x27
i2c = I2C(scl=Pin(22),sda=Pin(21),freq=400000)
lcd = I2cLcd(i2c,address,2,16)
lcd.display_on()
lcd.backlight_on()
lcd.putstr("Distance : ")
lcd.putstr(distance)
lcd.putstr("Temperature : ")
lcd.putstr(temp)


