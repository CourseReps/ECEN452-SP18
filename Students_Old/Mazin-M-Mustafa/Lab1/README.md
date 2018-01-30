

# Lab 1 Report
Mazin M Mustafa 

## Background

In this lab we will become familiar with basic softwares and S parameters for series impedance. This lab is just to start using the tools for this lab. Also, this lab gives an introduction to ABCD and S-parameters. Also, some review about the most common RF coaxial connectors.

## Design

There is no design

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

All tasks were performed successfully and results agree with theory. It was useful to explore Z0lver software and know about various connectors types.

## Reference

Agilent precision RF connector FAQ document



