Lab 6

Background:

In this week's lab, the students designed high frequency lowpass and bandstop filters.  The filters
were designed using distributed elements in a process that began with table lookup to determine the
necessary filter coefficients and culminated in transforming a ladder network to a series of open
circuit stubs through the application of Richard's Transformation and Kuroda's Identities.  The
lab culminated in the fabrication of the bandstop filter by means of a cut-and-solder technique 
utilizing copper tape on FR-4 substrate.

Application:

Filters are essential in many aspects of high frequency design, where it is necessary to remove noise
from signals which are transmitted or recieved.  A filter is used to process input signals from an
antenna and to focus output signals into a desired frequency band.

Design:

![Filter Calculations](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab_Notebook(Antenna%26Filters).pdf)

The design of the filters began with a prototype ladder network using normalized parameters obtained from a table to calculate maximally flat and equi-ripple designs.  The series stubs were transformed to open circuit stubs and then spacing transmission lines were added using Richard's Transformation and Kuroda's Identities.

Procedure:

The student cut and pasted strips of copper tape onto FR-4 substrate in order to create a distributed
element bandstop filter in microstrip according to the design calculations done in the prelab.  Separate
strips of tape were joined using solder, and the output was plotted using a network analyzer. 

Results:

![Band Stop Filter Simulation](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab6/BSF_Sim.png)

The simulated response shows a stop band at 3 GHz in excellent agreement with measured results.

![Low Pass Filter Simulation](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab6/LPF_Sim.png)

The simulation shows a good agreement with the measured data, but as in the milled version the pole frequency is a bit high, suggesting that the stubs may be a bit too long.

![Tapped Stub Low Pass Filter Simulation](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab6/LPF_T_Sim.png)

The simulated response of this filter shows a pole frequency right at 3 GHz, in perfect agreement with the design parameters.

![50 Ohm Line](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab6/Measured_50ohm_Line.png)

The 50 ohm line shows the expected near unity transmission of signal.

![Cut-Tape BSF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab6/Measured_BSF.png)

The filter response shows a stop band around 3 GHz.  The response is shifted slightly toward higher frequencies, indicating that the stub lengths are slightly shorter than they should be.  Ultimately,  the design met the specified parameters within acceptable error bounds, especially considering that it was hand fabricated using copper tape.

![Milled BSF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab6/Measured_Milled_BSF.png)

The milled filter response shows a stop band around 2.6 GHz, slightly shy of the target 3 GHz.  The stop band of the filter is much more symmetrical and smooth than the copper tape design due to the precision of its fabrication.

![Milled LPF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/derekjanak/Lab6/Measured_Milled_LPF.png)

The milled low-pass filter design shows a low reflectivity which reaches a minimum around the target 3 GHz before rising to near unity.  This is accompanied by a unity transmission which begins to fall off after the pole frequency at approximately 3 GHz.

Conclusion:

In this lab, the student learned to design several basic filters for various high frequency signals.
The student then gained the added experience of fabricating their design and taking measurements on
the phase and magnitude of the frequency response.

Hindsight:

In hindsight, I could have used more time to calculate design parameters and to troubleshoot my design;
however, ultimately, this lab was a rewarding and engaging experience.

Reflection:

The most challenging portion of the lab was the completion of the necessary theoretical design work.
The lab proved exceedingly rewarding by serving as a proof-of-concept for my skills in microwave design.
