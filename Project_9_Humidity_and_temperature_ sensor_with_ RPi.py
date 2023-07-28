import sys
import Adafruit_DHT
import time

# Main loop to continuously read temperature and humidity from DHT11 sensor
while True:
    # Read temperature and humidity from DHT11 sensor (connected to GPIO pin 4)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    # Print temperature and humidity values with formatting
    print('Temperature: {0:0.1f}°C  Humidity: {1:0.1f}%'.format(temperature, humidity))

    # Wait for 1 second before reading again
    time.sleep(1)
