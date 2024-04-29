from picamera import PiCamera # type: ignore

def take_picture(filename):

    with PiCamera() as camera:
        camera.capture(filename)
        camera.close()
