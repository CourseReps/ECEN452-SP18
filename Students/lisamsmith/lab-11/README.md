# Lab 11 Report
Lisa Smith

## Background

In contrast to the last lab, this lab will focus on how to find the dielectric of a solid as opposed to a liquid. A free space calibration was achieved by using a Gated, Reflect, Line (GRL) calibration. In this set up, a signal is incident at a material and the reflected and transmitted waves are recorded (using two horn antennas in this case) and use to calculate both the permeability and permittivity of the material.

## Design

This lab did not require any device design. 

## Procedure

Before the GRL calibration can take place, the cables that will be connected to the horn antennas are calibrated with a Short, Open, Line, Thru (SOLT) calibration. This will remove any errors due to the cables for more accurate results (just like with any normal measurement with the network analyzer connected to an antenna). The GRL calibration begins with placing a sample of plexiglass between the horns followed by a piece of metal that acts as the reflect. This data then undergoes a time domain Fourier transform in order to place the gates for the calibration. In addition to the two samples mentioned, both air and a piece of cardboard were measured.

## Results and Discussion

Form the pre-GRL data, it can be seen that the gate reflection occurs at 3.66 ns (local maximum). The information from the time domain allows us to find where the gating needs to be applied so more accurate data can be given by the GRL calibration. As seen in the post-GRL data, the S11 parameter very closely matches to zero, signifying full reflection. The graphs below show the values for E' of each material from 1 to 5 GHZ. 

![lab_11_graph1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-11/lab_11_graph1.PNG)

![lab_11_graph2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-11/lab_11_graph2.PNG)

![lab_11_graph3](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-11/lab_11_graoh3.PNG)

## Conclusion
In the post-GRL calibration data, S11 goes above zero at about 3.15 Ghz. This means there is stilll error event after calibration. This could be solved by having more absorber around the test set up, a better SOLT calibration, and better matched horn antennas. 

## Hindsight
This lab was just observation and just data processing after the data was measured.

## Reflection
This lab gave insight into how the dielectric of a material is found as well as understanding free space measurements.


