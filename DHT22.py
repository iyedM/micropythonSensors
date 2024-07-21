# -*- coding: utf-8 -*-
"""
DHT22 Sensor MicroPython
@author: User
"""
import machine
import dht
import time

dht_pin = machine.Pin(15)
dht_sensor = dht.DHT22(dht_pin)

def read_dht22():
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()
    return temp, hum

while True:
    temperature, humidity = read_dht22()
    print("Temperature:", temperature, "C")
    print("Humidity:", humidity, "%")
    time.sleep(2)

