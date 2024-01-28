#!/usr/bin/env python
import os
import datetime
import time



# Funktion zur Identifizierung des DS18B20-Sensors
def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

# Funktion zum Lesen der Temperaturdaten vom DS18B20-Sensor
def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    fahrenheit = (celsius * 1.8) + 32
    return celsius, fahrenheit

try:
    while True:
        serialNum = sensor()
        celsius, fahrenheit = read(serialNum)


        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'Temperatur (Celsius): {celsius:.2f}°C')
        print(f'Temperatur (Fahrenheit): {fahrenheit:.2f}°F')
        print(f'Aktuelles Datum und Uhrzeit: {current_datetime}')
        print('---------------------------------------')
        time.sleep(2)  # 2 Sekunden Pause vor erneuter Messung

except KeyboardInterrupt:
    GPIO.cleanup()
