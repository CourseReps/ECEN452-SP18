# Lab 8 Report
Lisa Smith

## Background

The hybrid coupler is a device that equally divides the power into the two output ports with a 90° phase shift. The Rat Race is another four port coupler that splits the input power in half. In addition, the rat race can have a phase shift of either 90° or 180°.

## Design

For Hybrid Coupler:

Below are the calculated values used for simulation at 2.5 Ghz. The values of length and width were found using an online calculator.

![lab_8_eq1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-8/lab_8_eq1.PNG)

![lab_8_values1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-8/lab_8_values1.PNG)

For Rat Race:

Below are the calculations and the values used in the HFSS simulation at 2.5 GHz. The values of length and width were found using an online calculator.

![lab_8_eq2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-8/lab_8_eq2.PNG)

![lab_8_values2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-8/lab_8_values2.PNG)

Both designs were made using the given HFSS files and substituting the calculated values above.

## Procedure
In lab, the devices were already fabricated on FR4 with milled copper. The devices were tested using the network analyzer and compared to the simulated results. 

## Results and Discussion
The device works similarly to the simulated results. The biggest difference is there is a shift in the operating frequency of the device from 2.5 GHz (as designed) to about 2.8 GHz (as built). This is a result in the arm lengths of the coupler are too short. In addition, the phase shift of the built device is always higher than the simulated. However both have a phase shift of about 90° at the design frequency of 2.5 GHz. S11 shows the matched port, S21 and S31 shows the power division, and S41 shows isolation.

![lab_8_graph1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-8/lab_8_graph1.PNG)

The device works similarly to the simulated results. S11 shows the matched port, S21 and S31 shows the power division, and S41 shows isolation.

![lab_8_graph2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/lisamsmith/lab-8/lab_8_graph2.PNG)

## Conclusion
In this lab, the measured and simulated results for each device were fairly similar. The phase shift of the output signal is the major consideration of which type of power divider to use. If no phase shift between the 2 outputs is wanted, the the hybrid coupler should be used. If a 90 degrees phase shift is wanted, then the rat race is the better device to use. Matched ports were used when measuring the devices to get more accurate results and to prevent any errors that would occur from impedance mismatch as opposed to error from the design.

## Hindsight
Because there was no actual building of the devices, this lab was fairly easy and straight forward.

## Reflection
This lab did give good insight to the operation of 2 types of power dividers and the advantages to each type of device and how they are designed.
