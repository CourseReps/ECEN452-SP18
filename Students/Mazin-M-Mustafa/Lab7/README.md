
# Lab 7 Report
Mazin M Mustafa 

## Background

In this lab we will design a Wilkinson power divider. The theory of the power divider is well established and the design is shown in figure 1. The design frequency was choosen to be 2.5 GHz.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab7/Po.png) <br>
fig.1 : Wilkinson Power Divider


## Design

An HFSS file was simulated for the power divider

Substrate : FR4
er = 4.1
tand = 0.01
h = 62 mil
fo = 2.5 GHz

## Procedure

The procedure is to calculate the dimensions of the structure at the specified frequency. Then optimizing the results to achieve the best performance.

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
fig.15 : BSF HFSS vs Milled S21 phases

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


