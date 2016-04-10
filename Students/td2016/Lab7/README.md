# Lab 7 Report
Thomas Darden

## Background
For this lab, we will design and simulate a Wilkinson Power Divider. We will also construct a phase shifter. The WPD will be designed with a center frequency of 2.5GHz and a feed impedance of 50 ohms. It will be placed on a 62mil FR4 substrate. The phase shifter will have the same design parameters as the WPD but will be designed for a frequency of 3GHz and will implement a 90 degree phase shift as well as a 180 degree phase shift.

## Design
The design for the WPD is as follows:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab7/Wilkinson-coupler.png)<br>
We must design as power divider for a 50ohm feed line, so this means that the circular lines going from port 1 to ports 2 and 3 must have an impedance of 50*sqrt(2) = 70.7107ohm. Knowing the resistances, we must determine the widths of the lines as well as the length of the line. Using the online microstrip calculator, we find:

For the 50ohm lines:

width = 3.128mm

For 70.7ohms:

width = 1.675mm

effective_wavelength/4 = 17.3mm

We also find that the value of the resistor between ports 2 and 3 must be 50*2 = 100ohms.

We then simulate the design in HFSS.

For the design of the phase shifter we built in lab, we first determined the length of a 50ohm line at 3GHz. We found that the width of the line must be 3.12mm. For a 90 degree phase shift, we must add a length of (effective wavelength)/4 to the line. To do this we measure a 35mm section of the line (after we measure the line with a network analyzer) and cut it off. We then add another 35mm line with stubs 7.02mm long attached to both ends. This means we added an eigth of a wavelength to both ends to add a distance of (effective wavelength)/4 to the line. We measure this with a network analyzer, and then cut the added piece off. We repeat the last procedure again, but not we cut a 35mm line with 14.036mm stubs attached to the end. This will add (effective wavelength)/2 to the line to give the signal a 180 degree phase shift.

##Procedure
First simulate the WPD design in HFSS.

Implement the phase shifter description mentioned in the Design section and measure the results.

## Results and Discussion
From the simulation of the WPD and the data of the milled WPD, we get the following graphs:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab7/Milled_WPD_Phase.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab7/Milled_WPD_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab7/Correct_S_Phase.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab7/Correct_Milled_Phase.png)<br>
From the above graphs it is clear to see that the simulated and milled design of the WPD work and have the relatively same result. Ports 2 and 3 get the same amount of power from port 1 and have low interation with each other and minimal reflection. It is interesting to note the the milled WPD has a better response in the lower frequencies than the simulated model does, but the opposite is true for the higher frequencies. 

For the phase shifter that we constructed in lab, our results are detailed below:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab7/Phase_Shifter_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab7/Phase_Shifter_Phase.png)<br>
From the above graphs, we can see that reflection is minimize and that we have low insertion loss within the divider in the three configuration. However, the phase difference in the shifter is not as great as it needs to be for the two phase shifter configurations we have. At 3GHz, our phases for the three configurations are:

Reference: phi = -437 degrees

90 Degree Shift: phi = -531 degrees

180 Degree Shift: phi = -570 degrees

From this data, we can see that our 90 degree phase shifter worked relatively well, with a 94 degree shift in signal. The 180 degree shifter, however, only gave the signal a 139 degree shift. This means that it missed the phase shift by 41 degrees.

We can calculate how off our shifters were by finding the percentage off our shifters were and multiplying that percentage by the effective wavelength of the signal. 

For the 90 degree shifter, we were off by 4 degrees.

(4/360)(56.146mm) = .624mm

For the 180 degree shifter, we were off by 41 degrees.

(41/360)(56.146mm) = 6.39mm

So for our constructed shifters, the 90 degree shifter was .624mm too long and the 180 degree shifter was 6.39mm too short.

## Conclusion
From this lab, I was able to implement a WPD and see how a ciruit can divide the power evenly to two ports in a curved design to avoid coupling. I was also able to see how hard it is to build an accurate phase shifter, as even a small difference in construction can make a huge difference. I probably messed up on the measurements whenever I was cutting the copper tape for the 180 degree shifter. I also was not able to put the shifters down evenly on the substrate so the design was a little rippled, which could have caused error.

## Hindsight
Now knowing how hard it is to build an accurate phase shifter, I wish we would have had more precise scissors to cut the tap with as the ones we had in lab were bulky and our tape needed to be precise to less than a millimeter to be correct.

## Reflection
Overall, this lab was informative but a little frustrating. It was hard having to cut the phase shifters accurately with such bulky scissors but the lab was straight forward in what needed to be completed. 
