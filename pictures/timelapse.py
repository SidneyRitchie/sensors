from picamera import PiCamera # type: ignore
from datetime import datetime
from time import sleep

def take_camera_picture():
    
    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")
    hour = datetime.now().strftime("%h")
    minute = datetime.now().strftime("%m")

    with PiCamera() as camera:
            camera.resolution(2592,1944)
            camera.start_preview()
            # Warm Up Time
            sleep(2)
            camera.capture('pictures/"+year+"/"+month+"/"+year+"-"+month+"-"+day+"-"+hour+"-"+minute+".jpg')
            camera.stop_preview()
            camera.close() 