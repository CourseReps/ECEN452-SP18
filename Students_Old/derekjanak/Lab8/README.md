Lab 8: Couplers

![Hybrid Coupler](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Hybrid.PNG)
![Rat Race Coupler](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/RatRace.PNG)

Background:

This lab focused on the demonstration of milled  quadrature hybrid couplers and rat race coupler 
designs similar to those covered in class.  Couplers such as these are important in the design of 
high frequency systems, where they function primarily as mixers,power dividers, and phase shifters.
Additionally, the rat race coupler finds applications in the summing and subtraction of input 
signals.

Application:

These coupler designs are very useful for processing input and output signals.  The rat race
coupler's ability to sum or subtract inputs allows it to combine signals from recievers that
are either in phase or 180 degrees out of phase.  The hybrid coupler will be applied further in
the final project of the course, where it will be used as a variable phase shifter in order to
control beam steering of a patch antenna array.

Design:

The rat race coupler consists of a ring of characteristic impedance Z0*sqrt(2) (Assuming even power
split) with a circumference of 1.5 wavelengths.  Spaced around the port are four ports with feedlines of 
characteristic impedance Z0.  Port 2 is the input port.  Port 1 is spaced one quarter wavelength 
clockwise around the circle from port 2,and functions as a summation of inputs at ports 2 and 3.  
Port 3 is spaced one quarter wavelength clockwise from port 1, and is isolated.  Port 4 is spaced one 
quarter wavelength clockwise from port 3, and functions as a difference of inputs at ports 2 and 3.
Application of an input signal at port 1 yields an in-phase power division at ports 2 and 3, while
application of an input signal at port 4 yields a 180 degree out-of-phase power division at ports
2 and 3.

The quadrature hybrid coupler consisted of a square structure of transmission lines in which the
horizontal lines are of characteristic impedance Z0/sqrt(2) and the vertical lines are of
characteristic impedance Z0.  Matched feedlines of characteristic impedance Z0 extend from each of
the four corners of the structure.  At the top left corner of the structure is port 1 (input).  At
the top right of the structure is port 2 (output, 0 degrees shift).  At the lower right of the
structure is port 3 (output, 90 degree shift with respect to port 2, 3 dB power division).  At the
lower left of the structure is port 4; this port is isolated.

Even/odd mode analysis was used in the design of both devices, as well as in the theoretical
verification of their functionalities.

Procedure:

The devices were designed and simulated in HFSS in order to verify their correct operation.  The
designs were then milled in microstrip on a 62 mil FR4 substrate.  In lab, the network analyzer was
used to measure each of the devices and the results were saved.  Plots of simulated and measured
data were created.  During measurement, it was necessary to provide matched loads at unused ports when
taking a measurement in order to prevent reflections which would introduce noice and error into the
measurements.

Results:

![Simulated Hybrid Coupler Input Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Simulated_Hybrid_Input.png)

The simulation plot shows transmission from port 2 to port 1 and port 3 to port 1, and isolation between ports 1 and 4.  This is in good agreement with measured values.  Due to design error, the center frequency was mistakenly chosen as 3 GHz, explaining the offset from measured values.

![Simulated Hybrid Coupler Port Match](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Simulated_Hybrid_Port_Match.png)

The simulation shows all ports matched just below 3 GHz.  During simulation, 3 GHz was mistakenly used as the target value, explaining the large deviation from 2.5 GHz.  Taking this discrepancy into account, the values match with the measured data.

![Simulated Hybrid Coupler 2-3 Phase shift](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Simulated_Hybrid_Coupler_Phase.png)

The simulation shows the phase difference between ports 2 and 3 reaching 90 degrees at the design frequency, in agreement with design specifications.

![Measured Hybrid Coupler 2-3 Phase shift](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Phase_Shift.png)

As in the simulations, the phase difference between ports 2 and 3 approaches 90 degrees at the design frequency.

![Hybrid Coupler Port 1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_Milled_Hybrid_Port1.png)

The reflection shows the expected minimum at the design frequency of 2.5 GHz.

![Hybrid Coupler Port 2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_Milled_Hybrid_Port2.png)

The S21 value is approximately -3 dB and the S22 value is minimized at the design frequency, as expected.  The phase shift is noticeable, as can be seen from comparison with the S11 phase.

![Hybrid Coupler Port 3](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_Milled_Hybrid_Port3.png)

The S33 and S32 values are minimized at the design frequency, indicating that the two ports are isolated.  The S31  value is approximately -3 dB.  The phase shift is even greater, approximately 180 degrees.

![Hybrid Coupler Port 4](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_Milled_Hybrid_Port4.png)

The data shows port 4 as being isolated from port 1.  The effects observed at ports 2 and 3 are inverted, with port 2 yielding the greater phase shift.

![Simulated Rat Race Coupler Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Simulated_RatRace.png)

The simulation shows transmission from ports 2 and 3 to port 1 and isolation between ports 4 and 1 (Based on S41).  This agrees well with experimental data.

![Rat Race Coupler Port 1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_RatRace_Port1.png)

Port 1 shows low reflectivity near the design frequency, as well as 90 degree phase shift from port 2.

![Rat Race Coupler Port 2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_RatRace_Port2.png)

Port 2 shows low reflectivity and relative isolation (Based on S23) from port 3 at the design frequency.

![Rat Race Coupler Port 3](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_RatRace_Port3.png)

Port 3 shows transmission to port 1 at the design frequency.

![Rat Race Coupler Port 4](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_RatRace_Port4.png)

Port 4 appears to be isolated with inverted effects at ports 2 and 3.

Conclusion:

In this lab, the students designed and simulated rat race and quadrature hybrid couplers.  The
students then took measurements on a fabricated circuit to verify the functionality of the
design.  The design was based on models discussed in lecture, and provided a thorough exercise
in even/odd mode analysis.  There were few difficulties in completing this lab, as the design
was covered thoroughly in lecture and the major part of the assignment centered on the simulation
of the design.

The simulations did provide a slight challenge, as it was necessary to shorten the lengths of the hybrid coupler
transmission lines in order to compensate for excess reactance.

Hindsight:

In completion of this lab, I felt that I learned a significant amount about the foundations of
coupling circuits.  I would have liked to have fabricated my own design, but time and material
limitations made this infeasible for each student to fabricate a board.  I also would have liked
to investigate applications of these devices; however, this opportunity will be given during the
final project.

Reflection:

The challenges in this lab stemmed from HFFS simulation of the circuits.  Difficulties were primarily
logistical, as student access to the HFFS software is limited.  The greatest benefit of this lab
was the illustration of the phase shifter and coupler concepts within more complex and practical
circuit designs.
