from picamera import PiCamera # type: ignore
from time import sleep

def take_picture(filename):

    with PiCamera() as camera:
        camera.capture(filename)
        camera.close() 