

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

Given the following data:

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab3/S211.png) <br>
fig.2 : S21 dB Line

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab3/S212.png) <br>
fig.3 : S21 Phase Line

One can derive the following equations for simple calculations: 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Mazin-M-Mustafa/Lab3/1234.png) <br>

Using the above equations, we can conclude the follwing results:

fo = 6.611 GHz and l = 6.4 mm

- The length of l is 6.4 mm from calculations
- Similiarly fL = 1.47 GHz and fH = 11.75 GHz
- Now, considering the calculations fro fo = 6.611 GHz
- w = 3.17 mm , e_eff = 3.14 , lamda_o = 5.645 cm, l = lamda/4 = 6.4 mm
- Also, the attenuation is estimated to be 0.57 dB/cm
- Assuming sigma = 5.8e7 siemens/m and metal thickness t = 0.001 cm
- Comparing the previous results with proided information

L = 11 mm and Line = 28.44 mm

We can finally find l = Line-THRU = 28.44 - 2x11 = 6.44 mm and w = 3.07 mm

whcih agrees

## Procedure

There is no procedure

## Results

L = 11 mm 

l = Line-THRU = 28.44 - 2x11 = 6.44 mm

w = 3.07 mm

## Discussion

All tasks were performed successfully and results agree with theory.

## Conclusion

## Hindsight

## Reflection

## Reference

"Microwave Transistor Amplifiers", Gonzalez




