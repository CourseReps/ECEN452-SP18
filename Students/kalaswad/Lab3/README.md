# Lab 3
The data provided in this folder is the measured S21 magnitude and phase of the Line standard of a TRL kit. I used this data and the TRL properties below to calculate the following.

* valid frequency range for the TRL kit
 * 1.511 GHz to 11.49 GHz
* effective dielectric constant of the material
 * Eeff = 3.103
* propagation velocity of the medium
 * Vp = 1.703e8 m/s
* attenuation coefficient in Np/m
 * 3.38e-3 Np/m

Plot showing data and linear regression: <br>
![image](https://github.com/kalaswad/ECEN452-Spring2016/blob/master/Students/kalaswad/Lab3/figure_1.png)

## TRL Properties
Reflect Length (11 mm) <br>
Thru Length (22 mm) <br>
Line Length (28.44  mm) <br>
Line-Thru = 6.44 mm <br>
Substrate thickness (62 mil) <br>

I used the 3 GHz frequency point for my calculations since it is in the middle of the measured frequency band. I used the Line-Thru physical length in my calculations. 

Useful Equation: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab3/Equation.png) <br>
where l is a physical length, and theta is electrical length (phase) in degrees.
