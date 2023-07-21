import RPi.GPIO as GPIO
import time

# Set the GPIO mode to use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for Trigger and Echo
GPIO_TRIG = 7  # Physical pin 7
GPIO_ECHO = 11  # Physical pin 11

# Set the GPIO mode for Trigger pin as output and Echo pin as input
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Initialize the Trigger pin to LOW and wait for 2 seconds
GPIO.output(GPIO_TRIG, GPIO.LOW)
time.sleep(2)

# Generate a short pulse of 10 microseconds on the Trigger pin
GPIO.output(GPIO_TRIG, GPIO.HIGH)
time.sleep(0.00001)
GPIO.output(GPIO_TRIG, GPIO.LOW)

# Measure the duration of the pulse on the Echo pin
while GPIO.input(GPIO_ECHO) == 0:
    start_time = time.time()

while GPIO.input(GPIO_ECHO) == 1:
    Bounce_back_time = time.time()

# Calculate the pulse duration and convert it to distance in centimeters
pulse_duration = Bounce_back_time - start_time
distance = round(pulse_duration * 17150, 2)

# Print the distance measured by the ultrasonic sensor
print(f"Distance: {distance} cm")

# Clean up the GPIO settings
GPIO.cleanup()
