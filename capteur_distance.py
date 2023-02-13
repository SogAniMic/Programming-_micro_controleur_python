from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=5,echo_pin=18)

while True:
    distance = sensor.distance_mm()
    print(distance)
    time.sleep_ms(500)
    

