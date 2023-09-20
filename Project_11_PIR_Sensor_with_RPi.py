import RPi.GPIO as GPIO
import time

#define pin no
PIR_input=29 #pir sensor output pin
LED=32 #led pin for signaling motion detection

#configure gpio settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #use board pin no system
GPIO.setup(PIR_input,GPIO.IN) #set PIR_input as input
GPIO.setup(LED,GPIO.OUT) # set led as output
GPIO.output(LED,GPIO.LOW) #initially turn off the led

while True:
    #check if motion is detected by reading the pir input (1 if high ,0 if low )
    if GPIO.input(PIR_input)==GPIO.HIGH:
        #turn on the led if motion is detected
        GPIO.output(LE,GPIO.HIGH)
    else:
        #turn off the led if no motion is detected
        GPIO.output(LED,GPIO.LOW)
        
    time.sleep(0.1) #small delay to control the loop 
        
        
        
        
