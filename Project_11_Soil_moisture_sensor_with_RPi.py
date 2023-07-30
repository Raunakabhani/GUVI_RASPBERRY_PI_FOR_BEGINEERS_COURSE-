import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# Callback function to be called when water level changes
def callback(channel):
    if GPIO.input(channel):
        print("Water Detected!")
    else:
        print("No Water Detected!")

# Add event detection to monitor changes in water level
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

# Infinite loop to keep the program running
while True:
    time.sleep(1)  # Wait for 1 second between readings
