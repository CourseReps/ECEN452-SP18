# Lab 6 Report
Mazin M Mustafa 

## Background

In this lab we will desing, simulate and fabricate LPF and BSF. The design of both LPF and BSF will be obtained using insertion loss method. Microstrip implementation of the filters will be done through filter transformation. The insertion loss method is used to control the transfer function behaviour of the filter specially in the pass-band. There are two possible ways to implement the filter: Maximally flat and Equal ripple. Each techique has advantages and disadvantages. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/equations.png) <br>
fig.1 : Equations for Insertion Loss

The LPF prototypes and implementations are basically lumped elements. This gives a possibility to implement the filter using discrete components or microstrip realization ... etc

## Design

The design of LPF starts with selecting cut-off frequency and substrate parameters. By identifying the rejection required for the filter will allow us to decide the number of elements in the filter. This can be obtained from design tables. These values give us the gk for each lumped element and this will be the initial design. The next step is to apply transformations by using Richards' transformations. Then by using Kuroda identities, a practically realizable microstrip version can be obtained. The same concept can be applied for BSF by introducing inverter, this gives a BSF filter. Similar process can be done for HPF and BPF.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/prototype.png) <br>
fig.2 : LPF prototype

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/Rich.png) <br>
fig.3 : Richards' transformation

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/kord.png) <br>
fig.4 : Kuroda identity

Substrate : FR4
er = 4.1
tand = 0.01
h = 62 mil

For LPF:
fc = 2.5 GHz
Rej = 10 dB at 3.25 GHz
maximally-flat

For LPF:
fc = 3 GHz
BW = 2.25 GHz - 3.75 GHz
Equal-ripple 0.5 dB

## Procedure

LPF:

1- Selecting the order of filter N

2- Evaluate the corresponding elements values

3- Assemble the prototypr LC ladder network

4- Applu Richards transformation

5- Apply Kuroda's identity

6- Calculate microstrip dimensions

7- Transform the desing into tapped stubs

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/eq3.png) <br>

x is the fraction of lamda

for Zo = 181 ohm => x = 0.03837

for Zo = 43  ohm => x = 0.12773

for Zo = 25  ohm => x = 0.16854

BSF:

1- Selecting the order of filter N

2- Evaluate the corresponding elements values

3- Assemble the prototypr LC ladder network

4- Applu Richards transformation

5- Apply Kuroda's identity

6- Calculate microstrip dimensions

7- Use intverters

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/eq2.png) <br>

## Results and Discussion

LPF transmision line:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/LPF1.png) <br>
fig.5 : HFSS model

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/LPF1_dB.png) <br>
fig.6 : MAG S21 dB

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/LPF1_phase.png) <br>
fig.7 : Phase S21 degree

LPF transmision line Tapped Stubs:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/LPF2.png) <br>
fig.8 : HFSS model

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/LPF2_dB.png) <br>
fig.9 : MAG S21 dB

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/LPF2_phase.png) <br>
fig.10 : Phase S21 degree

Z0lver files were developed as shown below:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/Zolv1.png) <br>
fig.11 : LPF Transmision Line

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/Zolv2.png) <br>
fig.12 : LPF Transmision Line Tapped Stubs

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/Zolver.png) <br>
fig.13 : Z0lover LPF results

BSF:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/BSF2_dB.png) <br>
fig.14 : BSF HFSS vs Milled MAG S21 dB

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/BSF2_phase.png) <br>
fig.15 : BSF HFSS vs Fabricated S21 phases

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/BSF3_dB.png) <br>
fig.16 : BSF HFSS vs Fabricated MAG S21 dB

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab6/BSF3_phase.png) <br>
fig.17 : BSF HFSS vs Fabricated S21 phases

Transmission lines values are available in the HFSS file uploaded : ECEN452_Lab6_Filters_MM_HIL_MW.hfss

## Discussion

HFSS and Z0lover simulatioins have shown results close to what expected from the design. For example the LPF cut-off frequency should be 2.5 GHz MAG S21 dB around -3 dB. Also, for rejection of 10 dB at fo = 3.25 GHz where MAG S21 dB around -10 dB.
Which is the criteria for designing the LPF in the first place. The milled LPF measured results are far away from these design requirements compared to the obtained design. Similarly for the BSF, the measured response is far away from the desired. However, the fabricated filter and HFSS were closer. S21 phases are not expected to match since it depends on the refence plans. The most important feature in the S21 phases is the linearity which is achieved. Z0lver results shouldn't be reliable because the software lacks tee model with different Zo for each side. 

## Conclusion

LPF and BSF design and simulations were performed successfully. Variation in results between milled and simulated can be discussed further more. But according to the requirements, the milled versions don't agree with requirements while the simulated versions agree.

## Hindsight

It would be better to fabricate milled versions of the filters and perform the measurements on the VNA.

## Reflection

Optimizing the HFSS design wasn't needed

## Reference

Microwave Engineering , David M Pozar


