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
    if not os.path.isdir("data/" + year):
        os.mkdir("data/" + year)

    # überprüfen, ob ordner für den monat existiert
    if not os.path.isdir("data/" + year + "/" + month):
        os.mkdir("data/" + year + "/" + month)

    # überprüfen, ob es eine csv datei von heute gibt
    if not os.path.isfile("data/" + year + "/" + month + "/" + year + "_" + month + "_" + day):
        print("datei existiert")
        # falls ja: sensordaten ans ende schreiben
        # falls nein: csv datei erstellen und daten ans ende schreiben
