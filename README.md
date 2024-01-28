in this project i implement a webserver on a Raspberry Pi for displaying temperature data from a
DS18B20 sensor, three components are used: a Flask web application (app.py) for the webserver, a
Python script (temperature display.py) for reading sensor data and converting temperatures, and an
HTML document to render the temperature and time on a webpage titled ”Temperature Monitor.” The
Flask app integrates real-time sensor data into the webpage, dynamically updating temperature readings
in Celsius and Fahrenheit, while styling is managed through a linked CSS file
