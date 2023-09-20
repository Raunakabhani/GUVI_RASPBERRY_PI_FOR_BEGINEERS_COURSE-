import RPi.GPIO as GPIO
import time

# Set pin numbers for sensor and buzzer
sensor = 16
buzzer = 18

# Set GPIO mode and setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

# Initialize buzzer state as off (LOW)
GPIO.output(buzzer, GPIO.LOW)
print("IR Sensor Ready.....")
print(" ")

try: 
    while True:
        if GPIO.input(sensor):
            # If object detected, turn on the buzzer (HIGH) and print message
            GPIO.output(buzzer, GPIO.HIGH)
            print("Object Detected")
            # Wait until object is no longer detected
            while GPIO.input(sensor):
                time.sleep(0.2)
        else:
            # If no object detected, turn off the buzzer (LOW)
            GPIO.output(buzzer, GPIO.LOW)
except KeyboardInterrupt:
    # Clean up GPIO configuration on keyboard interrupt
    GPIO.cleanup()
