# Lab 8 Report
Francisco Espinal

## Background
In this lab we constructed a Hybrid Coupler and a Rat Race coupler. A hybrid coupler is a four-port device that equally splits input signals with a 90-degree phase shift.  A Rat Race coupler is also a four-port device; the input gets split and equally distributed into the two exiting ports but the signal has a 180-degree phase shift. Both can also sum signals as well. These devices are widely used to split power signals because the reflections are sent to the isolated port or canceled at the input.  

## Design
We used a (Z_0=50) ohms reference impedance on a 62mil thick FR4 (e_r=4.1, tan d = 0.01) substrate to support a frequency range of 1 GHz to 5 GHz.  With these design specification we were able to use an online calculator to find the dimensions needed for both devices. And to find the lengths of each line, I use the following equation. 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab3/Equation.png) <br>

## Procedure
This lab only consisted of HFSS simulations. I started by finding the impedances of the coupler needed by using the following equation, Z_0/ sqrt(2). Then to find the length I use the equation given in the last section. Once I found all the values I plugged them into HFSS and analyzed the plots. The same procedure was conducted for the rat race coupler but instead of using the previous equation to get the impedances, I used sqrt(2)(Z_0).     

Hybrid Coupler 

|    |    Impedance (ohms)  | Width (mm) | Length (mm)|
| ----- |:-----:| :-----:|:------:|
|    Feed   | 50 |  3.11 | 16.8|
|    Port 1 to 2 |   35   | 15 |16.5 |
|    Port 4 to 3  |   35   | 15 | 16.5| 

Rat Race Coupler 

|    |  Impedance (ohms)  | Width (mm) | Length (mm)|
| ----- |:-----:| :-----:|:------:|
|    Half Circle   | 70.1|  1.6 | 100 |
|   The rest |   50  | 3.12 | 16.8 |


## Results and Discussion
##### Hybrid Coupler
![Mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab8/Final/Hybrid_Coupler_Magnitude_Plot.png) <br>
S11 shows the power reflected. S41 shows the isolation. S21 and S31 show the split in power. 

![Match](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab8/Final/Hybrid_Coupler_Matched_Magnitude_Plot.png) <br>

![Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab8/Final/Lab_8_Hybrid_Phase_Difference.png) <br>

My HFSS design did not quite align with the Milled data. My design matched closer to 3GHz than the desired 2.5GHz, other than that everything else was flawless. There was good isolation, and an acceptable split in power. Then the phase based of the graph was around 90 as expected.  

##### Rat Race

![Mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab8/Final/Rat_Race_Magnitude_Plot.png) <br>
S11 shows the power reflected. S41 shows the isolation. S21 and S31 show the split in power. 

![Match](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab8/Final/Rat_Race_Matching_Magnitude_Plot.png) <br>

My rat race coupler operated, as it should’ve. Everything was identical to the milled data. 

## Conclusion
Everything ran as expected. No modifications were done to improve the simulation, but modifications should’ve been done in order to get the desired behavior. A situation where the devices would be useful is when you would want to combine two transmission lines, in order for them to share one antenna.  Then we matched the loads on the ports because we could only measure two ports at a time. 


## Hindsight
N/A

## Reflection
The lab was straightforward, no changes are recommended. 

