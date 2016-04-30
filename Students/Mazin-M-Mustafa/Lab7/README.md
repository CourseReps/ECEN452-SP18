
# Lab 7 Report
Mazin M Mustafa 

## Background

In this lab we will design a Wilkinson power divider. The theory of the power divider is well established and the design is shown in figure 1. The design frequency was choosen to be 2.5 GHz.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab7/Po.png) <br>
fig.1 : Wilkinson Power Divider

We Also fabricated and measured a phase shifter. It was a transmission line phased shifter as shown below.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab7/PS.png) <br>
fig.2 : Transmission line phase shifter

## Design

An HFSS file was simulated for the power divider

Substrate : FR4
er = 4.1
tand = 0.01
h = 62 mil
fo = 2.5 GHz

## Procedure

The procedure is to calculate the dimensions of the structure at the specified frequency. Then optimizing the results to achieve the best performance as shown in the following figure.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab7/W1.png) <br>
fig.3 : HFSS model

## Results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab7/vvvvv.png) <br>
fig.4 : HFSS Vs Measured results

## Discussion

Results are close to the simulation but not exact. This depends on the many factors during the design, the fabrication or the measurement. 

## Conclusion

Wilkinson pwoer divider design and simulations were performed successfully. The phase shifter didn't work properly. Wilkinson power dividers are useful to built phased arrays and other applications in RF. The advantage of this power divider is that it is broadband.

## Reflection

It would be better to have a document for the lab

## Reference

Microwave Engineering , David M Pozar


