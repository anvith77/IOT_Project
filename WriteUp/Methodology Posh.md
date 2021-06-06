
## Pygame 
Pygame is a set of Python modules designed mainly intended for the development of video games. It is very versatile as it can run on any platform and operating system, adding to this it's also open source. Pygame's Core is relatively simple. The core functions use C and Assembly code which makes it faster and lighter to run. This allows us to run pygame even on low spec devices such as Raspberry Pi 2/3/Zero. Pygame takes advantage of CPUs with multiple cores/higher core count,  due which it may run even faster on the newer editions such as the Raspberry Pi 4. 
The functionality of the SDL (Simple DirectMedia Layer) library is enhanced with Pygame.
Pygame is modular and also allows us to have more control when using other libraries. Moreover, it lets you process images, receive inputs from a controller/joystick, and play audio files. Pygame has a strong community of developers who regularly update and fix bugs.  

![[1.png]]

## Communication b/w Raspberry Pi and OBD:
As all cars and light trucks built during 1996 and after were required to be OBD-II equipped. The OBD port of the car/vehicle can be accessed by using an OBD-II system/adapter, which is Widely available as USB/Bluetooth Versions. However, some systems/adapters have the provision of WiFi too. The connection, in this case, is established between the Raspberry Pi and OBD-II system over Bluetooth. As we have a Raspberry Pi 3 Model B+, it has an onboard Bluetooth module of version 4.2. 
When an OBD Bluetooth adapter is connected to the port, a light present on the adapter instantly illuminates. As long as the adapter is plugged in, It will be active and powered on, as the port has an 'always on' 12-volt output. The setup between Raspberry Pi and the OBD Adapter is done as to it scanning for the OBD adapter, after the adapter has been found it needs to be paired. For the OBD port is a serial port, it needs to be bound to a serial port on the Raspberry Pi. The MAC address of the OBD adapter is used for this port assignment. Through several commands available we can access the required parameters of the vehicle as wells as clear fault codes in the vehicle.  

![[GUI Block diagram.png]]

## GUI Code and Structure 
GUI Code Breakdown:	
As it was essential to develop a personalized GUI to accommodate all the necessary parameters, Pygame along with obd and DateTime libraries were used. The IDEs that were of our preference were IntelliJ Idea, Pycharm IDE.  The breakdown of the code is as follows
A full-screen window for GUI is created using a built-in function `pygame.display.setmode((0,0), pygame.FULLSCREEN)`.
 `"obd.Async(fast=False)`  statement is used, here `Async` is a subclass of obd, and this particular loop will keep the values of parameters updated with respect to the vehicle. 
 `connection.watch(obd.command."OBD commands" , callback = "Function defined for each parameter")`
 Update loop for the OBD Command of the parameter must be initialized with a `start( )` and contain a  `stop( )`. To update the OBD Command we use `watch( )`
The Colors, Font name, and Font size used to display the parameters collected from OBD-II are declared. All the parameter variables are declared as global variables. To get the values of the parameters, each parameter is given its dedicated function. Here the parameters that were taken were Speed, RPM, Load, Intake Temperature, Barometric Pressure, Coolant Temperature, Run time. Furthermore, PIDs can be added similarly if needed. Apart from these,  details like the time, day and date are also provided.

```python 
Psudo code: 
def get_parameter( variable):
	global parameter 
	if not variable.is_null( ):
		parameter = int(variable.value.magnitude)

```

`def hud( ):`  This function is used to draw the Window with parameter Names. This function includes all the parameter names,
Fonts for those and their position on the window.

`def rpmdbar( ):` This function is used to display a dynamic RPM bar i.e RPM bar will increase or decrease depending on the value of the rpm. It also includes colors to indicate the range of RPM. i.e Green if RPM is low, Orange if RPM is moderate and
Red if the RPM is high. The ranges are set according to ideal gear shift values for low-end cars to mid-segment cars, as they typically have their red line set at 6000 (Diesel) - 8000 RPM (Petrol)  

`def coolanttemp(coolanttemp)`: This function is used to change the color of the coolant temperature parameter displayed, based on the value of the coolant temperature obtained from OBD -II. The main purpose of this function is to warn the driver if the car engine gets too hot, as this may lead to engine seizure or overheating. 

`def main()`:  This is the main function that writes the values of all the parameters on the window and updates them when they change. This function also defines the font name and font size for each parameter.
This function is an infinite loop, which also calls the above functions, exiting this loop is possible through a press of a button. 

![[bandicam 2021-06-03 18-38-52-277.jpg]]



# GUI Layout and Setup 
This GUI contains all the important parameters that the user would need to know while the driving the vehicle. 
The paramters that are shown in the GUI are: 
1.Speed: As knowing the speed of the vehicle is of utmost priority ,it is being displayed in a larger font size at the center of the GUI.  
2. RPM and RPM bar: This parameter displays the engine RPM(Revolutions per minute) and the bar is designed in such a way that it changes its color depending the engine RPM, for instance if the RPM is low, bar will show the color green, yellow at moderate rpm and red at high rpm. As this is being implemented in low- medium segment cars, the engines are usually not very powerful and on average both diesel and petrol engines have their red line at 6000 RPM. 
3. Engine Load : Power produced by the engine is determined by Engine load. It is a force which resists the engine power. Whenever the engine speed increases,Engine load decreases.
4. Cabin temperature: It displays the temperature inside the cabin.It is implemented using MPU6050 sensor.
5.Real-time Clock : It is displayed at the top left corner of the GUI and it helps the user to know the day,date and time without looking at any other gadgets.
6. Run Time - This parameter indicates how long the engine has been running since its started.
7.Barometer- This parameter displays the atmospheric pressure.It is measured in KiloPascal(kpa)
8.Coolant temperature : This shows the temperature at which the coolant is being stored.It is measured in degree Celsius.
9.Intake Temperature : This displays the temperature of the air entering the engine. It is measured in degree Celsius.

As the convenience of the driver is of utmost priority, the GUI is designed having a black background so that the reflection wont be projected on the windshield

The display of choice for this application is a TFT Display as it has fairly high contrast, due to which the contents are readable independent of the lighting condition. It is also much sharper,brighter and has a faster refresh rate compared to a regular LCD Display. 
Raspberry Pi offers 2 ways of connecting displays, either through HDMI or DSI (Display Serial Interface). 


```
The display in this case, is connected through HDMI from Raspberry Pi an old phone with a TFT Display with the help of OTG and HDMI to USB 3.0 Video capture Card 
```

The contents are then projected onto a glass, although sunlight readability can be a problem, this can be reduced with the help of a Windshield Combiner Film.  When this film is used with the glass 


### 3M™ Windshield Combiner Film (3M WCF)

In place of the standard PVB wedge, 3M WCF forms a seamless flat layer between layers of windshield glass. It virtually eliminates secondary images. It opens up the entire windshield as a canvas for HUD displays.

The film also uses p-polarized light. When the film is used in the windshield and the HUD picture generating unit (PGU) is configured to project P-Pol light, vehicle occupants no longer need to remove standard S-Pol-blocking sunglasses to read HUD information. That’s great news for designers concerned about safety in HUD design.



![[2.png]]
![[voice control diagram.png]]


## Voice Control Code Overview 
To accomplish the task of voice control, certain python libraries were used such as speech recognition. This class has many functions out of which, a class called `Recognizer( )` is used. 
For the Recognizer function to work well, there are several APIs available, out of which `google_recognizer` was chosen as it's free and doesn't require an API Key to use it, and also works with a variety of languages.
The PyAudio library is essential as it can be used to receive audio input which is taken through a USB microphone in this case and provide audio output through a speaker, which is connected via a 3.5mm audio jack present on the Pi. To taken in real-time speech data the Microphone class is used. Pyttsx3 is a library that is used for text-to-speech conversion. It works offline, offers voices in both `female` and `male`. The `pyttsx3.init( )` function is a factory function used to get a reference to pyttsx3. 
 The above-mentioned python's speech recognition and pyaudio are set up in a custom function called `def command( ):`.  In addition to this, we require a trigger word, in this case, it's set as "My car" so that the voice control program works only when we need it to. Further, there exists a custom function called `def talk( ):` which uses pyttsx3 for voice feedback.
 For the functionalities of our voice control system a function called `def my_car( )` was created. Several subfunctions have been made with the help of other python libraries to allow the driver to request music, web search, weather, and more.  For each parameter related to the car, a function has been made to inform the driver, where it queries the car for the parameter value in real-time and provides voice feedback to the driver.  
```python 
Pseudo Function:
	if 'parameter' in command:
		connection = obd.OBD()
	 	r = connection.query(obd.commands.PARAMETER)
	 	print(r)
	 	talk(str(r))
```
The proposed system also has a speed limit feature that would alert the driver when they would exceed a certain speed limit.

![[MPU6050 with Raspberry pi.png]]

## MPU6050 

MPU6050 SENSOR:
MPU6050 Module consists of 3-axis Accelerometer, 3-axis Gyroscope, and an in-built Temperature sensor. It consists of 8 pins. The following details about the pins are given below:
1.Vcc: Provides power for the module, which can range from +3.3V to +5V. Preferably +5V is used.
2.Ground: Connected to the Ground of the system.
3.Serial Clock (SCL): It uses I2C serial communication protocol and it's responsible for the clock pulse 
4.Serial Data (SDA): It uses I2C serial communication protocol and is used for data transfer 
5.Auxiliary Serial Data (XDA): This is used to transfer data between other I2C modules that are connected with MPU6050  
6.Auxiliary Serial Clock (XCL): This is used to synchronize the clock between other I2C modules interfaced with MPU6050
7.AD0:  This pin can be used to vary the address if more than a single MPU6050 module is used
8.Interrupt (INT): Interrupt pin notifies that the data is available for the MCU module to read.

WORKING OF MPU6050:
MPU6050 Module requires a minimum input of 3.3 Volts and a Voltage Regulator. It uses two 4.7k resistors, where one resistor is used to pull up the I2C lines and another resistor is used to pull down the interrupt pin. The data from the MPU6050 can be read through the I2C bus. Whenever there is a change in motion, it will be reflected in its mechanical system which in turn varies the voltage.  The I2C consists of a 16-bit ADC which it uses to accurately read these changes in voltage after which it stores them in the FIFO buffer and this causes the INT (interrupt) pin to go high which means, the data is now ready to read. We have an MCU (Micro-Controller Unit) to read the data from the FIFO buffer through IIC Communication.

![[eq_mpu.png]]

INTERFACING OF MPU6050:
 This module is interfaced with Raspberry Pi using Python and C language. 
The pin-connections to interface MPU6050 with Raspberry Pi to get the values of Accelerometer and Gyroscope is mentioned below:

•	Pin 4 (5V Pin ) of the Raspberry Pi, which is 5V is connected to the VCC of MPU6050.
•	Pin34 (GND Pin) is connected to the GND of the sensor.
•	Pin3 (I2C1 SDA) is connected to the SDA of MPU6050.
•	Pin5 (SCL) of Raspberry Pi is connected to SCL of MPU6050

Once the pin-connections are made the values of both the gyroscope and accelerometer are obtained and printed on the Raspberry Pi's console. As we need acceleration we place these values into the below function 

```python 

def calculate_Acceleration():
  #Read the accelerometer,gyroscope values
	ACC_SENSITIVITY = 0.732/1000
	#according to data sheet for linear acceleration +/- 16g range	
	Ax = Ax * ACC_SENSITIVITY      
	#multiply raw reading by sensitvity to obtain acc in g's
  	Ay = Ay * ACC_SENSITIVITY
  	Az = Az * ACC_SENSITIVITY

  	#Normalize x and y vectors to compensate for gravity
  	thetaX = math.atan(Ax/math.sqrt(Ay**2+Az**2))
  	thetaY = math.atan(Ay/math.sqrt(Ax**2+Az**2))
  
  	AxComp = Ax * math.cos(thetaX)
  	AyComp = Ay * math.cos(thetaY)

  	acceleration = math.sqrt(AxComp**2 + AyComp**2) * 9.807

  	return acceleration

```



