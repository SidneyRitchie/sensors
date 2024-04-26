import os
from datetime import datetime

def log(temperature, humidity, soil_moisture, light_level):

    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")
    hour = datetime.now().strftime("%H")
    minute = datetime.now().strftime("%M")
    second = datetime.now().strftime("%S")

    print("{0},{1},{2},{3}".format(temperature, humidity, soil_moisture, light_level))

    # überprüfen, ob ordner für das jahr existiert
    if os.path.isdir("data/" + year):
        print("dir gibt es")
    else:
        print("dir gibt es nicht")

    # überprüfen, ob ordner für den monat existiert
    # überprüfen, ob es eine csv datei von heute gibt
