#Lab 9 Report

Chung-Huan Huang

## Background
In this lab, patch antenna were designed in HFSS (coaxial feeding) and compared with copper tape on an FR4 substrate. The design is based on following figure and operating frequency is set to be 3 GHz.
<br>

## Design
Using formulas in Lab9 instruction (below), parameters can be easily calculated based on given information below:<br>

<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab9/formula.png) <br>

Frequency: 3 GHz<br>
Dielectric constant: 4.1<br>
Thickness of substrate (H): 1.5748 mm<br>
Characteristic impedance: 50 ohm <br>

Therefore, we get <br>
Effective dielectric constant: 3.774 <br>
Patch_length: 24.27 mm <br>
Patch_width: 31.31 mm<br>
Input impedance at edge: 229.5 ohm<br>
d: 8.83 mm <mm>

<br>Fabricated patch antenna with single stub<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab9/patch_antenna_single_stub_matching.png) <br>

In order to get a better simulated results, optimization is done and values are: <br>
Patch_length: 23.7 mm<br>
Probe_feed_x: 5.8 mm<br>

<br>HFSS patch antenna model<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab9/HFSS_patch_antenna.png) <br>

##Procedure and Results
Simply use physical width and length of patch antenna calculated above and implemented on FR4 substrate using copper tape with feed line length of 40 mm. The characteristic impedance was setup up as 50 ohm. The VSWR measurement of copper taped patch antenna can be acquired about 2.579 and the impedance is about 73+j54 ohm at frequency 3.092 GHz. It・s easy to see that it・s not match so well with such VSWR value. Therefore, a stub was added to match the impedance to 50 ohm. By using Smith Chart, stub length was found as 0.121 effective wavelength (6.793 mm) and the position of the stub was 0.102 effective wavelength (5.727 mm) toward antenna from reference plane. Adding copper stub on the previous hardware and connected with network analyzer to measure the VSWR. The result shows out that VSWR is around 1.124 at 3.098 GHz. It・s obvious to see that VSWR decreases down below than 2 and can be regarded as well-matched.
<br>

<br>VSWR plot for fabricated patch antenna<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab9/fabricated_VSWR.png) <br>

For HFSS simulation, simply key in above calculated parameters into HFSS file and simulate at certain frequency range. Make sure VSWR curve got minimum value at 3 GHz. By looking at Smith Chart, using notes in class to determine best probe position until VSWR value below 1.2 at 3GHz. It・s found out that optimized VSWR of 1.07 can be achieved at 3 GHz.
<br>
<br>VSWR plot for simulated patch antenna<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab9/HFSS_patch_antenna_VSWR.png) <br>

<br>Smith plot for simulated patch antenna<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab9/HFSS_patch_antenna_smith.png) <br>

## Discussion
It can be seen that adding stub on the feeding line decreases VSWR value from 2.579 down to 1.124 in this lab. This tells us that a well-matched microstrip line is pretty important. However, we design this patch antenna at frequency of 3 GHz and the fabricated result came out that operating frequency shifts a little bit higher to 3.1 GHz. This may due to that the fabricated antenna is made by copper tape which will lead to human error.
<br>

## Conclusion
Both fabricated and simulated results show that patch antenna matching can be achieved by adding stub and putting correct feeding position. With VSWR of lower than 1.2 presents the whole circuit is acceptable and well-matching.
<br> 

## Hindsight
Feeding line position can be calculated advance in order to save time on position sweeping in simulation.<br>

## Reflection
This lab is pretty straightforward and not so difficult. With class notes, it・s easy for us to apply theorem into experiment and simulation, making the learning more effective.
<br>