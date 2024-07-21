# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:09:34 2024

@author: User
"""

import uasyncio as asyncio
import machine
import dht
import network
import umqtt.simple as mqtt

# Sensor and relay setup
dht_pin = machine.Pin(15)
dht_sensor = dht.DHT22(dht_pin)
mq2_pin = machine.ADC(26)
relay_pin = machine.Pin(18, machine.Pin.OUT)

# WiFi and MQTT setup
ssid = 'your_wifi_ssid'
password = 'your_wifi_password'
mqtt_broker = 'your_mqtt_broker_ip'
client_id = 'raspberry_pi_pico'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

print("Connected to WiFi")

client = mqtt.MQTTClient(client_id, mqtt_broker)
client.connect()

async def read_dht22():
    while True:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        print("Temperature:", temp, "C")
        print("Humidity:", hum, "%")
        await asyncio.sleep(2)

async def read_mq2():
    while True:
        gas_level = mq2_pin.read_u16()
        print("Gas Level:", gas_level)
        await asyncio.sleep(2)

async def control_relay():
    while True: # a3mlelha modification selon kifech bech tnadiha fl app 
        relay_pin.value(1)  # Turn on the relay
        await asyncio.sleep(5)
        relay_pin.value(0)  # Turn off the relay
        await asyncio.sleep(5)

async def send_mqtt():
    while True:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        gas_level = mq2_pin.read_u16()
        message = f"Temperature: {temp} C, Humidity: {hum} %, Gas Level: {gas_level}"
        client.publish("sensor/data", message)
        await asyncio.sleep(10)

loop = asyncio.get_event_loop()
loop.create_task(read_dht22())
loop.create_task(read_mq2())
loop.create_task(control_relay())
loop.create_task(send_mqtt())
loop.run_forever()
