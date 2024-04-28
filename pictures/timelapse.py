from picamera import PiCamera # type: ignore
from datetime import datetime

camera = PiCamera()

def take_camera_picture():
    
    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    day = datetime.now().strftime("%d")
    hour = datetime.now().strftime("%h")
    minute = datetime.now().strftime("%m")

    with PiCamera() as camera:
            camera.capture("0000")
            # camera.capture("pictures/"+year+"/"+month+"/"+year+"-"+month+"-"+day+"-"+hour+"-"+minute+".jpg")
            camera.stop_preview()
            camera.close() 