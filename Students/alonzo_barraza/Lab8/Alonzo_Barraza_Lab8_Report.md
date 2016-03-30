# Lab 6 Report
Alonzo Barraza 

## Background
Lab 8 was created to take a look at different couplers and see how they work. In this particular lab a Rat-Race coupler and a Hybrid coupler were studied. Each coupler has their own advanteges and disvanteges, along with some similarites. Both coupler designs want to have equal split, matched ports, and isolations depending on a given S parameter.   

## Design
The designs both couplers were made in HFSS beforehand and this lab required to adjest the line widths and lengths. The Hybrid coupler was the first design to be worked with. For this particular design, the four input ports were meant to have a 50 ohm impedance and quarter-wavelength line. The theorectical design had a width of 3.105mm and a length of 16.923mm, which both take into the dielectric constant of the board. The two lines that run perpendicular to the input lines had teh same values. However the lines connceting port 1 to port 2 and port 4 to port 3 had different dimessions. The line impdeance for these two lines were 35.35mm (Z0/sqrt(2) with Z0 = 50 ohms) with the width being equal to 5.248mm and the lenth equalling 16.498mm. This particular hybrid coupler is a 90 degree or a quadrature coupler. 

The second design was a Rat-Race coupler. A Rat-Race or ring-coupler has four ports as well. The lengths from port 1 to port 2 and port 3 are a quarter-wavelength as well as the length from port 3 to port 4. However, the distance from port 4 to port 2 is three-quaters-wavelength. Therefore the circumfrence of the ring is 6-quarters-wavelength. The input lines for each port were 50 ohm line which means the widths and lengths are 3.105mm and 16.923mm respectively. Each section between two ports had impdences of 70.71 ohms (Z0*sqrt(2)) therefore making the widths 1.648mm, the lengths 17.363mm, and circumference 104.178mm. 

## Procedure
Due to the short week, this lab consisted only of the simulation portion.  

## Results and Discussion
![Time Delay Shift: S11 Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab7/TDS_mag_S11.png) <br>
![Time Delay Shift: S21 Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab7/TDS_mag_S21.png) <br>
![Time Delay Shift: S11 Pahse](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab7/TDS_phase_S11.png) <br>
![Time Delay Shift: S21 Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab7/TDS_phase_S21.png) <br>
![Wilkinson Power Divider Magnitude: S11, S22, S33](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab7/WPD_mag_S11.png) <br>
![Wilkinson Power Divider Magnitude: S21, S31, S32](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab7/WPD_mag_S21.png)<br>
![Wilkinson Power Divider Phase: S11, S22, S33](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab7/WPD_phase_S11.png)<br>
![Wilkinson Power Divider Phase: S21, S31, S32](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab7/WPD_phase_S21.png)<br>

## Conclusion
The measurement portion of this lab was done by David and he provided the results in order to compare them with the HFSS results. For the most part the simulations and the fabracated designs produced the same results. As of right now the simulated ones have a phase shift but that can be corrected by adjusting the values.  

## Hindsight
This lab was simple and easy to go through.

## Reflection
As usual the difficult part is the fine tuning of the designs but after working with several designs it is becoming easier to know how to make adjustments. These lab do a great job of making us understand how these devices work and how to implement them. 
