import Adafruit_DHT
import RPi.GPIO as GPIO
import numpy as np

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

def grafico(trigger_msg, humidity, temperature, max_n = 50):
	humedad = np.zeros(max_n)
	temperatura = np.zeros(max_n)
	humidity,temperature = medicion()
	pass




