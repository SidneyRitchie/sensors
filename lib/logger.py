import os
from datetime import datetime

from lib.csv import write_to_file
from devices.camera import take_picture

FIELDNAMES = ["time","temperature", "humidity", "soil_moisture", "light_level"]

def log(temperature, humidity, soil_moisture, light_level):

    check_directories(year, month)

    now = datetime.now()

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")

    data = {
        "time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": temperature,
        "humidity": humidity,
        "soil_moisture":soil_moisture,
        "light_level": light_level
    }

    write_to_file("data/"+year+"/"+month+"/csv/"+year+"-"+month+"-"+day+".csv", FIELDNAMES, data)
    take_picture("data/"+year+"/"+month+"/images/"+year+"-"+month+"-"+day+"-"+hour+"-"+minute+"-"+second+".jpg")


def check_directories(year, month):


    if not os.path.isdir("data/" + year):
        os.mkdir("data/" + year)

    if not os.path.isdir("data/" + year + "/" + month):
        os.mkdir("data/" + year + "/" + month)
    
    if not os.path.isdir("data/" + year + "/" + month + "/images"):
        os.mkdir("data/" + year + "/" + month + "/images")

    if not os.path.isdir("data/" + year + "/" + month + "/csv"):
        os.mkdir("data/" + year + "/" + month + "/csv")