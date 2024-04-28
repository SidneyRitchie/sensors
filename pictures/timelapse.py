import os
from picamera import PiCamera # type: ignore
from datetime import datetime


camera = PiCamera()

def get_camera_image():
    
    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")
    hour = datetime.now().strftime("%h")
    minute = datetime.now().strftime("%m")

    with PiCamera() as camera:
        #Kamera Parameter
        camera.resolution = (2592, 1944) #Full Frame
        camera.capture("pictures/"+year+"/"+month+"/"+year+"-"+month+"-"+day+"-"+hour+"-"+minute+".jpg")




def check_directories(year, month):

    if not os.path.isdir("pictures/" + year):
        os.mkdir("pictures/" + year)

    if not os.path.isdir("pictures/" + year + "/" + month):
        os.mkdir("pictures/" + year + "/" + month)