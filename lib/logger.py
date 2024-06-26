import os
from datetime import datetime

from lib.csv import write_csv_file
from lib.json import write_json_file
from devices.camera import take_picture

FIELDNAMES = ["time", "temperature", "humidity", "soil_moisture", "light_level"]

def log(temperature, humidity, soil_moisture, light_level):

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

    base_path = f"data/{year}/{month}"
    
    check_directories(base_path)
    write_csv_file(f"{base_path}/csv/{year}-{month}-{day}.csv", FIELDNAMES, data)
    write_json_file(f"{base_path}/json/{year}-{month}-{day}.json", data)
    take_picture(f"{base_path}/images/{year}-{month}-{day}-{hour}-{minute}-{second}.jpg")


def check_directories(base_path):
    
    create_directory_if_not_exists(base_path)
    create_directory_if_not_exists(f"{base_path}/csv")
    create_directory_if_not_exists(f"{base_path}/json")
    create_directory_if_not_exists(f"{base_path}/images")


def create_directory_if_not_exists(path):

    if not os.path.isdir(path):
        os.makedirs(path)
