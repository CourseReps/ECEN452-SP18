
# Lab 8 Report
Mazin M Mustafa 

## Background

In this lab we will design a Rat Race and 90 degree Hybrid couplers. The theory of the two structures are well established and the design is the following figures. The design frequency was choosen to be 2.5 GHz.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab8/h.png) <br>
fig.1 : 90 degree Hybrid coupler

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab8/Ra.png) <br>
fig.2 : Rat Race coupler

## Design

An HFSS file was simulated for the structures

Substrate : FR4
er = 4.1
tand = 0.01
h = 62 mil
fo = 2.5 GHz

## Procedure

The procedure is to calculate the dimensions of the structure at the specified frequency. Then optimizing the results to achieve the best performance as shown in the following figure.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab8/ddd.png) <br>
fig.3 : 90 Hybrid coupler HFSS model

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab8/ww.png) <br>
fig.4 : Rat Race coupler HFSS model

## Results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab8/a1.png) <br>
fig.5 : 90 Hybrid coupler |S| dB

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab8/a2.png) <br>
fig.6 : 90 Hybrid coupler Phase Difference

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab8/a3.png) <br>
fig.7 : 90 Hybrid coupler RL

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab8/a4.png) <br>
fig.8 : Rat Race coupler |S| dB

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab8/a5.png) <br>
fig.9 : Rat Race coupler phase difference

## Discussion

Results are close to the simulation as expected. This process required optimizing the dimensions. One expection is the phase values for Delta. The HFSS simulations give correct results for both Felta and Sigma, where the measured resutls were correct for Sigma but not for Delta. The reason could be that S24 measurements were missing, so instead, S42 results were used.

## Conclusion

Rat Race and 90 degree Hybrid couplers designs and simulations were performed successfully. The hybrid coupler provide two options of phase shift: -90 and -180 degree which means that the output phase difference is 90 degrees. Also, the output of the coupler is divided between the two outputs eqaully. The disadvantage is a narrow bandwidth of the chybrid coupler. The rat race or ring coupler provides two options: in phase and 180 phase difference. This has different applications. Results are relatively broadband.

## Reflection

It would be better to have a document for the lab

## Reference

Microwave Engineering , David M Pozar


