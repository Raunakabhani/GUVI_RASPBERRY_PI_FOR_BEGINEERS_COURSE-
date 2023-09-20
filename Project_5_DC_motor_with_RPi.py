# Import the required libraries
import RPi.GPIO as GPIO
from time import sleep

# Define the motor control pins
ENA = 17  # Enable Pin
IN1 = 27  # Control Pin 1
IN2 = 22  # Control Pin 2

# Set up the GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Function to move the motor forward
def forward():
    GPIO.output(ENA, GPIO.HIGH)  # Enable the motor
    GPIO.output(IN1, GPIO.HIGH)  # Set control pin 1 high
    GPIO.output(IN2, GPIO.LOW)   # Set control pin 2 low

# Function to move the motor backward
def backward():
    GPIO.output(ENA, GPIO.HIGH)  # Enable the motor
    GPIO.output(IN1, GPIO.LOW)   # Set control pin 1 low
    GPIO.output(IN2, GPIO.HIGH)  # Set control pin 2 high

# Main loop
while True:
    forward()  # Move the motor forward
    sleep(1)   # Wait for 1 second
    backward() # Move the motor backward
    sleep(1)   # Wait for 1 second
