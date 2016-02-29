# Lab 3 Report
Abhay Shankar Anand

### Frequency Range for TRL Kit (-20&#176; and -160&#176;)
Frequency range was calculated by extrapolating the Phase CSV data using Python. The calculated values are:<br>
![freqRange](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab3/results/freqRange.jpg)

### Effective Dielectric Constant &#949;<sub>eff</sub>
Using the equation:<br>
![equation](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab3/results/Equation.png)

We know, <br>
*l* = 6.44 mm <br>
&#952; = -40.84&#176; <br>
*c* = 3 x 10<sup>8</sup> m/s <br>
*f* = 3 GHz <br>

Substituting all these values, we get,<br>
**&#949;<sub>eff</sub> = 3.103**

### Propagation Velocity of the Medium
The propagation velocity is the speed of light (*c*) scaled by 1 / &#8730;&#949;<sub>eff</sub><br>
__*v* = 1.703 x 10<sup>8</sup> m/s__

### Attenuation Constant
|S21| at 3 GHz = -0.02936 dB = 3.3802 x 10<sup>-3</sup> Np <br>
*l* = 6.44 mm <br>
&#945; = |S21| / *l* <br>
**&#945; = 0.5249 Np/m**

## TRL Properties
Reflect Length (11 mm) <br>
Thru Length (22 mm) <br>
Line Length (28.44  mm) <br>
Line-Thru = 6.44 mm (**This is the physical length measured after the reference planes are established) <br>
Substrate thickness (62 mil) <br>
