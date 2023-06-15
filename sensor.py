# Imports
import Adafruit_DHT
import RPi.GPIO as GPIO
from datetime import datetime,time

# Pines de conexión de sensor
pin = 4
GPIO.setmode(GPIO.BCM) 
sensor = Adafruit_DHT.DHT11

def medicion():
    # Realiza una medición del 
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        # Redondea a 2 decimales
        humidity = round(humidity,2)
        temperature = round(temperature,2)
    else:
        raise Exception("No se han obtenido datos")    
    return (humidity,temperature)
