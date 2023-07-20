import RPi.GPIO as GPIO
from time import sleep

# Set the GPIO mode to use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Set pin 7 as an output pin for the LED
GPIO.setup(7, GPIO.OUT)

# Set pin 11 as an input pin for the push button
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True: # Run forever
    if GPIO.input(11) == GPIO.LOW: # Check if the button is pressed
        GPIO.output(7, GPIO.HIGH) # Turn on the LED
    else:
        GPIO.output(7, GPIO.LOW) # Turn off the LED
    sleep(0.1) # Add a small delay to avoid rapid toggling
