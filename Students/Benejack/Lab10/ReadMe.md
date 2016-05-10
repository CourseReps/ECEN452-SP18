# Lab 10 Report
Benjamin Jack

## Background
The coaxial probe in this lab is used to measure the dielectric constants for different materials(real and imaginary). The probe uses basic transmission line concepts to take the measurements; similar
to s-parameters and transmission and reflection coefficients. The magnitude and phase are used to calculate our desired values.

## Design
No calculations in this lab.

## Procedure
We took the coaxial dielectric probe in a very precise and stable setup and calibrated the probe with DI water. DI water has a well known dielectric curve with plateaus at high and low frequency. For
the range we were in, the dielectric constant has a smooth slope and it is easy to see if the calibration is off from the smoothness of the line and from the plateaus at either end of the frequency range.
After calibrating the probe, we carefully cleaned the probe tip and measured each of the remaining liquids, cleaning the probe each time and ensuring the setup and liquid are both stable and untouched 
between and during measurements.

## Results and Discussion

From our results it appears that the more water based fluids in our lab were the cleaning agents, which had higher dielectric constants, similar to water. The other fluids, which did not contain as much water, 
had correspondingly low dielectric constants and are much more varied depending on the chemical.

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab10/DIWatere.png)<br>

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab10/EP.png)<br>

For the general chemical dielectric constants found online, our measurements match up. 
Acetone - 20.7, DI Water - 80.1, Isopropyl Alcohol - 17.9, Ethylene Glycol - 37.0, Silicone Fluid - 2.4
The measurements from online were for the liquids at room temperature and without frequency dependence. From our plots, we can see that the silicone fluid and the acetone do not seem to have any frequency dependence, and thus our measurements line up with the measurements online. However,
for DI water, isopropyl alcohol and ethylene glycol it requires interpolation to see if our data lines up, which it does, although the ethylene glycol from our measurements looks like it would measure below 37.0 at 0 Hz. The DI water measurement I found online also seems high compared
to many other sources. 

![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/Benejack/Lab10/EPP.png)<br>

The coaxial probe is a broadband probe and can measure over a wide range of frequencies for the dielectric constant, and the accuracy is very good but not as good as a waveguide. The setup we used could be improved by a better cleaning method between the measurements and a better way to
ensure the probe sits cleanly in the fluid and does not form any bubbles as well. There do not appear to be any errors in our data other than perhaps the oscillating nature of some of the plots, but these all seem to be within a few units. 

## Conclusion
The coaxial dielectric probe is a relatively cheap, simple and effective method for measuring the dielectric constant. Even with an informal setup for the measurements, but also an expensive network analyzer, the measurements were quite accurate. The dielectric probe is a broadband and accurate
method to measure dielectric constants. It is important to ensure the liquid the probe is immersed in has a large enough volume to hold the fringing field from the probe in order to maintain accurate measurements.

## Hindsight
My knowledge of the complex dielectric constants before the lab was very limited, and my understanding now is at least marginally better. It is difficult to see the application sometimes when different material properties lead to different uses
which are only seen in the end product.

#Sources
Sources for the dielectric constants:
http://depts.washington.edu/eooptic/linkfiles/dielectric_chart%5B1%5D.pdf
http://www.engineeringtoolbox.com/liquid-dielectric-constants-d_1263.html
http://www.clearcoproducts.com/pdf/pure-silicone/Dielectric_Properties_Pure_Silicone_Fluids.pdf


