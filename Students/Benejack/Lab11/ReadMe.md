# Lab 11 Report
Benjamin Jack

## Background
Free space material measurements are used to measure the complex permittivity and permeability of materials. In particuler, we can measure these values by examining the air/material interface on a slab. The GRL(gated, reflect, line)
 calibration is important so we get an accurate measurement of our material under test. We can use two antennas to take this measurement in the time domain and convert to the frequency domain or vice versa. A one port measurement can
 be used, but it is easier to do a two port measurement as it is less prone to error and noise.

## Procedure
First in lab we performed a GRL calibration with the two horn antennas. The metal plate serves as the reflect standard and has the same thickness as our material under test. We also used gating to narrow the time domain width to show the portion
of the curve which we wanted to see - where the material is located. After the calibration, we used the same setup and approximately same thickness materials to measure the permittivity of different materials.

## Results and Discussion

This plot has a mistake - the Y axis should be the dielectric constant, not the magnitude in dB. Air should have a dielectric constant of 1 and it also makes sense that cardboard is between plexiglass and air because cardboard has air pockets within
it and plexiglass is a solid material.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab11/epmeas.png)<br>

The peak in the S11 graph showing reflection shows the highest reflection at 3.66ns - the location of the reflect standard metal sheet.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab11/S11.png)<br>

The S21 measurement shows that around 3GHz, we do not have any loss across the airspace we calibrated for in the GRL calibration.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab11/S21.png)<br>

Include measured/simulated Plots here. All plots are to be made in Python by modifying the csv plotter code. Explain how you can tell the device is working by examining the data (S-parameters). Comment on any differences between the measured and simulated results and sources of error.

## Conclusion
The calibration is key to this method working correctly, so it is important to have consistency in between measurements and ensure that all measurements are taken carefully and in approximately the same manner. Each material tested should be perpendicular to the
antennas, at the same distance away, with the same thickness, and not moving during the calibration or measurement. This measurement technique requires more care than the coaxial probe test does and is more difficult to discern errors.

## Hindsight
For our measurements, the biggest improvement area would be the method for holding the materials. The materials we were testing did not always stay exactly upright. Also, the material thicknesses were not entirely precise, but this was less of an issue than the materials staying upright.

## Reflection
The mathematical theory behind this calibration and measurement is pretty intense and hard to grasp.