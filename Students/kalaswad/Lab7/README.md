# Lab 7 Report
Matias Kalaswad

## Background
In this lab we worked with different types of power dividers. The following four types were simulated using Z0lver as part of a homework assignment: delta power divider, splitter, four-way splitter, and Wilkinson power divider. The basic function of power dividers is to split and input signal into two or more identical output signals.

## Design
The 90 degree phase shifter required 1/8th wavelength T-lines at each side of the thru length. We calculated a quarter wavelength which at 3 GHz is 14.06 mm, so the 1/8th wavelength is 7.03 mm long. The 180 degree phase shifter required a half wavelength overall so we added a quarter wavelength (14.06 mm) to both ends of the thru. Both designs had an impedance of 50 ohms which corresponds to a copper strip of length 3.1 mm.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab7/Lab7WilkinsonPowerDividerHFSS.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab7/Lab7WilkinsonPowerDividerParameters.png)

## Procedure
In lab we built a time delay shifter out of copper tape. This shifter had a 90 degree shift and a 180 degree shift, both of which required separate designs. There was a 50 ohm line with length similar to previous labs. The first delay path we made was for the 90 degree phase shift. There was a small separation between the 50 ohm line and the path legs so we had to solder across the gap to connect the path legs. The second delay path was created in a similar manner but with lengths to create a 180 degree shift. This time the path legs were calculated to be 23.98 mm. Once the 90 degree path was removed and the 180 degree path soldered onto the 50 ohm line, David once again measured the phase shift. He had warned us ahead of time that the result would not be correct because there was a discontinuity when the shift was this high. The analyzer measured the phase to be -233.9 degrees which David told us to subtract 360 degrees from. The result was 593.9 degrees which from our reference phase was a shift of about 164 degrees instead of 180.

## Results and Discussion
The resistor is necessary in the power divider to dissipate half of the input power. We could not see any major differences between THRU and THRU2. If we had time to make a new phase shifter we would have wanted to re-cut our copper strips to make them more accurate widths.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab7/Wilkinson_Magnitude2.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab7/Phase_Shifter_S11.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab7/Phase_Shifter_S21.png)

## Conclusion
The main point of this lab was to learn about the design of different power dividers and to practice constructing phase shifters.  While there were some errors due to the poor connections with the copper tape, our measurements were fairly accurate.  Our desired value for the 180 degree shift should have been closer to 609 degrees and we believe that if we had done this shift first it would have been more accurate.  Since we had to remove and re-solder on the 50 ohm line, the second shifter was less accurate due to poor connection.

## Hindsight
David warned us about the 180 degree shifter not work properlying and this saved us from having to remake our design. The z0lver assignments were helpful in understanding some of the concepts for this lab.

## Reflection
This lab was a good continuation from the previous lab and somewhat solidified my understanding of what we were learning in class. The novelty of cutting copper tape and soldering quickly wore off.
