import dht
import time
import keys
import ubinascii  
import machine
from mqtt import MQTTClient 
from machine import ADC 

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = keys.AIO_USER
AIO_KEY = keys.AIO_KEY
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_MOIST_FEED = keys.AIO_LUFTFUKTIGHET
AIO_TEMP_FEED = keys.AIO_TEMPERATUR
AIO_SOIL_MOIST_FEED = keys.AIO_MOIST

# Variables
RANDOMS_INTERVAL = 20000                    # (milliseconds). How often data is sent to Adafruit
last_random_sent_ticks = 0                  # (milliseconds). Used to keep track of the last time data was sent to Adafruit IO
temp_sensor = dht.DHT11(machine.Pin(27))    # DHT11 Constructor 
soil_sensor = ADC(machine.Pin(26))          # Capacitive Soil Moisture Sensor v1.2
moist_wet=13347                             # Moisture sensor calibration.
moist_dry=42986

# Callback Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):          # sub_cb means "callbac subroutine"
    print((topic, msg))          # Outputs the message that was received. Debugging use.


# Functions to collect and send data
def send_data():
    global last_random_sent_ticks
    global RANDOMS_INTERVAL
    if ((time.ticks_ms() - last_random_sent_ticks) < RANDOMS_INTERVAL):
       return; # Too soon since last one sent.

    temp, hum, moist = measure_data()
    try:
        client.publish(topic=AIO_MOIST_FEED, msg=str(hum))
        client.publish(topic=AIO_TEMP_FEED, msg=str(temp))
        client.publish(topic=AIO_SOIL_MOIST_FEED, msg=str(moist))

    except Exception as e:
        print("client.publish() - FAILED")
    finally:
        last_random_sent_ticks = time.ticks_ms()

def measure_data():
    temp_sensor.measure()
    temperature = temp_sensor.temperature()
    humidity = temp_sensor.humidity()

    moisture = (moist_dry-soil_sensor.read_u16())*100/(moist_dry-moist_wet)

    print("\nTemperature is {} degrees Celsius \nHumidity is {}% \nSoil moisture is {}\n".format(temperature, humidity, str(moisture)))    
    return temperature, humidity, moisture


# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
client.set_callback(sub_cb)
client.connect()
client.subscribe(AIO_MOIST_FEED)
client.subscribe(AIO_TEMP_FEED)
client.subscribe(AIO_SOIL_MOIST_FEED)
print("Connected to %s, subscribed to %s and %s topic" % (AIO_SERVER, AIO_MOIST_FEED, AIO_TEMP_FEED))

try:
    while 1:
        client.check_msg()
        send_data()

except Exception as e:
    print("An error occurred:", str(e))
finally:
    client.disconnect()
    client = None
    print("Disconnected from Adafruit IO.")