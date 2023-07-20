# Libraries
import RPi.GPIO as GPIO
from time import sleep

# Disable warnings (optional)
GPIO.setwarnings(False)

# Select GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set buzzer - pin 11 as output
buzzer = 11
GPIO.setup(buzzer, GPIO.OUT)

# Run the forever loop
while True:
    GPIO.output(buzzer, GPIO.HIGH)   # Turn on the buzzer
    print("Beep")                   # Print "Beep" in the console
    sleep(0.5)                      # Delay for 0.5 seconds
    GPIO.output(buzzer, GPIO.LOW)    # Turn off the buzzer
    print("No Beep")                # Print "No Beep" in the console
    sleep(0.5)                      # Delay for 0.5 seconds
