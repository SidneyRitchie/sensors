from time import sleep
from datetime import datetime

from sensors.humidity_temperature import get_humidity, get_temperature
from sensors.soil_moisture import get_soil_moisture
from sensors.light import get_light_level

from lib.logger import log

	
while True:

	light_level = get_light_level()
	humidity = get_humidity()
	temperature = get_temperature()
	soil_moisture = get_soil_moisture()

	if(not soil_moisture):
		soil_moisture_text = "Trocken"
	else:
		soil_moisture_text = "Feucht"

		

	log(temperature,humidity,soil_moisture,light_level)

	sleep(30)