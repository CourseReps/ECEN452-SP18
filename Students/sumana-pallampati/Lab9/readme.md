# Lab 9 Report
Sumana Pallampati

## Background
A rectangular patch antenna consists of a metal sheet called a patch, a substrate and a ground plane. The resonant length determines the operating frequency and the width controls the impedance and efficiency. The best possible geometry of a rectangular patch is a square patch. The length of the patch is usually half wavelength long. The fringing fields along L create a length extending effect (capacitive) that alters the resonant frequency of the patch. Thus, a correction term is introduced and the physical length is shorter than the electrical length. There are many types of matching methods namely stub matching, quarter wave transformer matching, inset feed etc. The types of feeding methods inculde edge fed and coaxial fed. 

## Design
The length and width of the patch were calculated using the design parameters namely f = 3 GHz, eps_r = 4.1 for FR4 and the height of the substrate h = 62 mil = 1.5748 mm. The equations are given below - <br>
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab9/Screen%20Shot%202016-04-13%20at%202.24.04%20PM.png)
Using the equations, W = 31.31 mm, L = 22.107 mm and eps_eff = 4.513. The length of the stub is 0.372*lambda = 19.05 mm and the distance of the stub from the reference plane is d = 0.28*lambda = 14.34 mm. In the HFSS simulation, the length of the patch is increased to 23.7 mm to obtain a minimum VSWR at 3 GHz. The distance of the probe from the centre of the patch was found to be 5.7 mm. At this point, the patch was matched to 50 ohm at 3 GHz.

## Procedure
In the lab, we first cut out a patch with the required dimensions from copper tape. We measured the input impedance of the patch using a 50 ohm feed line and read the impedance at 3 GHz from the smith chart. Then we designed the stub matching network for the input impedance so that it matches with the source impedance. Then we measured the VSWR and S11 on the smith chart for the matched patch antenna. The HFSS simulation involved changing the length and width of the patch and determing the location of the coaxial probe. With the calculated values, an initial simulation was run and then the parameters were tweaked to obtain a VSWR value close to 1 at 3 GHz.

## Results and Discussion
The comparison between VSWR of the stub matching, unmatched and probe fed simulation in HFSS is as follows -
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab9/VSWR.png) <br>
The S11 plotted on smith chart for the HFSS simulation is as follows -
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab9/SmithChart_HFSS.PNG) <br>
It is observed that copper tape version of the patch antenna resonates at around 3.4 GHz. This can be attributed inaccuracies while cutting the tape and thus the length is shorter than it is supposed to be. The stub matching provides a VSWR of 1.2 which is good. The HFSS simulation provides the VSWR of 1.04.

## Conclusion 
The design procedure of the patch antenna involves the calculation of length, width and eps_eff from the specifications of operating frequency, eps_r and height of the substrate. Then it should be matched to the characteristic impedance and this can be accomplished using either an inset, stub or quarter wave matching. 

## Hindsight
The design was pretty straightforward and I understood the matching networks better after the lab.

## Reflection
The design of the stub matching was bit tricky as we had to consider the distance from the generator instead of the load. But, the designing process was smooth and had no other issues during fabrication.
