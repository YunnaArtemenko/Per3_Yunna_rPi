from gpiozero import LED, Button
from time import sleep

led = LED(19)
button = Button(16)

button.when_pressed = led.on
button.when_released = led.off
pause()