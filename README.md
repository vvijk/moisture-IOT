# moisture-IOT

_By jb225ps_

In this tutorial, you will learn how to create a soil moisture sensor IoT device using a Raspberry Pico W microcontroller, a soil moisture sensor, a DHT-11 sensor, a breadboard, MicroPython, and some jumper wires. By the end of this tutorial, you'll have a functioning device that can measure soil moisture levels and send the data to a remote server for analysis and monitoring.

Estimated time of the project is about 10 hrs

## Objective

The purpose of the Soil Guardian 3000 soil moisture sensor IoT device is to measure and monitor soil moisture levels, humidity, and temperature in real-time. By placing the sensor within the soil, it continuously provides readings that indicate the moisture content. This information can be further analyzed to optimize the conditions for the plant and improve its health.

## List of Materials

For this project, you will need the following materials:

#### Raspberry Pi Pico WH

<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/PICO-WH.jpg" width="300px">

Description: The Raspberry Pi Pico WH is a microcontroller board based on the RP2040 chip. The Pico WH variant includes pre-soldered headers, making it convenient for a breadboard-based project like this. It can be programmed using MicroPython, C/C++, or other compatible programming languages.
* RP2040 CPU
* ARM Cortex-M0+ 133MHz
* 256kB RAM
* 30 GPIO pins
* 2MB on-board QSPI Flash
* CYW43439 wireless chip
* IEEE 802.11 b/g/n wireless LAN


#### Breadboard
![Breadboard](https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/breadboard.jpg)


Description: A breadboard is a versatile prototyping tool used for building and testing electronic circuits. It consists of a grid of holes into which electronic components can be inserted and interconnected without the need for soldering. The breadboard is used as a platform to connect the Raspberry Pi Pico and the sensors using jumper wires.

#### DHT-11 Sensor
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/dht-11.jpg" width="300px">

Description: The DHT-11 sensor is a low-cost sensor that measures temperature and humidity. The sensor operates within a specific temperature and humidity range and provides reasonable accuracy for most general-purpose applications.

#### Capacitive Soil Moisture Sensor
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/capsensor.jpg" width="300px">
Description: The capacitive soil moisture sensor is a sensor specifically designed to measure the moisture content of the soil.

#### Jumper Wires
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/wires.jpg" width="300px">
Description: Jumper wires are used to establish electrical connections between different components on a breadboard or between the breadboard and other devices.

#### Micro USB Cable
<img src="https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/microUSB.jpg" width="300px">
Description: A Micro USB cable is used to provide power to the Raspberry Pi Pico and establish a data connection for programming.

---

| Item | Cost (SEK) | Link (Not affiliated) |
| ----------------------------- | ---------- | ------------------------------------------------------------------------------------------------------- |
| Raspberry Pi Pico WH  | 109:- | [ElectroKit](https://www.electrokit.com/produkt/raspberry-pi-pico-wh/)  |
| Breadboard  | 69:- | [ElectroKit](https://www.electrokit.com/produkt/kopplingsdack-840-anslutningar/)  |
| DHT-11 Sensor | 49:- | [ElectroKit](https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/)  |
| Capacitive Soil Moisture Sensor | 68:-  | [Amazon](https://www.amazon.se/dp/B07HJ6N1S4?psc=1&ref=ppx_yo2ov_dt_b_product_details)  |
| Jumper Wires | 29:-  | [ElectroKit](https://www.electrokit.com/produkt/labbsladd-20-pin-15cm-hane-hane/)  |
| Micro USB Cable | 120:- | [Kjell&Co](https://www.kjell.com/se/produkter/kablar-kontakter/usb-kablar/micro-usb-kabel-1-m-p68687)  |

---

## Computer Setup

This tutorial is for Windows but is pretty similar on other operating systems.

### Step 1: Download and Install Node.js

Download and install Node.js from [HERE](https://nodejs.org/en).

### Step 2: Download and Install VS Code

Download and install VS Code from [HERE](https://code.visualstudio.com/Download).

### Step 3: Install Pymakr Plugin

Open VS Code and go to the extensions manager. Search for the **Pymakr** plugin and install it.

![Pymakr Plugin](https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/pymakr.png)

## Pico Setup

### Step 1: Download Micropython Firmware

Download the Micropython firmware for Raspberry Pi Pico WH from [HERE](https://micropython.org/download/rp2-pico-w/). Make sure to download the latest **uf2** file under releases.

### Step 2: Connect Raspberry Pi Pico

Connect the micro-USB cable to your Raspberry Pi Pico. (Don't put the other end in the PC yet..)

### Step 3: Flash Micropython Firmware

1. While holding down the **BOOTSEL** button on the RPi Pico (the small button close to the micro-USB port), connect the other end of the USB cable to your computer.
2. Release the button after you see your device pop up on your computer.
3. In your file system, you will see a new drive called **RPI-RP2** which is your RPi Pico device. Paste the **uf2** file you previously downloaded and add it to the device.
4. The Raspberry Pi Pico will automatically disconnect from your computer and reconnect. Now your RPi Pico is flashed with Micropython and ready to go.

---

## Putting Everything Together

Start by connecting the Raspberry Pi Pico and the sensors to the breadboard, then connect all the wires. You can arrange the components as desired, but make sure to connect everything correctly. Here is a circuit diagram showing how I did it:

![Circuit Diagram](https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/circut_soil3000.png)

---

## The Code

The project's code consists of four Python files. You can either use the `git pull` command to fetch the files or manually copy them from this directory and paste them into your IDE. Here is a brief overview of what each file contains:

1. **boot.py**: This is where the Pico connects to Wi-Fi. It imports the Wi-Fi credentials from the **keys.py** file and sets up a connection to the Wi-Fi network.
2. **keys.py**: This file holds all your crucial credentials, including Wi-Fi credentials and Adafruit credentials.
3. **mqtt.py**: This file contains the MQTT library used for sending data to Adafruit.
4. **main.py**: This is the main program file. It starts and runs the program, collects data from the sensors, and sends it to Adafruit.

---

## Platform and Data Transmitting

I have chosen Adafruit as the platform to display the data. Adafruit provides a simple and easy way to display data in real-time online. They offer a free plan that allows 10 feeds with 30 entries per minute and a storage period of 30 days, which is suitable for this project.

To transmit data to the Adafruit platform, Wi-Fi is used since the device will be connected at home with stable Wi-Fi connectivity. The MQTT (Message Queuing Telemetry Transport) protocol is chosen for data transmission due to its lightweight and secure nature.

Data is collected every 20 seconds, but you can easily change this interval in the `main.py` file by modifying the `RANDOMS_INTERVAL` variable.

```python
# Variables
RANDOMS_INTERVAL = 20000                    # (milliseconds). How often data is sent to Adafruit
last_random_sent_ticks = 0                  # (milliseconds). Used to keep track of the last time data was sent to Adafruit IO
temp_sensor = dht.DHT11(machine.Pin(27))    # DHT11 Constructor 
soil_sensor = ADC(machine.Pin(26))          # Capacitive Soil Moisture Sensor v1.2
moist_wet=13347                             # Moisture sensor calibration.
moist_dry=42986
```

*ADD MORE CODE*

---

## Presenting the Data

For presenting the data, three line graphs and a matching gauge are used. The temperature has two limits: 21°C and 26°C. The temperature range between these limits is shown in green, indicating an optimal temperature. If the temperature exceeds 26°C, it turns red to indicate that it's too hot, and if it goes below 21°C, it turns blue to indicate that it's too cold.

<h3 align="center">Ok temperature</h3>

![Temperature Graph](https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/temp.png)

---

<h3 align="center">High temperature</h3>

![High Temperature Graph](https://github.com/vvijk/Soil-Guardian-3000/blob/main/pictures/high_temp.png)

---

## Finalizing the Design

[Include pictures with the flower]
