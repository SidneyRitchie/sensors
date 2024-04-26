from time import sleep
from datetime import datetime

from sensors.humidity_temperature import get_humidity, get_temperature
from sensors.soil_moisture import get_soil_moisture
from sensors.light import get_light_level

from lib.logger import log

try:
	while True:

		light_level = get_light_level()
		humidity = get_humidity()
		temperature = get_temperature()
		soil_moisture = get_soil_moisture()

		if(not soil_moisture):
			soil_moisture = "Trocken"
		else:
			soil_moisture = "Feucht"

		print("-------------------------")
		print("| {0} |".format(datetime.now().strftime("%Y.%m.%d - %H:%M:%S")))
		print("-------------------------")
		print("Temperatur = {0:0.1f}°C".format(temperature))
		print("Luftfeuchtigkeit = {0:0.1f}%".format(humidity))
		print("Lichtstärke = {0:.2f}lux".format(light_level))
		print("Bodenfeuchtigkeit = {0}".format(soil_moisture))
		print("")

		log(temperature,humidity,soil_moisture,light_level)

		sleep(10)

except KeyboardInterrupt:
	print("Script end!")
