import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BOARD)    # Set the GPIO pin numbering mode to BOARD
gp.setup(23, gp.IN)     # Set pin 23 as input (reading from sensor)
gp.setup(33, gp.OUT)    # Set pin 33 as output (LED)

while True:
    try:
        if gp.input(23) == 1:     # If the input from pin 23 is HIGH (1)
            gp.output(33, gp.HIGH)    # Turn on the LED (set pin 33 to HIGH)
        elif gp.input(23) == 0:   # If the input from pin 23 is LOW (0)
            gp.output(33, gp.LOW)     # Turn off the LED (set pin 33 to LOW)
    except KeyboardInterrupt:   # If the user interrupts the program with Ctrl+C
        gp.cleanup()   # Clean up GPIO settings
        break   # Exit the loop and end the program
