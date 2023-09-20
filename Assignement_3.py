import RPi.GPIO as GPIO
from time import sleep

# Define GPIO pins for left motor
leftForwardPin = 7
leftBackwardPin = 11
leftEnablePin = 13

# Define GPIO pins for right motor
rightForwardPin = 8
rightBackwardPin = 10
rightEnablePin = 12

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set up GPIO pins for left motor
GPIO.setup(leftForwardPin, GPIO.OUT)
GPIO.setup(leftBackwardPin, GPIO.OUT)
GPIO.setup(leftEnablePin, GPIO.OUT)

# Set up GPIO pins for right motor
GPIO.setup(rightForwardPin, GPIO.OUT)
GPIO.setup(rightBackwardPin, GPIO.OUT)
GPIO.setup(rightEnablePin, GPIO.OUT)

# Initialize PWM for left motor enable pin
leftEnPWM = GPIO.PWM(leftEnablePin, 100)
leftEnPWM.start(50)  # Starting duty cycle at 50%
GPIO.output(leftEnablePin, GPIO.HIGH)

# Initialize PWM for right motor enable pin
rightEnPWM = GPIO.PWM(rightEnablePin, 100)
rightEnPWM.start(50)  # Starting duty cycle at 50%
GPIO.output(rightEnablePin, GPIO.HIGH)

try:
    while True:
        # Move both motors forward
        GPIO.output(leftForwardPin, GPIO.HIGH)
        GPIO.output(rightForwardPin, GPIO.HIGH)
        sleep(1)

        # Increase duty cycle to 100%
        leftEnPWM.ChangeDutyCycle(100)
        rightEnPWM.ChangeDutyCycle(100)
        sleep(1)

        # Reduce duty cycle to 50%
        leftEnPWM.ChangeDutyCycle(50)
        rightEnPWM.ChangeDutyCycle(50)
        sleep(1)

        # Stop both motors
        GPIO.output(leftForwardPin, GPIO.LOW)
        GPIO.output(rightForwardPin, GPIO.LOW)
        sleep(1)

        # Move both motors backward
        GPIO.output(leftBackwardPin, GPIO.HIGH)
        GPIO.output(rightBackwardPin, GPIO.HIGH)
        sleep(1)

        # Increase duty cycle to 100%
        leftEnPWM.ChangeDutyCycle(100)
        rightEnPWM.ChangeDutyCycle(100)
        sleep(1)

        # Reduce duty cycle to 50%
        leftEnPWM.ChangeDutyCycle(50)
        rightEnPWM.ChangeDutyCycle(50)
        sleep(1)

        # Stop both motors
        GPIO.output(leftBackwardPin, GPIO.LOW)
        GPIO.output(rightBackwardPin, GPIO.LOW)
        sleep(1)

except KeyboardInterrupt:
    # Cleanup GPIO on program exit
    leftEnPWM.stop()
    rightEnPWM.stop()
    GPIO.cleanup()
