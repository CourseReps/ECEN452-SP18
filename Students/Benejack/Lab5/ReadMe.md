# Lab 5 Report
Benjamin Jack
##Task 1
Data:
Zo = 50 ohms, 62 mil thick, FR4, f[1,5] GHz, 15mm ref. plane

## Background
Breifly explain what the device does and what it is used for. This section does not need to be a long paragraph and does not need to be very technical.

I first used the online microstrip calculator to calculate physical widths and lengths for a 50 ohm transmission line.
Next, I found the wavelength, effective dielectric constant and lengths for the TRL calibration.
I simulated all three of the files in HFSS and exported the data after de-embedding. The data came out at -92 degrees phase at 3 GHz for the Line standard
and I changed the length but I did not see the phase get closer to -90 degrees. I would have changed the width, but the lab manual did not say whether to modify
the width and I could not find the impedance of the line calculated in HFSS. 

Use S-param...
Check back with graphs...

I used MATLAB to import the data from the Reflect standard and generated a 3rd order polynomial with coefficients... to generate the polynomial fit for the capacitance
which I converted from reactance by... EQUATION

I did not see any significant differences in the measured in simulated data for task 1 as the measurements where all on such a small scale.

Mag S21 Line: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/S21_Line_Mag.png)<br>

Phase S21 Line: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/S21_Line_Phase.png) <br>

Mag S21 Thru: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/S21_Thru_Mag.png) <br>

Phase S21 Thru: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/S21_Thru_Phase.png)<br>


##Task 2
Data:
Zo = 50 ohms, 62 mil thick, FR4, f[1,5] GHz, 15mm ref. plane

Mag S21 Thru: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/PIN_On.png)<br>

Phase S21 Thru: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/PIN_Off.png)<br>


Use the exported data to plot the measured TRL data against the HFSS simulation data

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
