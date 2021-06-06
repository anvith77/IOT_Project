## Introduction

A Head-up Display is a device that has a transparent display on which information is displayed, it is kept right in the line of sight of the driver. Drivers get all the important information such as speed, engine load, fuel load, and many other parameters without looking down at the dashboard of the car.

## Block Diagram Overview

Input signals or codes from the car's ECU are sent to the OBD-II via pin-connection, which is in turn connected with the Raspberry PI-3 via Bluetooth. The "Voice Control" feature which is included in this project, is also integrated with Raspberry PI-3. In this feature, the input is the microphone and the output is the speaker. The Accelerometer and the gyroscope values (possibly In-car temperature values) are sent by the MPU-6050 sensor via GPIO pin. The Raspberry Pi then sends these values to the Display/GUI which we have developed via the HDMI Port.

## Raspberry Pi

Raspberry Pi is a low-priced computer that is composed of open-source software. It's available in 3 versions (Model A/B/Zero), Several versions have been released over the years that include various upgrades and enhancements.

It has an ARM-Based Processor as its Powerhouse. Newer versions include onboard Bluetooth and WiFi modules, Raspberry pi has several ports such as USB, HDMI/Analog Composite, 15 pin Connectors, Ethernet, GPIO, SD Card.

Raspberry Pi takes advantage of its General Purpose In Out ports to interface with external devices as these pins have a variety of functionalities such as PWM, I2C, SPI, and Serial Control.

## OBD-II

OBD-II(Onboard Diagnostics version - 2). It is a computer system inside a vehicle that keeps track of the vehicle's performance. This will interact with cars ECU(Engine Control Unit). This can

be connected to Raspberry Pi - 3 via Bluetooth and data can be transferred to raspberry Pi3 for processing. OBD-II provides a list of vehicle parameters to monitor, along with how to encode the data for each. The various parameters available are addressed by PID's(Parameter Identification Numbers). A list of PIDs is available which can be used to convert raw OBD-II data into meaningful information.

## Voice Control

The Voice Control feature is something that will help the driver to interact with the car and get the necessary details without even touching the screen, which makes it very convenient. In the proposed Voice Control system, with the help of the google cloud platform, the driver can give a relevant command and the required operations will be performed and the driver will get the result he needed which could be any information about the car or just to perform some task like pick a call or lower windows etc

## ECU
 An Engine Control Unit (ECU) a.k.a ECM is a computer inside a car/vehicle that receives input from a wide range of sensors present in the vehicle. With the help of the data obtained from the sensors, it will perform the necessary actions, this may range from fuel injection to maintaining cabin temperature. The car's performance may vary based upon the engine profiles set by the ECU. Some vehicles may have multiple ECUs whereas some have only one ECU present in them. 