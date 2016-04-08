

# Lab 9 Report
Mazin M Mustafa 

## Background

In this lab we will design and simulate a patch antenna as shown in figure 1. Also, we will macth the antenna to 50 ohm transmission line. The design of patch atnenna can be done using the follwoing equations.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab9/p1.png) <br>
fig.1 : Patch Antenna

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab9/eqt.png) <br>
fig.2 : Equations

## Design

For FR4 substrate :
er = 4.1
fo = 3 GHz
h = 62 mil

The calculated resutls using the previously mentioned equations:

L = 24.27 mm
W = 31.31 mm
x = 8.94 mm

## Procedure

The desing was done in two steps: desinging the patch antenna and then perform the impedance matching. The first step is shown in figure 3. In this step we only consider the resonance frequency for the patch antenna. From theory, the input impedance wi;; be much larger than 50 ohm. Witch requires impedance matching. Measured results are shown in figure 4.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab9/antenna1.png) <br>
fig.3 : Unmatched patch antenna

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab9/unmatched.png) <br>
fig.4 : VSWR for unmatched patch antenna

The next step in to measure the input impedance and then use single stub to match the antenna to 50 ohm line as shown in figure 5. The corresponding results are shown in figure 6

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab9/antenna2.png) <br>
fig.5 : Matched patch antenna

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab9/matched.png) <br>
fig.6 : VSWR for matched patch antenna

The obtained Zin = 133 + j22 ohms
The stub matching required:
d = 0.152 lamda = 7.23 mm (moving towards the load)
l = 0.128 lamda = 8.59 mm (stub length)

HFSS model

In this step we will simulate an HFSS model for the same patch antenna using probe feed as shown in figure 7. In this design there is no need for matching network. Instead, we can determine the location to feed the antenna directly where the input impedance is equal to Zo as described in the equations. Then by optimizing the the simulation model we can obtain the best results as shown in figures 9 and 10.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab9/hfss.png) <br>
fig.7 : HFSS probe fed patch antenna

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab9/VSWRHFSS.png) <br>
fig.9 : VSWR results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab9/smith.png) <br>
fig.10 : S11 smith chart

## Discussion

Both the measured and simulated model results were close enough to what was expected. The main focus is to reduce the VSWR at the resonance frequency. VSWR around 1.1 was obtained from the fabricated antenna. Where VSWR from HFSS was  with more accurate resonant frequency.

## Conclusion

Patch antenna was fabricated and simulated successfully.

## Hindsight

## Reflection

## Reference

Antenna Theory: Analysis and Design , Constantine A. Balanis


