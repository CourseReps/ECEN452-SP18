# Assignment
The data provided in this folder is the measured S21 magnitude and phase of the Line standard of a TRL kit. Your assignment is to use this data and the TRL properties below to calculate the following.

* valid frequency range for the TRL kit (extrapolate S21 phase plot to find the frequencies where the phase is -20deg and -160deg)
* effective dielectric constant of the material (use equation that relates physical length to electrical length)
* Ans:
* lumda_g = (360/40.8388) * 6.44mm = 56.77mm 
* lumda_g = lumda_air / squreroot(dielectric_constant_effective) => dielectric_constant_effective = 3.1


* propagation velocity of the medium (use the effective dielectric constant calculated above)
* attenuation coefficient in Np/m (use the magnitude at one frequency and convert dB/m to Np/m)

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
