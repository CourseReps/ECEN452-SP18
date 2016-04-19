<b>ECEN 452-500: Ultra High Frequency Techniques</b><br>
Spring 2016 – Prof. Huff<br>
Lab 10


<br>Step 6: Calculate the widths of the transmission lines and enter these into the design “N5_MaxFlat_LPF_T-Line” within the HFSS project “ECEN452_Lab6_Filters.hfss”. You will also need to enter this information into the “N5_MaxFlat_LPF_T-Line.zov” Z0lver assignment.<br>
<b>Ans:<br>
The original design parameters are shown in the following figures. Obviously, the results doesn't meet the requirement.<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab10/dielectric_constant.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab10/dielectric_loss.png) <br><br>
Also, the Zolver design layout and simulation results are shown in the following figures.<br>

<b>Conclusion:<br>

1. Dielectric constant of all the experimental material will change the values at different frequency. We observe the dielectric constant will decrease as the frequency goes higher.<br>
2. Different filter transformations are involved in the filter design. For the maximally LPF, the impedance and frequency scaling are needed. Also, the Richard's transformation and Kuroda's identities are involved to successfully implement the LPF design. On the other hand, the BSF needs one extra process from the prototype filter. The inductor should convert to an inductor parallel with a capacitor and a capacitor should convert to an inductor in series with a capacitor.
3. The lumped LC used in Task 1 step 7 only works well at low frequency. At high frequency, the distributed components are prefered.</b>
