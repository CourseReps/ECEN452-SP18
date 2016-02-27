# Assignment
The data provided in this folder is the measured S21 magnitude and phase of the Line standard of a TRL kit. Your assignment is to use this data and the TRL properties below to calculate the following.

* valid frequency range for the TRL kit (extrapolate S21 phase plot to find the frequencies where the phase is -20deg and -160deg) <br>
  f = 1.46919GHz  @ -20deg<br>
  f = 11.75353GHz @ -160deg<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab3/frequency_range.png)<br>

* effective dielectric constant of the material (use equation that relates physical length to electrical length)<br>
  e_eff = 3.10291<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab3/effective_dielectric_constant.png)<br>

* propagation velocity of the medium (use the effective dielectric constant calculated above)<br>
  v_prop = 1.7031 x 10^8 m/s<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab3/propagation_velocity.png)<br>

* attenuation coefficient in Np/m (use the magnitude at one frequency and convert dB/m to Np/m)<br>
  alpha = 0.52487 Np/m<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab3/attenuation_coefficient)<br>

## TRL Properties
Reflect Length (11 mm) <br>
Thru Length (22 mm) <br>
Line Length (28.44  mm) <br>
Line-Thru = 6.44 mm (**This is the physical length measured after the reference planes are established) <br>
Substrate thickness (62 mil) <br>

You only really need one frequency point to do this assignment. I suggest using 3 GHz since it is in the middle of the measured frequency band. The electrical length is the the negative of the phase measurement in degrees (e.g. phase = -45deg => electrical length = 45deg). Use the Line-Thru physical length in your calculations. 

Useful Equation: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab3/Equation.png) <br>
where l is a physical length, and theta is electrical length (phase) in degrees.
