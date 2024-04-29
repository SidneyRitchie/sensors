from gpiozero import DigitalInputDevice # type: ignore

d0_input = DigitalInputDevice(17)

def get_soil_moisture():
    return d0_input.value
