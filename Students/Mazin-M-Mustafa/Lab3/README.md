

# Lab 3 Report
Mazin M Mustafa 

## Background

In this lab we will discuss and design a TRL kit. This lab is a preparation for lab 5. The TRL calibration kit is used to shift reference planes for a circuit to avoid the effects from connectors and transmission lines. We would like to focus on the DUT. The TRL kit is hown in the next figure:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab5/TRL2.png) <br>
fig.1 : TRL calibration kit

## Design

Given the following parameters:

FR4 

er = 4.1

tand = 0.01

h = 62 mil

Zo = 50 ohm


One can derive the following equations for simple calculations: 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab3/1234.png) <br>

Using the above equations, we can conclude the follwing results:

fo = 6.611 GHz and L = 6.4 mm

- The length 

## Procedure

Python code was executed and the plot of the three datasets were generated as shown in figure 1:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/Python_code_output.png) <br>
fig.1 : Python output

For a series impedance, from symmetry & reciprocity :

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/1.png) <br>

And as a result of this we have:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/2.png) <br>


The results can be obtained from ABCE matrix as follows:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/3.png) <br>


By shifting the reference planes:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/4.png) <br>

or 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/5.png) <br>


![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/6.png) <br>
Table.1 : substrates properties

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/7.png) <br>
Table.2 : Coaxial connectors

## Results

HFSS & Z0lver files were simulated and the results are shown below:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P2_1.png) <br>
fig.3 : Z0lver circuit

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P2_2.png) <br>
fig.4 : Z0lver circuit results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P2_3.png) <br>
fig.5 : Z0lver circuit

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P2_4.png) <br>
fig.6 : Z0lver circuit results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P6_2_S11.png) <br>
fig.7 : S11 HFSS vs Z0lver vs Analytic

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P6_1_S21.png) <br>
fig.8 : S21 HFSS vs Z0lver vs Analytic

## Discussion

All tasks were performed successfully and results agree with theory.

## Conclusion

## Hindsight

## Reflection

## Reference

Agilent precision RF connector FAQ document




