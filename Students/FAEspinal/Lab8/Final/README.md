# Lab 8 Report
Francisco Espinal

## Background
In this lab we constructed a Hybrid Coupler and a Rat Race coupler. A hybrid coupler is a four-port device that equally splits input signals with a 90-degree phase shift.  A Rat Race coupler is also a four-port device; the input gets split and equally distributed into the two exiting ports but the signal has a 180-degree phase shift. Both can also sum signals as well. These devices are widely used to split power signals because the unwanted reflections are sent to the isolated port or canceled at the input.  

## Design
We used a (Z_0=50) ohms reference impedance on a 62mil thick FR4 (e_r=4.1, tan d = 0.01) substrate to support a frequency range of 1 GHz to 5 GHz.  With these design specification we were able to use an online calculator to find the dimensions needed for both devices. And to find the lengths of each line, I use the following equation. 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab3/Equation.png) <br>

## Procedure
This lab only consisted of HFSS simulations. I started by finding all the dimensions needed by using the following equation I was able to get the impedance of the coupler, (Z_0)/(sqrt(2)). Then to find the length I use the equation given in the last section. Once I found all the values I plugged them into HFSS and analyzed the plots. The same procedure was conducted for the rat race coupler but instead of using the last equation I used (sqrt(2)(Z_0)).   

|    |    Impedance (ohms)  | Width (mm) | Length (mm)|
| ----- |:-----:| :-----:|:------:|
|    Feed   | 50 |  3.11 | 16.8|
|    Port 1 to 2 |   35   | 15 |16.5 |
|    Port 4 to 3  |   35   | 15 | 16.5| 


## Results and Discussion
##### Hybrid Coupler
![Mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab8/Final/Hybrid_Coupler_Magnitude_Plot.png) <br>
![Match](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab8/Final/Hybrid_Coupler_Matched_Magnitude_Plot.png) <br>

##### Rat Race
Identify which traces show port matching, power splitting and isolation. 
Comment on the difference of the simulated and the measured results. 

![Mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab8/Final/Rat_Race_Magnitude_Plot.png) <br>
![Match](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab8/Final/Rat_Race_Matching_Magnitude_Plot.png) <br>

## Conclusion
Everything ran as expected.  The devices would be useful when you would want to combine two transmission lines in order for them to share one antenna.  Why did we put matched loads on the ports while measuring the S-parameters?  What modifications did you have to make to the T-line widths/lengths to improve your simulated results?


## Hindsight
N/A

## Reflection
The lab was straightforward, no changes are recommended. 

