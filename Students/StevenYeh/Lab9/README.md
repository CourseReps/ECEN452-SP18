<b>ECEN 452-500: Ultra High Frequency Techniques</b><br>
Spring 2016 – Prof. Huff<br>
Lab 9 - Patch Antenna HFSS design

For the Lab 9 activity you made an edge-fed patch antenna using copper tape on an FR4 substrate. You used either a quarter wave transformer or a single stub to impedance match the antenna. In the HFSS file for Lab 9 you will design a probe-fed patch antenna on 62 mil FR4 at 3GHz; same parameters as the in-lab activity. You will impedance match this antenna by adjusting the position of the probe feed. The following steps outline the process for designing this antenna.<br>





<br>Step 1: Calculate the dimensions of the patch using the formulas and design parameters from the in-lab activity (f = 3GHz, εr = 4.1, h = 1.5748mm).<br>
<b>Ans:<br>
w = (c/2*f) * sqrt(2/εr + 1) = 31.31 mm<br>
ε_eff = (εr+1)/2  + (εr-1/2)*(1+12*(h/w))^-0.5 = 3.77<br>
ΔL = 0.412*h*((εr+0.3)*(w/h + 0.264)/(εr_eff-0.258)*(w/h + 0.8)) = 0.7324 mm<br>
L = c/(2*f*sqrt(ε_eff)) - 2*ΔL = 24.29 mm<br></b>




<br>Step 2: Enter these dimensions into the HFSS design for patch_width and patch_length<br>


<br>Step 3: Enter a value for the probe position along the x-axis (probe_feed_x)<br>



<br>Step 4: Look at the VSWR plot to make sure the patch is resonant at 3GHz. You should see a minimum at 3GHz. Adjust patch_length accordingly.<br>
<b>Ans:<br>
The optimum simulation results of the patch antenna is when patch_length = 23.85 mm and patch_width = 24 mm. Similarly, the feeding probe has a 7.225 mm distance (probe_feed_x = 4.7 mm) away from the edge of the patch surface. The HFSS design parameters are provided as the figure together with the design layout.<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab9/patch_hfss_design_parameters.png)<br><br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab9/patch_hfss.png)<br><br>

The patch has VSWR of 1.0552 at 3 GHz and has a bandwidth of 84.4 MHz (2.9576GHz to 3.0420 GHz). As a result, the patch has the best impedance matching to the 50 Ohm at 3 GHz. The results achieve the requirement of VSWR below 1.2.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab9/patch_hfss_vswr.png)<br><br>
</b>



<br>Step 5: Look at the Smith Chart to check the impedance match of the antenna. Use your notes from class to determine whether to move the probe closer to the center or closer to the edge of the patch. Adjust probe_feed_x accordingly and rerun your simulation.<br>
<b>Ans:<br>
As mentioned above, when probe_feed_x = 4.7 mm comes the best impedance matching results. The Smith chart illustrated the resonant frequency is around 3 GHz and the normalized input impedance is 1.0389 - 0.0386j. The imaginary part of the impedance is very small which prove the resonance of the patch.<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab9/patch_hfss_smith_chart.png)<br><br>
</b>






<br>Step 6: Repeat steps 4 and 5 and keep adjusting until the design is impedance matched at 3GHz. You should see a VSWR minimum at 3GHz (±50MHz); try to get the value at 3GHz below 1.2. The 3GHz marker on the Smith Chart should be close to the center of the Smith Chart<br>


<br>Step 7: Compare your results to the patch antenna you made during the lab session and use the lab report template to summarize the design objective, process, and results for Lab9.<br>
<b>Ans:<br>
For n = 5, g1 = 0.6180, g2 = 1.6180, g3 = 2.0000, g4 = 1.6180, g5 = 0.6180, g6 = 1.0000<br>
impedance scaling:<br>
Rs = 50, RL = 50, C1 = 0.618/50 = 0.01236, L2 = 50 * 1.618 = 80.9, C3 = 2/50 = 0.04, L4 = 80.9, C5 = 0.01236<br>
Frequency Scaling:<br>
C1' = C5' = C1/w_c = 0.01236/(2 * pi * 2.5 * 10^9) = 0.787 pF<br>
L2' = L4' = L2/w_c = 80.9/(2 * pi * 2.5 * 10^9) = 5.15 nH<br>
C3' = 0.04/(2 * pi * 2.5 * 10^9) = 2.55 pF<br><br>
The Zolver design layout and simulation results are shown in the following figures.<br></b>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/N5_MaxFlat_LPF_LC_Design.jpg)<br><br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab6/N5_MaxFlat_LPF_LC_Result.jpg)<br><br><br>





<b>Conclusion:<br>

1. Two filters are designed using the insertion loss method in this lab. One is the maximally flat LPF and another is the Equal-Ripple BSF.<br>
2. Different filter transformations are involved in the filter design. For the maximally LPF, the impedance and frequency scaling are needed. Also, the Richard's transformation and Kuroda's identities are involved to successfully implement the LPF design. On the other hand, the BSF needs one extra process from the prototype filter. The inductor should convert to an inductor parallel with a capacitor and a capacitor should convert to an inductor in series with a capacitor.
3. The lumped LC used in Task 1 step 7 only works well at low frequency. At high frequency, the distributed components are prefered.</b>
