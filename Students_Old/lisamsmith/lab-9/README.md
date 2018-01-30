# Lab 9 Report
Lisa Smith

## Background

The patch antenna is a simple antenna that is linearly polarized. The patch antenna radiates like a monopole antenna. Unlike the dipole antenna, the patch radiates in only one direction because the ground plane reflects all the radiation that would otherwise radiated the opposite direction.

## Design

The equations below are used to find the dimensions of the patch antenna. For simulations, the antenna was feed directly with a coaxial probe. The position was found by moving the probe L/3 from the edge of the patch and refined using simulated data.

![lab_9_eq1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-9/lab_9_eq1.PNG)

![lab_9_values](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-9/lab_9_values.PNG)

## Procedure
In lab, a 50 Ohm microstrip transmission line was used to feed the antenna with a quarter wave transform used to match the antenna. The antenna was feed first with an unmatched to find the input impedance. Then a Smith chart was used to find how far away from the reference point (15 mm) the transform needed to be.

![lab_9_eq2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-9/lab_9_eq2.PNG)

## Results and Discussion
At 3 GHz, the simulated patch had a final impedance or 50.35+j0.75 and a VSWR of 1.017, while the measured patch had a final impedance of 60.592-j7.998 and a VSWR of 1.272. Both the simulated and measured patches are well matched and operate at the appropriate frequency. Below are the results for both the simulated and measured results for each of the patch antennas with the alternate matching a feed structures. 

![lab_9_graph](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-9/lab_9_graph.PNG)

## Conclusion
In this lab, the measured and simulated results for the patch antenna were fairly similar despite the difference in how the antenna was fed. 
## Hindsight
Because the was fairly large compared to the normal small width of the transmission lines, this lab was fairly easy and straight forward.

## Reflection
This lab did give good insight to the operation of the patch antenna and 2 types of feeding techniques.
