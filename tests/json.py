from datetime import datetime
from lib.json import write_json_file

data = {
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "temperature": 20,
    "humidity": 20,
    "soil_moisture":20,
    "light_level": 20
}

write_json_file("test.json", data)
