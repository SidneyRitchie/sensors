import os
from datetime import datetime
from lib.csv import write_to_file

FIELDNAMES = ["time","temperature", "humidity", "soil_moisture", "light_level"]

def log(temperature, humidity, soil_moisture, light_level):

    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")

    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": temperature,
        "humidity": humidity,
        "soil_moisture":soil_moisture,
        "light_level": light_level
    }

    check_directories(year, month)
    write_to_file("data/"+year+"/"+month+"/"+year+"-"+month+"-"+day+".csv", FIELDNAMES, data)


def check_directories(year, month):

    if not os.path.isdir("data/" + year):
        os.mkdir("data/" + year)

    if not os.path.isdir("data/" + year + "/" + month):
        os.mkdir("data/" + year + "/" + month)
    
    if not os.path.isdir("pictures/" + year):
        os.mkdir("pictures/" + year)

    if not os.path.isdir("pictures/" + year + "/" + month):
        os.mkdir("pictures/" + year + "/" + month)
