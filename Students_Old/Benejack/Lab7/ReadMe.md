# Lab 7 Report
Benjamin Jack

## Background
A phase shifter can be useful for a number of applications such as directing antennas and radiation. All a phase
shifter does is change the phase of the output from the input by some controlled amount and with some small amount
of loss. The Wilkinson power divider is used to divide power from one input port to two output ports. Typically
it is a one directional device and one port is always used for the input. The power can be split unevenly, although
this makes the device more complicated to design.

## Design
*Task1:<br>
Data:
Zo = 50 ohms, 62 mil thick = 1.578mm, FR4 (Er = 4.1), f=3 GHz, w = 3.1mm line

For the phase shifter, we took a 50 ohm section of line with two connectors and then we calculated the wavelength
of the signal at 3GHz using the online microstrip calculator. We know that a half wavelength gives us a 180 degree
phase shift and a quarter wavelength gives us a 90 degree phase shift. Because we are inserting a parallel section
of transmission line with equivalently two stubs, we said the 180 degree shifter had two quarter wavelength stubs
and the 90 degree phase shifter had two eighth wavelength stubs which we measured as 14.07mm and 7.03mm respectively.
We had to significantly modify this design as our stubs were too short and I am not entirely sure why, even now. I think
the biggest problem is how we were measuring and cutting the stubs - not from the center of the lines but from the edges.
When you measure from the centers, in particular for the 90 degree shifter, it adds another 3mm on either side, which would
have brought our data significantly closer to correct. 

*Task2:<br>
Data:
Zo = 50 ohms, 62 mil thick = 1.578mm, FR4 (Er = 4.1), f=2.5 GHz

For the Wilkinson Power Divider (WPD), the design is well-known so for the simulations, I knew we wanted a 3dB split
so the legs would be equal on the divider. For this, we have all three ports with impedance 50 ohms and the quarter
wavelength sections of the divider have impedance 70.7 ohms (increased by a factor of root 2). The resistor across the
two legs of the WPD is given by 2Zo = 100 ohms. Because we used a circular model for the WPD, the length of the line is not exactly what I initially calculated. From our calculations, a quarter wavelength in the 70.7 ohm section at 2.5GHz is 17.36 mm, however, this does not work exactly in our HFSS simulations. Because the line is curved, we add inductance to the line and effectively shorten the line so we have to add length to the line, according to online, you have to add approximately 1.5*w for a 180 degree span (2.5 mm). However, there are also effects generated from the t-junction split we have which create more inductance by the transformer effect and we have to add more length to our line to account for this. From HFSS, it turned out that 24.2mm length gave the best output instead of 17.36 mm. The results are shown below.

## Procedure
In lab we created the 50 ohm line standard and then we used the online microstrip calculator to figure out the wavelengths
and measurements for our stub lengths and then spent the remaining time cutting and soldering repeatedly. We measured the
50 ohm standard, then cut 1mm slits out of it at 15mm apart then placed two parallel 15mm strips on either side of the
line at appropriate distances to drop in our stubs for the 90/180 degree phase shifters. After taping the stubs, we in turn
soldered each phase shifted line and measured the data. We also measured the data for our 50 ohm line again after adding
the parallel lines, but it did not make any difference. After the phase shifter, we measured the data for the WPD.

## Results and Discussion

Thru Standards: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab7/ThruStandards.png)<br>
Not much change here.

90 Degree Phase Shifter: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab7/90PhaseShifter.png)<br>
As this graph shows, our data was off by about 25 degrees, which is very significant and cannot be from the cutting
and taping alone. I think the biggest difference was that we did not measure from the appropriate portions of the different
lines already taped down.

180 Degree Phase Shifter: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab7/180PhaseShifter.png)<br>
Our 180 degree phase shifter came in over by about 35 degrees and I am not sure entirely why this one did not
work as well. When we were soldering, we left a gap so the lines would not be touching and tried to account for
this in our measurements by subtracting a millimeter, but I don't know if this is enough to change the phase so much.

Mag S11: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab7/S11.png)<br>

Mag S21: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab7/S21.png)<br>
Here we can see that at 3 GHz we get about -3.7dB at port 2, which is actually lower than it should be, but not terribly
far off from the measured data.

Mag S22: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab7/S22.png)<br>

Mag S31: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab7/S31.png)<br>
We saw the same data here in S31 as we saw in S21, where the design frequency for the circuit seems to be lower
than intended and the loss is higher than desired at 3GHz.

Mag S32: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab7/S32.png)<br>
At S32 we should see high attenuation because we do not want the signals from ports 3 and 2 reflecting back and
forth between the two ports.

Mag S33: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab7/S33.png)<br>

## Conclusion
The phase shifter is important for controlling antenna directions and other applications and although the design is simple,
the precision is difficult to achieve. The WPD is a simple design for power splitting, in particular for even power
splits. However, there are many effects to account for with the layout of the microstrip. The line length changed pretty significantly from the original length due to the added inductance. The line probably has coupling effects as well from the split into ports 2 and 3 where the lines run almost parallel.

## Hindsight
I wish I understood how to measure the lengths for stubs and transmissions lines in microstrip better than I do,
because when you are dealing with millimeters, small changes make a significant difference. I am getting a better feel now for understanding the relationship between lumped element an transmission line models and how the effects of each translate back and forth.

## Reflection
The phase shifter was the most challenging, although it shouldn't have been. Understanding the theory of the Wilkinson 
divider was the most rewarding. I also see now how important the non ideal effects are for microstrip layout in the actual implementation of a design after treating the ideal case.
