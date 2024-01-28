#!/usr/bin/env python
import os
from flask import Flask, render_template
import datetime

app = Flask(__name__)

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

# Routenfunktion für die Startseite
@app.route('/')
def index():
    try:
        serialNum = sensor()
        celsius, fahrenheit = read(serialNum)

        # Aktuelles Datum und Uhrzeit abrufen
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return render_template('index.html', celsius=celsius, fahrenheit=fahrenheit, current_datetime=current_datetime)
    except Exception as e:
        return f"Fehler: {str(e)}"

if __name__ == '__main__':
    app.run(host='169.254.56.10', port=8080, debug=True)
