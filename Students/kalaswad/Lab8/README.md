# Lab 8 Report
Matias Kalaswad

## Background
This lab introduced us to how different kinds of couplers operate. In lab we focused on the Rat-Race coupler and the Hybrid coupler. The Rat-Race coupler is used in planar technologies like microstrips and waveguides. It has four ports, each a quarter wavelength from each other around the top part of a ring with impedance factor of root 2 compared to the port’s impedance.  The Hybrid coupler is a passive device that is often used in radio and telecommunications.  It is a directional coupler with the input power divided equally between two output ports.

## Design
Both couplers were to be made in HFSS before lab. The Hybrid coupler was first and had input ports with 50 ohm characteristic impedance and quarter wavelength line. The two lines perpendicular to the input lines had a width of 3.105 mm and a length of 16.92 mm.  The lines connecting port 1 to port 2 and port 3 to port 4 had impedances of Z_0/√2 with Z_0=50 ohms, or 35.35 mm, widths of 5.25 mm, and lengths of 16.5 mm.  This is known as a quadrature coupler.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Lab8HybridHFSS.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Lab8HybridParameters.png)

The Rat-Race coupler was designed next. The lengths between the ports were quarter wavelengths, except for the 2 ports farthest away from each other which are separated by three quarter wavelengths. The total circumference is 1.5 wavelengths. The port measurements are like that of the hybrid coupler: 50 ohms, 3.105 mm width, 16.92 mm length.  The parts of the circle between ports has impedance Z_0*√2 = 70.7 ohms which translates to a width of 1.648 mm, and length of 17.36 mm.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Lab8_RatRace_HFSS.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Lab8_RatRace_Parameters.png)

## Procedure
We only had to do the simulations for this lab so there was no in-lab portion.

## Results and Discussion
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Hybrid_Coupler_Magnitude2.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/Hybrid_Coupler_Phase2.png)

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab8/RatRace_Magnitude2.png)

## Conclusion
The main point of this lab was to teach us about the Hybrid and Rat-Race couplers.  David took measurements in lab and gave us the results to compare to HFSS. These results were almost the same.

We put matched loads on the ports while measuring S-parameters so that the reflections from other ports don’t interfere.  It helped to get an accurate measurement at ports across the circuit from each other.

## Hindsight
We should have done more research on the couplers before the lab in order to understand what the results that David provided meant. We also wished we had more instruction of using HFSS.

## Reflection
The most difficult part of this lab was implementing the designs in HFSS because we have so little experience with it.  The best part of the lab was learning how the couplers work and how they are designed.
