# Lab 5 Report
Benjamin Jack

## Background
The TRL kit is a kit designed to calibrate the VNA so we can ensure later measurements on devices with the same characteristic impedance line, but more complex designs
are accurate. The PIN diode switch allows us to take a signal and tune our circuit to pass the frequency we desire and also control whether any signal passes at all by
biasing the diode with a DC bias voltage.

## Design
*Data:
Zo = 50 ohms, 62 mil thick, FR4, f[1,5] GHz, 15mm ref. plane
*Task 1
In task one, I used the online microstrip calculator to calculate the values for the TRL kit: the width to give a 50 ohm characteristic impedance line, and the length
of a quarter wavelength section to append to the Line standard. The microstrip line width was 3.09mm and the line lengths (TRL) were 15mm, 30mm, and 40.07mm respectively.
I simulated all three of the files in HFSS and exported the data after de-embedding. The data came out at -92 degrees phase at 3 GHz for the Line standard
and I changed the length but I did not see the phase get closer to -90 degrees. I would have changed the width, but the lab manual did not say whether to modify
the width and I could not find the impedance of the line calculated in HFSS. 

*Task 2
For task two, I used the online microstrip calculator again to calculate the stub width and length to give a characteristic impedance of 100 ohms. I simulated the first 
file, isolating a single stub, and adjusted the length of the stub slightly to get the correct operating frequency lowered down to 2.5 GHz. My original calculations yielded a stub
length of 18.8 mm, but after simulation, I realized I needed to shorten the length to 18.1 mm. The stub was tuned to too low of a frequency, and because of the inverse relationship
between frequency and wavelength, in order to get a higher target frequency, I needed to decrease the stub length.

## Procedure
In lab we measured the S21 phase and magnitude for each of the standards of the TRL kit using the VNA. We also used the VNA to measure the magnitude response of the pin diode circuit
for the S11 and S21 parameters.

## Results and Discussion

I did not see any significant differences in the measured in simulated data for task 1 as the measurements where all on such a small scale.

I used MATLAB to import the data from the Reflect standard and generated a 3rd order polynomial to generate the polynomial fit for the capacitance
which I converted from reactance by C = (1/2*pi*f*Reactance)

Polynomial Fit Capacitance: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/Cap.png)<br>

Mag S21 Line: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/S21_Line_Mag.png)<br>

Phase S21 Line: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/S21_Line_Phase.png) <br>

Mag S21 Thru: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/S21_Thru_Mag.png) <br>

Phase S21 Thru: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/S21_Thru_Phase.png)<br>

Mag S21 Thru: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/PIN_On.png)<br>

Phase S21 Thru: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab5/PIN_Off.png)<br>
<<<<<<< Updated upstream
=======

## Conclusion
It is important to remember the precision of the TRL kit because calibration is critical for more complex designs. The
pin diode allows us to pass through our signal not only at a certain frequency, but also with a controlled on/off switch
based off of a DC voltage biasing the diode. The S-parameters, which are easy to measure, allow us to easily evaluate whether
our design is working.

## Hindsight
Comment on anything you know now, having completed the lab, that you wish you knew at the beginning of the lab.
The VNA and HFSS output data in Hz and GHz respectively and that took a bit to figure out why my plotting was not working for my python plots because my x-axis scaling was off.
I also wish I had known \b is a special character in python... but that's another story.

## Reflection
It was challenging to setup the lab simulations, software, formatting and so forth and truly understanding the theory behind even the simple portions of this first lab
was difficult, but it was rewarding to get a more tangible feel for what we are learning means and how it applies to producing something for an end goal.
>>>>>>> Stashed changes
