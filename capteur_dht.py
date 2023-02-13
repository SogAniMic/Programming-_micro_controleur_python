import dht
import machine
import time

d = dht.DHT11(machine.Pin(5))

while True: 
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print("Température :",temp, "°C")
    print("Humidité :",hum, "%")
    time.sleep_ms(500)
    

