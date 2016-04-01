#Lab 8 Report

Chung-Huan Huang

## Background
In this lab, Hybrid couple and Rat Race coupler were designed and compared with simulation results. The design is based on following figure and operating frequency is set to be 2.5 GHz.<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/Hybrid_coupler.PNG) <br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/rat_race_coupler.PNG) <br>

## Design
Using Microstrip online calculator, parameters can be easily calculated based on above figure and given substrate information (FR4). <br>
Parameters of Hybrid coupler are setup as:<br>
Feed line width: 3.1298828125 mm<br>
Coupler_x_width: 3.1298828125 mm<br>
Coupler_y_width: 5.28125 mm<br>
Coupler_x_length: 16.880172629099 mm <br>
Coupler_y_length: 16.470546778345 mm<br>

<br>Parameters of Rat Race coupler are setup as:<br>
Feed line width (50 ohm): 3.1298828125<br>
Rat race line width (70.71 ohm): 1.6767578125 mm<br>
Rat race circumference: 6/4 lambda : 17.295580370995644*6=103.7734822 mm<br>

##Procedure and Results
Simply key in above calculated parameters into HFSS file and simulate at certain frequency range. Simulated model is shown below.<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/model_1.PNG) <br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/model_2.PNG) <br>

<br>S parameters are shown below:<br>

## Discussion
The results of measurement data and simulated data are similiar. However, there may be some curves are not match very well. This may due to that connectors may not be will implemented and microstrip line may not be fabricated as precise as simulated model.<br>

## Conclusion
Only simulation are conducted for both Hybrid coupler and Rat Race coupler. The hardware measurement was done by David. The results for both simulated and measurements show out the curve correspondence.<br>

## Hindsight
None<br>

## Reflection
If possible, it¡¦s better to have a lab instruction document. That would make me more clearly to understand what to do for the lab. Also, it¡¦s much easier to understand design process if we can do the hardware experiment.<br>