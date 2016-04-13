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
The optimum simulation results of the patch antenna is when patch_length = 23.85 mm and patch_width = 24 mm. Similarly, the feeding probe has a 7.225 mm distance (probe_feed_x = 4.7 mm) away from the edge of the patch surface. The HFSS design parameters are provided as the figure together with the design layout.<br><br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab9/patch_hfss_design_parameters.png)<br><br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab9/patch_hfss.png)<br><br>

The patch has VSWR of 1.0552 at 3 GHz and has a bandwidth of 84.4 MHz (2.9576GHz to 3.0420 GHz). As a result, the patch has the best impedance matching to the 50 Ohm at 3 GHz. The results achieve the requirement of VSWR below 1.2.<br><br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab9/patch_hfss_vswr.png)<br><br>
</b>



<br>Step 5: Look at the Smith Chart to check the impedance match of the antenna. Use your notes from class to determine whether to move the probe closer to the center or closer to the edge of the patch. Adjust probe_feed_x accordingly and rerun your simulation.<br>
<b>Ans:<br>
As mentioned above, when probe_feed_x = 4.7 mm comes the best impedance matching results. The Smith chart illustrated the resonant frequency is around 3 GHz and the normalized input impedance is 1.0389 - 0.0386j. The imaginary part of the impedance is very small which prove the resonance of the patch.<br><br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab9/patch_hfss_smith_chart.png)<br><br>
</b>






<br>Step 6: Repeat steps 4 and 5 and keep adjusting until the design is impedance matched at 3GHz. You should see a VSWR minimum at 3GHz (±50MHz); try to get the value at 3GHz below 1.2. The 3GHz marker on the Smith Chart should be close to the center of the Smith Chart<br>


<br>Step 7: Compare your results to the patch antenna you made during the lab session and use the lab report template to summarize the design objective, process, and results for Lab9.<br>
<b>Ans:<br>

The patch with width = 31.31 mm and height = 24.29 mm fabricated on FR4 using the copper tape has VSWR = 2.50. Then the original patch using the stub tuning method to do the impedance matching work. Finally, a VSWR of 1.29 is derived.<br>

The measured results of the matched and unmatched are used to compare with the HFSS simulation data. The plot is provided below to make a comparison.<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/StevenYeh/Lab9/patch_vswr_comparison.png)<br><br>
</b>





<b>Conclusion:<br>

1. The patch becomes resonant (imaginary part of the impedance is 0) when the length of the patch is around 0.49*Lumda_g.<br>

2. In this work, the patch is built on FR4 which has a dielectric constant of 4.1. In general, FR4 is good for the traditional electronic circuit design but may not efficient for the patch antenna to radiate. Besides, it has high loss when the operating frequency over GHz. It's suggest to use other kinds of substrate to replace the FR4 such as the Duroid 5880 (εr=2.2) to get a better radiation characteristics.<br>

3. The input impedance of the patch will increase when the feeding probe is close to the edge of the patch surface. We define the probe distance from the patch edge as Δx. In this experiment, when Δx = 5.655 mm, we observed input impedance = 42.105 - 39.205j (Ohm). When Δx = 7.655 mm, we have input impedance = 32.46 - 27.715j (Ohm). When Δx = 10.655 mm, we have input impedance = 13.67 - 4.51j (Ohm). As a result, if Δx increase, the input impedance of the patch will decrease. We use this phenomenon to do the impedance matching job.</b>
