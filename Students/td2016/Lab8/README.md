# Lab 8 Report
Thomas Darden

## Background
For this lab we will be designing a hybrid coupler and a rat race coupler. We will only be simulating these designs in HFSS but we will compare our results with the results of the milled couplers. As always, our couplers will be designed with a center frequency of 2.5GHz on a 62mil FR4 board with 50ohm feed lines. 

## Design
The first coupler we will design is the hybrid coupler. This design can be illustrated in the following diagram:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/HybridCoupler.png)<br>
Since our feed lines are 50ohms, our Zo is going to be 50ohms. This means that 50/sqrt(2)=35.355mm. Knowing these impedances, along with our other design parameters, allows us to calculate the widths of lines as well as the effective quarter wavelengths.

For the 50ohm lines:

width = 3.1279mm

Length = 16.883mm

For the 35.4ohm lines:

width = 5.272mm

Length = 16.472mm

Using these values, we can simulate our designs in HFSS.

Now we must design the rat race coupler. This design can be illustrated in the following diagram:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/RatRaceCoupler.png)<br>
Since our feed lines are 50ohms, the widths and quarter wavelengths are the same as above. However, for effective power splitting, our must design our circle to have the impedance of 50*sqrt(2)=70.7107. This gives us the width of 1.675mm and a quarter wavelength of 17.3mm. Knowing these design parameters, we can simulate the design in HFSS.

## Procedure
For the couplers, simulate in HFSS.

## Results and Discussion
For the hybrid coupler, we found that the design was functioning correctly but at a higher frequency. This meant that our design was too short. I am unsure whether or not this was due to the way the HFSS file was set up, but the way I fixed this issue was adding half of the widths of the opposite lines to the lengths of the lines.

This give the 50ohm lines: L = 16.883 + 5.272/2 = 19.519mm

35.355mm lines: L = 16.472 + 3.1279/2 = 18.036mm

When the lines have the above values the design functions as it should. This correct design gives us the following graphs:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Hybrid_Sim_S21_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Hybrid_Sim_S21_Phase.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Hybrid_Sim_Matched_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Hybrid_Sim_Matched_Phase.png)<br>

The milled design of the hybrid coupler gives us the following graphs:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Hybrid_Mil_S21_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Hybrid_Mil_S21_Phase.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Hybrid_Mil_Matched_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Hybrid_Mil_Matched_Phase.png)<br>

From these graphs, we see that our designed coupler works the same as the milled coupler. Port 2 and 3 recieve the same amount of power at our design frequency while port 4 is isolated and port 1 has minimal reflection. 
We also see from the phase graphs that port 3 has a 90 degree phase shift from port 2. This can be further illustrated by the following graph:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/PhaseDifference.png)<br>

From the rat race coupler, we were able to simulated the designs in HFSS. The results are detailed in the following graphs:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Rat_Sim_S21_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Rat_Sim_S21_Phase.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Rat_Sim_Match_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Rat_Sim_Match_Phase.png)<br>

From the milled rat race coupler, we got the following graphs:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Rat_Mil_S21_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Rat_Mil_S21_Phase.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Rat_Mil_Match_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab8/Rat_Mil_Match_Phase.png)<br>
From these graphs we are able to see that our designed coupler works the same as the milled coupler. When port 2 is excited, port 3 is isolated and ports 1 and 4 recieve equal power. 

## Conclusion
From this lab, I was able to design 2 versions of a 4 port power splitter, with one port isolated. The hybrid coupler has a 90 degree phase shift between the 2 ports while the rate race coupler allows the 2 ports to have the same phase shift. I'm not sure if the additional lengths I had to add to the hybrid coupler were actually required for the design or if it was a problem with the HFSS file.

## Hindsight
I wish I knew more about HFSS to determine how to look more accurately at the phase graphs and how the designs are actually put together. 

## Reflections
Overall, the design process of the couplers was very straigt-forward in terms of applying the knowledge learned in class. I think it would be beneficial to have the parameters of the milled couplers known in order to see if there is a problem with the design file.
