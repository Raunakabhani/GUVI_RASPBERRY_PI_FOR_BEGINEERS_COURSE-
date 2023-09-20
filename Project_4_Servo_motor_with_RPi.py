import RPi.GPIO as GPIO
import time

# Define the GPIO pin for the servo
servoPIN = 17

# Set the GPIO mode to use BCM numbering
GPIO.setmode(GPIO.BCM)

# Configure the GPIO pin as an output
GPIO.setup(servoPIN, GPIO.OUT)

# Create a PWM object with a frequency of 50Hz
p = GPIO.PWM(servoPIN, 50)

# Start the PWM with an initial duty cycle of 2.5% (neutral position)
p.start(2.5)

try:
    while True:
        # Move the servo to 90 degrees (neutral position)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        
        # Move the servo to 180 degrees
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        
        # Move the servo to 0 degrees
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        
        # Move the servo back to 90 degrees
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)

except KeyboardInterrupt:
    # Stop the PWM and clean up the GPIO settings
    p.stop()
    GPIO.cleanup()
