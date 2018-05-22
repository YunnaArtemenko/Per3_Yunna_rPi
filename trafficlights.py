from gpiozero import Button

button = Button(22)

button.wait_for_press()
print("Pressed")
button.wait_for_release()
print("Released")