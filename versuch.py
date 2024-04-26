import smbus # type: ignore
import time
from datetime import datetime

from sensors.humidity_temperature import get_humidity, get_temperature
from sensors.soil_moisture import get_soil_moisture

DEVICE = 0x23
POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07
CONTINUOUS_LOW_RES_MODE = 0x13
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_HIGH_RES_MODE_2 = 0x21
ONE_TIME_LOW_RES_MODE = 0x23

bus = smbus.SMBus(1)

def convertToNumber(data):
	result=(data[1] + (256 * data[0])) / 1.2
	return result

def readLight(addr=DEVICE):
	data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
	return convertToNumber(data)

print('[Press CTRL + C to end the script!]')
try:
	while True:
# Licht wie stark
		lightLevel = readLight()
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
		print("Lichtstärke = {0:.2f}lux".format(lightLevel))
		print("Bodenfeuchtigkeit = {0}".format(soil_moisture))
		print("")

		time.sleep(10)


# Scavenging work after the end of the program
except KeyboardInterrupt:
	print("Script end!")
