

# Lab 1 Report
Mazin M Mustafa 

## Background

In this lab we will become familiar with basic softwares and S parameters for series impedance.

## Design

There is no design

## Procedure

Python code was executed and the plot of the three datasets were generated as shown in figure 1:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/Python_code_output.png) <br>
fig.2 : Python output

For a series impedance, from symmetry & reciprocity :

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/1.png) <br>
fig.2 : Python output

And as a result of this we have:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/2.png) <br>
fig.2 : Python output


The results can be obtained from ABCE matrix as follows:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/3.png) <br>
fig.2 : Python output


By shifting the reference planes:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/4.png) <br>
fig.2 : Python output

or 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/5.png) <br>
fig.2 : Python output


![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/6.png <br>
Table.1 : Python output

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/7.png <br>
Table.2 : Python output

HFSS & Z0lver files were simulated and the results are shown below:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P2_1.png) <br>
fig.3 : Z0lver circuit

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P2_2.png) <br>
fig.4 : Z0lver circuit

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P2_3.png <br>
fig.5 : Z0lver circuit

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P2_4.png) <br>
fig.6 : Z0lver circuit

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P6_2_S11.png) <br>
fig.7 : S11 HFSS vs Z0lver vs Analytic

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab1/P6_1_S21.png) <br>
fig.8 : S21 HFSS vs Z0lver vs Analytic


## Results

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab11/Time%20Domain%20S11.png) <br>
fig.2 : Time domain S11

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab11/Frequency%20Domain%20S21.png) <br>
fig.3 : Frequency domain S21

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab11/e_prime.png) <br>
fig.4 : e' Measurements 

## Discussion

The time domain transform measures the delay for receiving the reflected wave. The peak value of S11 indicates the MUT location. After applying a time window, this removes the effects of over reflections. The reflect in a calibration standard which helps in determining the location of MUT and also de-embed the free space. Results are close what was expected. 

## Conclusion

## Hindsight

## Reflection

## Reference

[1] http://cp.literature.agilent.com/litweb/pdf/5988-9472EN.pdf 



