## Reference Papers 
[[Motorcycle Head-Up Display.pdf]]
[[The Future of Holographic HUD.pdf]]
[[Automotive Displays from Direct View to AR Head-Up 1.pdf]]
[[Advantage of Head-Up Display for Automobiles.pdf]]
[[A prototype of low cost heads up display for automobiles navigation system.pdf]]

[Plague Scam website check](https://www.editpad.org/tool/plagiarism-checker)

[Scam check list](https://www.whatisresearch.com/best-plagiarism-checker-for-research-papers-free/)

![](https://projects-raspberry.com/wp-content/uploads/2018/07/calculate-tilt-compensated-acceleration-value-in-the-x-y-plane..jpg)


#todo 
- [  ] obd sensor values - RAW values 
- [x] OBD values on GUI 
- [ ]  OBD Sensor Values RAW 
- [x]  MPU Raw Values 
- [ ]  MPU GUI
- [ ]  References - in order  
- [ ]  ONLINE [ ' Link goes here ' ]
- [ ] Voice Control Terminal Values 
- [ ] FInd out processing time. latency of each code 
- [ ]   


## Introduction 
1. Block Diagram of project - Everything about each block + explanation - Overall Overview 
2. Features of Raspberry Pi 3 for HUD along with OBD-II 
3. Voice control -> software -> method of implementation with hardware  
		ONE PAGE LIMIT 
	
COnvert block diagrams to JPEG. 
![[HUD .png]]

## Title:
1. Heads Up Display with Voice Control for Low Spec Automobiles 
2. Head's Up Display with Voice Assistant and Feedback 
3. Head's Up DIsplay for Older Automobiles 

## Abstract: 
Head's Up Display (HUD) is often an important safety feature that's usually left out in Low to Mid segment cars. A Head's up Display supplements a drivers Field of View by providing essential and necessary information like Speed,Rpm,Navigation etc, so it essentially reduces distraction and increases concentration during the drive, thereby reducing the chances of an accident/loss of life.  Ripped off the internet 
According to the World Health Organisation (WHO), road crashes kill 1.2 million people and permanently disable another 50 million every year. Over the past decade, road crash has become the 10th leading cause of death in the world, and is prected to rise to the fifth position by 2030. 
[Source](https://www.autocarpro.in/news-national/india-distracted-driving-study-reveals-adverse-impact-mobile-phones-road-safety-24507)
share of luxury cars in the overall market, in fact, has come down from 1.2% in 2019 to about 0.9% now  
 Read more at:  
[Luxury Cars Percent India](https://economictimes.indiatimes.com/industry/auto/auto-news/indian-luxury-car-market-set-to-register-a-record-40-decline-in-2020/articleshow/78004931.cms?utm_source=contentofinterest&utm_medium=text&utm_campaign=cppst)	Eight percent of fatal crashes, 15 percent of injury crashes, and 14 percent of all police-reported motor vehicle traffic crashes in 2018 were reported as distraction-affected crashes. ■ In 2018 there were 2,841 people killed and an estimated additional 400,000 people injured in motor vehicle crashes involving distracted drivers.

[Source-pdf](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/812926)
[Source-website](https://www.cdc.gov/transportationsafety/distracted_driving/index.html)

#### Points to highlight/Mention :
1. Accidents rate and Fatalities 
2. Accidents due to distractions 
3. Mid + Low segment cars >> Luxury Cars (Quantity)
4. Head's up display - Purpose 
5.  Cannot eliminate accidents but reduce/bring fatality numbers down

## Conclusion 
Voice Assistant and Feedback allows the driver to stay more alert while on the drive, as most cars in the lower and mid segment lack these features/functionalities. Adding to this a Head's up Display considerably reduces distractions, making it much more safer and comfortable for the driver. 

## GUI Layout
The GUI shown is designed using Pygame. This aims to display all the necessary information which the driver would need to know while the user/driver is driving the vehicle. In the GUI proposed, we have displayed 1) "speed", which is displayed in bigger font size in the center of the GUI  2) a Real-time clock that would help the driver note the time 
3) RPM  & RPM Bar - which displays the rpm and the rpm bar which changes its color from green, yellow to red for low medium and high rpm respectively. 
''' As this is being implemented in low- medium segment cars, the engines are usually not very powerful and on average both diesel and petrol engines have their red line at 6000 RPM. '''
4) Cabin temperature- which shows the temperature of the cabin 5) coolant temp 6)intake temperature 7) Run Time - which tells how long the engine has been running since it started. 8) Barometer- which displays the pressure outside. ( to be added)(advantage)
9)Load- which displays the engine load. These are the important information displayed. We have chosen a black background for the GUI reason being that it doesn't get reflected when we project onto the windshield, hence making it convenient for the driver.
In order to output the obtained information to the driver, we built a touchscreen capable HUD using the pygame module to display a few pre-selected vehicle information onto the TFT screen.


