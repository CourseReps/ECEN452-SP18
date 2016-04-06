#Lab 8 Report

Zhong Chen

## Background

In this lab,I will complete two designs of a Hybrid coupler and the design of Rat-Race coupler. I will be designing these two designs for a Z0=50 Ohms reference impedance on the 62 mil thick FR4 substrate.<br>
Hybrid Coupler Model:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab8/Hybrid_Coupler.jpg) <br>

Rat-Race Coupler Model:<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab8/Rat_Race_Coupler.PNG) <br>

## Design

Use Microstrip online calculator, parameters can be easily calculated based on above figure and given substrate information (FR4). 
Parameters of Hybrid coupler are set up as:
Feed line width: 3.1298828125 mm
Coupler_x_width: 3.1298828125 mm
Coupler_y_width: 5.28125 mm
Coupler_x_length: 16.880172629099 mm 
Coupler_y_length: 16.470546778345 mm <br>

However,the center frequency is a little shifted,below is the first simulation result:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab8/First_Simulation.png) <br>

Modify the Coupler_x_length: 18.5 mm. <br> 

Parameters of Rat Race coupler are set up as:
Feed line width (50 ohm): 3.1298828125
Rat race line width (70.71 ohm): 1.6767578125 mm
Rat race circumference: 6/4 lambda : 17.295580370995644*6=103.7734822 mm


## Results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab8/Hybrid_matching.png) <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab8/Input_Port1.png) <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab8/Rat_Race_matching.png) <br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab8/Rat_Race_Input_Port1.png) <br>


## Conclusion
The results of measurement data and simulated data are similiar. However, there may be some results are not matched very well. This problem may be coming from that the microstrip line may not be fabricated as precise as simulated model.

## Reflection
No.



