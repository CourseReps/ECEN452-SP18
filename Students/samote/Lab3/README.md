## Samuel Mote
## ECEN 452 Lab #3

Properties: <br>
lref = 11 E-3 m <br>
lthru = 22 E-3 m / lline = 28.44 E-3 m ==> ?lTL = 6.44 E-3 m <br>
thickness = 62 E-3 m <br>

1. Valid Frequency Range: <br>
@ 1.5 GHz, ?1 = -20.154594° <br>
@ 4.5 GHz, ?2 = -62.111099° <br>
?? = -41.956505° <br>
Slope = ??/?f ==> m = -41.956505°/3 GHz ==> m = -13.9855°/GHz <br>
-160 + 62.1 = -13.9855(fmax - 4.5) ==> fmax = 11.5 GHz <br>
-20 + 62.1 = -13.9855(fmin - 4.5) ==> fmin = 1.4897 GHz <br>
1.4897 GHz < f < 11.5 GHz  <br>

2. Dielectric Constant: <br>
@ 3 GHz, ?1 = -40.838772° <br>
l= (c/(fv?))(?/360) ==> 6.44 E-3 = ((3 E8)/(3 E9 v?))(40.838772/360) ==> eeff = 3.103 <br>

3. Propagation Velocity: <br>
v = c/v? ==> v = (3 E9)/v3.103  ==> v = 1.7 E8 m/s <br>

4. Attenuation Coefficient: <br>
1 Np = 8.686 dB <br>
@ 3 GHz, dB = 0.029361164 <br>
a = dB/(m(8.686)) ==> a = 0.029361164/((6.44 E-3)(8.686)) ==> a = 0.5249 Np/m <br>




# Assignment
The data provided in this folder is the measured S21 magnitude and phase of the Line standard of a TRL kit. Your assignment is to use this data and the TRL properties below to calculate the following.

* valid frequency range for the TRL kit (extrapolate S21 phase plot to find the frequencies where the phase is -20deg and -160deg)
* effective dielectric constant of the material (use equation that relates physical length to electrical length)
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
