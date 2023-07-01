# Soil Guardian 3000 

#### By jb225ps

In this tutorial, you will learn how to create a soil moisture sensor IoT device using a Raspberry Pico W microcontroller, a soil moisture sensor, a DHT-11 sensor, a breadboard, MicroPython and some jumper wires. By the end of this tutorial, you'll have a functioning device that can measure soil moisture levels and send the data to a remote server for analysis and monitoring.

Estimated time of project is about 10hrs

## Objective

The purpose of this soil moisture sensor IoT device also called "Soil guardian 3000" is to measure and monitor soil moisture levels, humidity and temperature in real-time. By placing the sensor within the soil, it continuously provides readings that indicate the moisture content. 

This can further be analyzed to see correlations between the parameters and the plants health. This information can further guide you in optimizing the conditions for the plant.


## List of material

For this project you need:

#### Raspberry Pi Pico WH
[Link](https://www.electrokit.com/produkt/raspberry-pi-pico-wh/) *109:- SEK* <br>
The Raspberry Pi Pico WH is a microcontroller board based on the RP2040 chip. It has a dual-core ARM Cortex-M0+ processor. The Pico WH variant includes pre-soldered headers, making it convenient for a breadboard-based project like this. It can be programmed using MicroPython, C/C++, or other compatible programming languages. <img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/PICO-WH.jpg" width="385px">

#### Bread board
A breadboard is a versatile prototyping tool used for building and testing electronic circuits. It consists of a grid of holes into which electronic components can be inserted and interconnected without the need for soldering. The breadboard is used as a platform to connect the Raspberry Pi Pico and the sensors using jumper wires.
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/breadboard.jpg" width="385px">

#### DHT-11 sensor
The DHT-11 sensor is a low-cost sensor that measures temperature and humidity. The sensor operates within a specific temperature and humidity range and does reasonable accuracy for most general-purpose applications. <img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/dht-11.jpg" width="385px" >

#### Capcitive Soil Moisture Sensor
The capacitive soil moisture sensor is a sensor specifically designed to measure the moisture content of soil. 
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/capsensor.jpg" width="385px">

#### Jumper wires
Jumper wires are used to establish electrical connections between different components on a breadboard or between the breadboard and other devices. <br>
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/wires.jpg" width="385px">

#### Micro USB cable
A Micro USB cable is used to provide power to the Raspberry Pi Pico and establish a data connection for programming.<br> <img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/microUSB.jpg" width="385px">

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

***
## Computer setup
This tutorial is for Windows but is pretty similar on other operating systems. 
* Step 1: Download and install Node js [HERE](https://nodejs.org/en)
* Step 2: Download and install VS Code [HERE](https://code.visualstudio.com/Download)
* Step 3: Open VS Code and go to the extensions manager. Search for the **Pymakr** plugin and install it. (see image for steps)
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/pymakr.png" width="450px">

## Pico setup
* Step 1: Download the **Micropython** firmware [HERE](https://micropython.org/download/rp2-pico-w/). Make sure to download the lates **uf2** file under releases. (lägg in bild)
* Step 2: Connect the micro-usb cable to your Raspberry Pi Pico. (Don't put the other end in the PC yet..)
* Step 3: While holding down the **BOOTSEL** button on the RPi Pico (the small little button close to the micro-usb port) connect the other end of the USB cable to your computer. Release the button after you se your device pop up on your computer.
* Step 4: In your file system you will see a new drive called **RPI-RP2** which is your RPi Pico device. Paste the **uf2** file you previously downloaded and add it to the device. The Raspberry Pi Pico will automatically disconnect from your computer and reconnect. Now your RPi Pico is flashed with Micropython and ready to go.

## Putting everything together
Start with connecting the Pico and the sensors to the breadboard then connect all the wires. (You can do this however you want but make sure you are connecting everything as it should) Here is a circuit diagram on how i did it:
<br><img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/circut_soil3000.png" width="385px" align="left"><br>

## The Code
The project's code consists of four Python files. You can either use the ```git pull``` command to fetch the files or manually copy them from this directory and paste them into your IDE. Here is a brief overview of what each file contains:
* **boot.py** This is where the pico connects to WiFi. It start with importing your WiFi credentials from the **keys.py** file and then continues to set up a connection to your WiFi.
* **keys.py** This file holds all your crucial credentials.
```python
WIFI_SSID = "insert_wifi_ssid"
WIFI_PASS = "inser_wifi_password"

AIO_USER = "insert_adafruit_username"
AIO_KEY = "insert_adafruit_api_token"
AIO_LUFTFUKTIGHET = "insert_feed_for_humidity"
AIO_TEMPERATUR = "insert_feed_for_temperature"
AIO_MOIST = "insert_for_soil_moisture"
```
* **mqtt.py** 
Since we are going to use the **MQTT** protocol to send our collected data to adafruit we need the following library. (this is a straight copy from [HERE](https://github.com/iot-lnu/applied-iot/blob/master/Raspberry%20Pi%20Pico%20(W)%20Micropython/network-examples/N2_WiFi_MQTT_Webhook_Adafruit/lib/mqtt.py))
* **main.py**
Here is where the main program is going to start and run. It's also here where we have the functions to collect and send the data from our sensors. 


## Platform and data transmitting

I've choose **adafruit** as platform to display the data. It's an cloud-serice that provides a simple and easy way to display data in real-time online. They have a free plan that offers 10 "feeds" with 30 entries per minute with a storage of 30 days which suited this project perfectly. If i would have done a project where i would need the data stored for a longer period of time I probably would've done something self hosted depending on the size of the project.

To transmit data to the Adafruit platform i choose WiFi since i will have this device connected at home where I have stable WiFi connectivity. I tried experimenting with LoRaWAN but did not have coverage in my area.

Regarding transport protocol I choose MQTT(Message Queuing Telemetry Transport) which provides a lightweight and secure protocol for data transmission

Im collecting data every 20 seconds but this can easily be changed in the ```main.py``` file by changeing the ```RANDOMS_INTERVAl``` variable.
```python
# Variables
RANDOMS_INTERVAL = 20000                    # (milliseconds). How often data is sent to Adafruit
last_random_sent_ticks = 0                  # (milliseconds). Used to keep track of the last time data was sent to Adafruit IO
temp_sensor = dht.DHT11(machine.Pin(27))    # DHT11 Constructor 
soil_sensor = ADC(machine.Pin(26))          # Capacitive Soil Moisture Sensor v1.2
moist_wet=13347                             # Moisture sensor calibration.
moist_dry=42986

```

## Presenting the data
In terms of presenting the data I've choosen three line grafs with an matching gauge. The temperature has two limits, 21C and 26C. In between that is shown in green as an OK temperature. If the temperature goes above that it changes to red to indicate that its too hot and if it's going below 21 it turns blue to indicate that its to cold.
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/temp.png" width="600px">
***
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/high_temp.png" width="600px">


## Finalizing the design
(Inser pictures with the flower)
