import Adafruit_DHT # type: ignore

sensor = Adafruit_DHT.DHT22
pin = 12
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

def get_humidity():
    return humidity

def get_temperature():
    return temperature