from picamera import PiCamera
import datetime

camera = PiCamera()

camera.capture('test + %Y %M %d %h %m %s.jpg')



