# Lab Report 6
Thomas Darden

## Background
For this lab we are designing two low pass filters and a band stop filter. We will be conducting the design and simulation of all three filters, but in lab we are only constructing the band stop filter. These filters will be designed with a 50ohm reference impedance on a 62mil thick FR4 substrate.

## Design
We will first design a maximally-flat low pass filter with a cutoff frequency of 2.5GHz and a minimum attenuation of 10dB at 3.25GHz.
To do this, we must first find the order N of the filter. We can find this by using the following equation:

abs(f_10dB/f_cutoff)-1

abs(3.25GHz/2.5GHz)-1 = 1.3 - 1 = 0.3

We use this number to find the order in the following graph:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab6/Attenuation%20Chart.PNG)<br>
From this, we find we must construct a fifth order circuit.
Using a look-up table, we find that the five element value we need are the following:

g1 = 0.6180

g2 = 1.6180

g3 = 2.0000

g4 = 1.6180

g5 = 0.6180

We now need to use Richard's Transformation to convert the caps to open circuit stubs and the inductors to short circuit stubs.

For caps, this means that z_new = 1/g

For inductors, this means that z_new = g

Now our five values shall be represented as z, as opposed to g, giving us the following:

z1 = 1.61804, z2 = 1.61803, z3 = 0.50000, z4 = 1.61803, z5 = 1.61804

From these values, we must use Kuroda's identities to convert series stubs to shunt stubs. We first do this by inserting unit elements on the source side (we are capitalizing on symmetry for less work). We will look only at the right side of the circuit (z1, z2, and z3). This gives us the following config:

ue1 = 1, z1 = 1.61804, z2 = 1.61803, z3 = 0.50000 (the order the values are presented in is the configuration of the circuit)

Using the identity, we switch units ue1 and z1 finding ue1's new resistance to be ue1' = z1/(1+ue1/z1) = 0.61922 and z1' = ue1/(1+ue1/z1) = 0.38270. This gives us:

z1' = 0.38270, ue1' = .61922, z2 = 1.61803, z3 = 0.50000

Adding another unit element to the source side and performing another conversion we find that we have the following configuration:

z1" = 3.61804, ue3' = 1.38196, z2' = 0.85410, ue1" = 2.23607, z3 = 0.50000

Applying symmetru and impedance scaling to convert the elements into transmission lines gives us:

Element z1 = 181ohms, 0.125*wavelength = 9.095mm, width = 0.084247mm

Element ue3 = 69ohms, 0.125*wavelength = 8.637mm, width = 1.759mm

Element z2 = 43ohms, 0.125*wavelength = 8.351mm, width = 3.9619mm

Element ue1 = 112ohms, 0.125*wavelength = 8.8976mm, width = 0.53918mm

Element z3 = 25 ohms, 0.125*wavelength = 8.0428mm, width = 8.3965mm

Element ue2 = 112ohms, 0.125*wavelength = 8.8976mm, width = 0.53918mm

Element z4 = 43ohms, 0.125*wavelength = 8.351mm, width = 1.759mm

Element ue4 = 69ohms, 0.125*wavelength = 8.637mm, width = 1.759mm

Element z5 = 181ohms, 0.125*wavelength = 9.095mm, width = 0.084247mm

We found the widths and the lengths of the lines by using the microstrip calculator available online.
We use the values we have found above and simulate them in HFSS. 
We can perform impedance and frequency scaling for the lumped element prototype found earlier to find the values of the inductors and capacitors in the circuit. We can find that:

C1 = C5 = (0.618/50)/(2*pi*2.5*10^9) = 0.787pF

L2 = L4 = (50*1.6180)/(2*pi*2.5*10^9) = 5.15nF

C3 = (2/50)/(2*pi*2.5*10^9) = 2.546pF

The low pass filter we have designed, however, can be difficult to implement without being milled. To fix this problem, we can design a filter that is modified with tapped stubs. As a design parameter, we define the stubs to have a 1mm width (giving them a resistance of 89ohms). Using the online calculator with this knowledge, we can find the effective wavelength to be 70.2452mm. This is an important value, as we need it to find the length of the stubs in the following equation:

L_stubs = (wavelength/(2*pi))*arccot(2*Z/89)

From this equation, we find the length of the stubs to be:

L_1 = L_5 = 2.695mm

L_2 = L_4 = 8.972mm

L_3 = 11.839mm

Using these values, we will run an HFSS simulation.

Now we must design a fifth-order 0.5dB equi-ripple band stop filter with a center frequency of 3GHz and a bandwidth of 2.25GHz to 3.75GHz (delta = 0.5). For the fifth order circuit, we use a loop up table to find the element values:

g1 = 1.7058

g2 = 1.2296

g3 = 2.5408

g4 = 1.2296

g5 = 1.7058

Using quarter-wave transformers to convert the circuit to shunt stubs, we find the configuration of the circuit (on the source side) to be:

z1, ue1, z2, ue2, z3

The inverters have a element value of 1. We can find the impedance of all elements using the following equation:

Z_s = (4*89)/(pi*delta*g_n)

z1 = z5 = 74.6418ohms

z2 = z4 = 103.549ohms

z3 = 50.118ohms

ue1 = ue2 = ue3 = ue4 = 50ohms

All elements will have the length of the effective wavelength/4. Using the online calculator, we find these value to be:

Z = 50ohms : width = 3.115mm, L = 14.036mm

Z = 75ohms : width = 1.4778mm, L = 14.451mm

Z = 104ohms : width = 0.667mm, L = 14.751mm

We will use these length when building our constructed band stop filter and when simulating in HFSS.

## Procedure
Simulate the low pass filters in HFSS.

Simulate the band stop filter in HFSS.

Create the bandstop filter by cutting copper tape measured to the specified lengths and widths. Attach those to the board and solder the connectors on as well as the junction between the stubs and the feed line. Be sure to measure the 50ohm feed line first with the network anaylzer to make sure your feed line is correct. Then measure the completed circuit with the networkd analyzer to see the accuracy of the filter.

## Results and Discussion
From the low pass filters, we got the following simulation data and measured data plotted in the below graphs.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab6/LPF_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab6/LPF_Phase.png)<br>
From these graphs it is clear to see that the tapped LPF works relatively better than the untapped by attenuating the higher frequencies at a faster rate. Our simulated untapped LPF works about the same as the milled LPF with the milled LPF not working as effectively as the simulated design implied. However, it is clear from the simulations that the filter do work as intended, allowing the lower frequencies to propogate while reflecting the higher frequencies.

For the band stop filter we designed, we first measured the 50ohm line we created in lab to test for accuracy. The results are as follows:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab6/50Ohm_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab6/50Ohm_Phase.png)<br>
From these graphs, we can tell that the feed line is allowing the signal to propogate with minimal insertion loss or reflection.

The results from the completed band stop filter, as well as the simulated filter, are presented in the following graphs:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab6/BPF_dB.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab6/BPF_Phase.png)<br>
From the above graphs, we can see the filter we designed in HFSS and constructed in lab is performing exactly as expected. The S21 parameter is maximized within the frequency range we wanted, with 3GHz being the center of the band. The milled filter, however, appears to have been designed incorrectly. It is possible that this filter was designed with a center frequency of 2.5GHz, however, this was not our design parameter. 

## Conclusion
Through this lab, I was able to learn how to create filter without the use of inductors or capacitors. I learned that there are multiple ways to construct a filter, based on the tools you have access too. The copper tape design we made functioned as desired, though we had to be careful when soldering on the stubs, as the extra solder could affect our filter greatly (as it did many others).

## Hindsight
It would have been nice to know how to use the air gun before the lab so some uncoordinated people (like myself) wouldn't hurt themselves. 

## Reflection
Overall, this lab was fun as I got to create the filter myself. I did manage to slightly burn myself, but that was definitely my own fault. 
