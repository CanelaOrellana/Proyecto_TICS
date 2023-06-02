import Adafruit_DHT
import RPi.GPIO as GPIO
import numpy as np
from utils import Memory
import time
import matplotlib.pyplot as plt

pin = 4
GPIO.setmode(GPIO.BCM) 
sensor = Adafruit_DHT.DHT11
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


def medicion():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	if humidity is not None and temperature is not None:
    		temperature = round(temperature, 2)
    		humidity = round(humidity, 2)
    		print("Temperatura = {}°C, Humedad = {}%".format(temperature, humidity))
	else:
	    	print("Error al leer los datos del sensor.")
	return(humidity,temperature)

def graph(trigger_msg,temp,hum):
	# Recibe memorias de humedad y temperatura y va graficando 
	while trigger_msg is not False:
		time.sleep(10)
		humidity,temperature = medicion()
		temp.add(temperature)
		hum.add(humidity)
	pass
	
if __name__ == "__main__":
	Humidity = Memory(100)
	Temperature = Memory(100)
	

