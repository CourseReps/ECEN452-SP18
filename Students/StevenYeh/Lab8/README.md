<b>ECEN 452-500: Ultra High Frequency Techniques</b><br>
Spring 2016 – Prof. Huff<br>
Lab 8


Task 1: Hybrid Coupler<br>
<br>Step 1:In this exercise, a four port hybrid coupler will be designed and simulated in the HFSS. Port #1 is the input port, port #2 is the through port, port #3 is the coupled port and port #4 is the isolation port. The coupler should have a 3 dB power split from port #1 to port #2 and port #3. A minimum return loss at each port should be less than -10 dB and at port #4 there should have no power out. All the ports have characteristic impedance of 50 Ohm and are designed to operate at 2.5 GHz.<br>
<b>Ans:<br>
<br>Step 2: The design layout along with the parameters(width, length and so on) are shown in the following figure.<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/design_layout_hybrid_coupler.png)<br>
Figure 1 - Disign layout of the hybrid coupler<br><br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/design_parameter_hybrid_coupler.png)<br>
Figure 2 - Design parameter<br><br>

The coupler x trace is calculated to have impedance of 50 Ohm; on the other hand, the coupler y trace has 35.36 Ohm impedance. Each traces on the coupler are designed to be quarter-wavelength. The port #2 and port #3 have phase delay of 90 degrees and 180 degrees respectively if input from port #1. If input from port #2 or port #3, the results are the same due to the symmetric structure. It's also a reciprocal device and it can be proved from the S matrix. <br></b>

<br>Step 2: Next, the S parameters of the hybrid coupler are illustrated below.<br>
<b>Ans:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/input_port_s_parameters_dB_hybrid_coupler.png)<br>
Figure 3 - Input from Port #1 to Port #2, #3, and #4<br><br>

The above results shown a very close power split between port #2 and port #3 which are -3.51 dB and -3.71 dB, respectively. An -22.91 dB isolation is founded at port #4. The insertion loss is around 0.51 dB from port #1 to port #2 and 0.71 dB from port #1 to port #3 at 2.5 GHz. A little bit losses come from the conductor or dielectric material are expected. The FR4 substrate can provide decent performance at 2.5 GHz.<br><br>


![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/port_matching_s_parameters_dB_hybrid_coupler.png)<br>
Figure 4 - Impedance Matching at each port <br><br>

Moreover, all the ports have return loss less than -20 dB are observed and it means only 1% of the power will be returned back to the source.<br><br>



![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/input_port_90deg_phase_difference_hybrid_coupler.png)<br>
Figure 5 - Phase difference between port #2 and port #3 (input from port #1)<br><br>


A 89.58 degree of phase difference is simulated from port #1 to port #3 which is acceptable to the desired values. The ideal phase difference value is 90 degrees from port #2 and port #3, if input from port #1.</b><br><br>



<br>Step 3: Finally, the simulated and measured data are compared and shown in the following figures.<br>
<b>Ans:<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/power_split_ioslation_hybrid_coupler.png)<br>
Figure 6 - Input from Port #1 to Port #2, #3, and #4<br><br>


![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/impedance_matching_hybrid_coupler.png)<br>
Figure 7 - Impedance Matching at each port<br><br>


![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/phase_difference_between_2_3_hybrid_coupler.png)<br>
Figure 8 - Phase difference between port #2 and port #3 (input from port #1)<br><br>


The measured results agree with the simulate ones.


</b><br><br>









Task 2: Rat-Race Coupler<br>
<br>Step 1:In this exercise, a 180 degree hybrid will be designed and simulated in the HFSS. A 0 degree or 180 degree phase differences are expected when input from port #1 or port #4. If input from port #1, it will be eaually split into two in-phase signals at port #2 and port #3. In this case, port #4 will be isolated. On the contrary, if input from port #4, two evenlys split signals with 180 degree phase difference can be derived at port #2 and #3. Also the port #1 is the isolation port in this case.<r>
A minimum return loss at each port should be less than -10 dB and a decent isolation between port #2 and port #3 is wanted. All the ports have characteristic impedance of 50 Ohm.<br>
<b>Ans:<br>
The design layout along with the parameters(width, length and so on) are shown in the following figure.<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/design_layout_rat_race.png)<br>
Figure 1 - Disign layout of the rat-race coupler<br><br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab8/design_parameters_rat_race.png)<br>
Figure 2 - Design parameter<br><br>

A 100 Ohm resistor is connected at the joint of the traces to provide good isolation between port #2 and port #3. The quarter-wavelength ring structure has impedance of 70.71 Ohm and trace length of 17.36mm. The traces after the ring structure are also quarter-wavelength and have impedance tapering features. Because the designs are all symmetric, we are supposed to have a 3 dB power split result.<br></b>

<br>Step 2: Next, the S parameters of the Wilkinson power divider are illustrated below.<br>
<b>Ans:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab7/S_parameter.png)<br>
Figure 3 - S parameters<br><br>

The results shown a very close power split between port #2 and port #3 which are -3.57 dB and -3.59 dB, respectively. An -14.89 dB isolation is founded between port #2 and port #3. Next, all the ports have return loss less than -14.75 dB are observed. The insertion loss is around 0.5 dB from port #1 to port #2 or port #3 which is acceptable at 2.5 GHz. A little bit losses come from the conductor or dielectric material are expected. The FR4 substrate can provide acceptable performance at 2.5 GHz.</b><br>

<br>Step 3: Finally, the simulated and measured data are compared and shown in the following figures. The results are close from the simulated and measured data.<br>
<b>Ans:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab7/impedance_matching_comparison.png)<br>
Figure 4 - Impedance Matching comparison <br><br>


![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab7/power_split_isolation_comparison.png)<br>
Figure 5 - Power split and isolation comparison</b><br><br>
