Lab 8: Couplers

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

The rat race coupler consists of a ring of characteristic impedance Z0*sqrt(2) with a 
circumference of 1.5 wavelengths.  Spaced around the port are four ports with feedlines of 
characteristic impedance Z0.  Port 2 is the input port.  Port 1 is spaced one quarter wavelength 
clockwise around the circle,and functions as a summation of inputs at ports 2 and 3.  Port 3 is 
spaced one quarter wavelength clockwise from port 1, and is isolated.  Port 4 is spaced one 
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
data were created.

Results:

![Hybrid Coupler Port 1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_Milled_Hybrid_Port1.png)

The reflection shows the expected minimum at the design frequency of 2.5 GHz.

![Hybrid Coupler Port 2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_Milled_Hybrid_Port2.png)

The S21 value is approximately -3 dB and the S22 value is minimized at the design frequency, as expected.  The phase shift is noticeable, as can be seen from comparison with the S11 phase.

![Hybrid Coupler Port 3](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_Milled_Hybrid_Port3.png)

The S33 and S32 values are minimized at the design frequency, indicating that the two ports are isolated.  The S31  value is approximately -3 dB.  The phase shift is even greater, approximately 180 degrees.

![Hybrid Coupler Port 4](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_Milled_Hybrid_Port4.png)

The data shows port 4 as being isolated from port 1.  The effects observed at ports 2 and 3 are inverted, with port 2 yielding the greater phase shift.

![Rat Race Coupler Port 1](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_RatRace_Port1.png)

Port 1 shows low reflectivity near the design frequency, as well as 90 degree phase shift from port 2.

![Rat Race Coupler Port 2](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab8/Measured_RatRace_Port2.png)

Port 2 shows low reflectivity and relative isolation from port 3 at the design frequency.

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
