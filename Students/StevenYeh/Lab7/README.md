<b>ECEN 452-500: Ultra High Frequency Techniques</b><br>
Spring 2016 – Prof. Huff<br>
Lab 7


Task 1: Wilkinson Power Divider Design<br>
<br>Step 1:In this exercise, a two ways power divider will be designed and simulated in the HFSS. The power divider should have 3 dB equal split characteristics at 2.5 GHz. A minimum return loss at each port should be less than -10 dB and a decent isolation between port #2 and port #3 is wanted. All the ports have characteristic impedance of 50 Ohm.<br>
<b>Ans:<br>
The design layout along with the parameters(width, length and so on) are shown in the following figure.<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab7/design_layout.png)<br>
Figure 1 - Disign layout of the power divider<br><br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab7/design_parameters.png)<br>
Figure 2 - Design parameter<br><br>

A 100 Ohm resistor is connected at the joint of the traces to provide good isolation between port #2 and port #3. The quarter-wavelength ring structure has impedance of 70.71 Ohm and trace length of 17.36mm. The traces after the ring structure are also quarter-wavelength and have impedance tapering features. Because the designs are all symmetric, we are supposed to have a 3 dB power split result.<br></b>

<br>Step 2: Next, the S parameters of the Wilkinson power divider are illustrated below.<br>
<b>Ans:<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab7/S_parameter.png)<br>
Figure 3 - S parameters<br><br>

The results shown a very close power split between port #2 and port #3 which are -3.57 dB and -3.59 dB, respectively. An -14.89 dB isolation is founded between port #2 and port #3. Next, all the ports have return loss less than -14.75 dB are observed. The insertion loss is around 0.5 dB from port #1 to port #2 or port #3 which is acceptable at 2.5 GHz. A little bit losses come from the conductor or dielectric material are expected. The FR4 substrate can provide acceptable performance at 2.5 GHz.</b><br>


<b>Conclusion:<br>

1. Two filters are designed using the insertion loss method in this lab. One is the maximally flat LPF and another is the Equal-Ripple BSF.<br>
2. Different filter transformations are involved in the filter design. For the maximally LPF, the impedance and frequency scaling are needed. Also, the Richard's transformation and Kuroda's identities are involved to successfully implement the LPF design. On the other hand, the BSF needs one extra process from the prototype filter. The inductor should convert to an inductor parallel with a capacitor and a capacitor should convert to an inductor in series with a capacitor.
3. The lumped LC used in Task 1 step 7 only works well at low frequency. At high frequency, the distributed components are prefered.</b>
