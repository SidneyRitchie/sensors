import Adafruit_DHT # type: ignore

sensor = Adafruit_DHT.DHT22
pin = 12
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

def getHumidity():
    return humidity

def getTemperature():
    return temperature