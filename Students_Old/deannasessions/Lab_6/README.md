# Lab 6 Report
Deanna Sessions

## Background
This lab was an introduction in filter design as well as an introduction to copper tape fabrication. Two types of filters were examined during the course of this lab, the low-pass filter and the band-stop filter. Both filters were examined and simulated within HFSS and then students fabricated a band-stop filter using copper tape and a blank sheet of FR4. The low-pass filters were milled on FR4 and measured to be compared to simulated data. 

## Design
Task 1:

Design Parameters:
Zo = 50 ohms
h = 62 mil
FR4 Er = 4.1
fc = 2.5 GHz
f-range = 1 GHz - 5 GHz 

A maximally flat low pass filter (LPF) was designed with a cutoff frequency of 2.5 GHz and a minimum attenuation of 10dB set at 3.25 GHz. This is calculated using with n = 5. 

Using this graph the g-values that correspond to the ladder LC circuit can be determined. 
g1 = 0.618
g2 = 1.618
g3 = 2.000
g4 = 1.618
g5 = 0.618

Each of the above g-values correspond to the shunt capacitors and series inductors above. 
Shunt Capacitors: Z = 1/g
Series Inductors: Z = g

This results in impedances as follows:
Z1 = 1.618
Z2 = 1.618
Z3 = 0.500 
Z4 = 1.618
Z5 = 1.618

Each section is 1/8 wavelength and the unit element impedances can be calculated in the same method. The values for the capacitors and inductors are found using the following equations:
L = (Zo)g/w
C = g/((Zo)w)

For the center tapped stub we were able to utilize our knowledge of open circuit stub impedances to calculate the lengths given a set impedance of 89 ohms. Necessary equation to complete this task includes:

Zoc = jZocot(Bl) in which Bl = pi/4

We use this equation to calculate ZocA, ZocB, ZocC which end up being j181, j43, and j25 respectively. Using these Zoc values we can then calculate the lengths of the lines using the following equation:

L = arccot(2ZocA/Zo)(lambda/(2pi)) where Zo = j89

This results in the following lengths:
L1 = L5 = 2.71 mm
L2 = L4 = 9.02mm
L3 = 11.89 mm
UEL1 = UEL2 = 8.67 mm
UEL3 = UEL4 = 8.91 mm

Task 2:

Design Parameters:
fc = 3GHz
delta(d) = 0.5
Zo = 50 ohms
FR4 Er = 4.1 
h = 62 mil
f-range = 2.25 GHz - 3.75 GHz

This band stop filter was designed much like the LPF in task 1 using the g-values found in the N = 5 column of the table. 

The resulting g-values:
g1 = g5 = 1.706
g2 = g4 = 1.230
g3 = 2.54

These g values use the same LC ladder network approach as before using quarter wavelength transformers to convert the design. The impedances are calculated using Z = (4Zo/pidg)

## Procedure
The width of the 50ohm line was calculated using an online calculator and the design process was completed as seen in the design section of this report. After designing the BSF and LPF the BSF was fabricated using copper tape and compared to the milled model. Stubs were measured and cut and artfully placed on the surface of a clean FR4 board based on the designs that were decided upon. After the copper tape was placed, the joints were soldered using a solder gun and connectors were attached to either end of the line. This was then tested using the VNA to retrieve data that could be used for comparison with the milled and simulated data.

## Results and Discussion
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_6/Lab6_LPF_T-Line.png)<br>

This graph shows the three different forms of the LPF that were tested; simulated, simulated tapped stub, and milled FR4. The simulated and the milled FR4 LPFs are similar enough in response. The simulated tapped stub has a different response than the other two, but still functions as a LPF and is arguably better at it than the other two.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_6/Lab6_LPF_Phase.png)<br>

This is the measured phase of the milled LPF on FR4.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_6/Lab6_BSF_T-Line.png)<br>

This shows the three different BSFs that were tested in the lab. They all have similar responses, but it is apparent that the different BSFs were following different frequency requirements.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_6/Lab6_BSF_Phase.png)<br>

This shows the mismatch in phase between the milled and the copper tape versions of the BSF. This can be attributed to slight variances in length and adjustments in design.

## Conclusion
As electrical engineers, we have been hearing about low-pass filters and band-stop filters for years and know how they are supposed to function, but this lab got into the design that goes into making a filter that functions at the proper frequency range and provides the proper response. There were a few hiccups in fabrication using the copper tape because it isn't exactly the most forgiving medium, but we were able to create a functioning filter. On top of fabricating the design, the different filters were simulated and adjusted based on the response. This lab provided an opportunity to design and then troubleshoot based on the intended response vs. the actual response.

## Hindsight
I wish I had known that solder guns and slivers of copper tape can be a pain to get just right. We were able to implement our design fairly painlessly, but there was a bit of fighting that came along with it. We had to get the air flow just right so that it didn't blow away the strips of copper tape. We also had to make sure that we were using a high enough heat setting to efficiently melt the solder while keeping a low enough heat to avoid melting the copper tape adhesive. 

## Reflection
This was a really fun lab and it was nice being able to fabricate and test a design right then and there without having to wait for milling to occur. It was also fun to take on the challenge of fabricating a copper tape model that rivalled the milled version. This was a good lab to really get into the groove of creating microwave structures and testing them for comparison to simulations.
