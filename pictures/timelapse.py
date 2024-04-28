from picamera import PiCamera # type: ignore
from datetime import datetime
from time import sleep

def take_camera_picture():
    
    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")
    hour = datetime.now().strftime("%H")
    minute = datetime.now().strftime("%M")
    second = datetime.now().strftime("%S")

    with PiCamera() as camera:
            camera.capture("pictures/"+year+"/"+month+"/"+year+"-"+month+"-"+day+"-"+hour+"-"+minute+"-"+second+".jpg")
            camera.close() 