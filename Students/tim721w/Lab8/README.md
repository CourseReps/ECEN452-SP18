#Lab 8 Report

Chung-Huan Huang

## Background
In this lab, Hybrid couple and Rat Race coupler were designed and compared with simulation results. The design is based on following figure and operating frequency is set to be 2.5 GHz.<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/Hybrid_coupler.png) <br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/rat_race_coupler.png) <br>

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
Simply key in above calculated parameters into HFSS file and simulate at certain frequency range. Simulated model is shown below:<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/model_1.png) <br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/model_2.png) <br>

<br>S parameters are shown below:<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/Hybrid_dB.png) <br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/Phase_diff.png) <br>
It can be seen that power splits equally to port 2 and port 3 from S21 and S31 (about 3 dB at 2.5GHz). Port 4 is regarded as isolated with port 1 from S41(about 25dB at 2.5GHz).
<br>

<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/RatRace_dB.png) <br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab8/RatRace_phase_diff.png) <br>
It can be seen that power splits equally to port 2 and port 3 from S21 and S31 (about 3 dB at 2.5GHz). Port 4 is regarded as isolated with port 1 from S41(about 40dB at 2.5GHz).
<br>

## Discussion
The results of measurement data and simulated data are similiar. However, there may be some curves are not match very well. This may due to that connectors may not be will implemented and microstrip line may not be fabricated as precise as simulated model.<br>

<br>Q1: Widths and lengths of T-Line are calculated based on the structures of coupler shown above. The calculations are done through microstrip online calculator. (http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm)
<br>
<br>Q2: Hybrid coupler is useful for 90 degree phase shifted power divider. Ratrace coupler is useful for 180 degree phase shifted power divider or combiner.
<br>
<br>Q3: To put matched loads when measuring S parameters is to reduce reflection from ports.
<br>


## Conclusion
Only simulations are conducted for both Hybrid coupler and Rat Race coupler. The hardware measurements were done by David. The results for both simulated and measurements show out the curve correspondence.<br>

## Hindsight
None<br>

## Reflection
It would be better for us to measure S-parameters with VNA. 