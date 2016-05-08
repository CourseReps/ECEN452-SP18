# Lab 11 Report
Abhay Shankar Anand

## Background
Lab 11 consists of Dielectric Measurements of solids using Free Space Measurements

Dielectric measurements use the basic concept of Reflection and Transmission obtained from S-parameters. As the MUT is placed in free space at some distance from the antennas, we use a concept called time gating where we identify the MUT's location with respect to time.

## Design
* Fields from antenna at port 1 pass through the MUT and are received at antenna connected to port 2.
* To avoid non-Line-of-Sight paths, the base of the entire setup is paded with EM absorbers.
* The MUT must be latge enough to receive all of the radiations from the antenna ane be placed at the far field of it too.

### Procedure

1. Calibrate both the ports of the VNA using 2-port SOLT calibration.
2. Using in-built functions in the VNA, convert the frequency domain S11 into time domain S11 (Inverse Fourier Transform).<br>
Here, we observe a peak at time = 0. This implies that at the origin of the antenna, there is maximum reflection (which is true).
3. With this plot running in the VNA, place the metal plate in the MUT stand.<br>
We observe a new peak forming at 3.66 ns. This means that a new reflection is observed at a location corresponding to 3.66 ns away from the antenna.
4. This is the time that we use for time-gating. Time gating is a concept of filtering in the time-domain. We ignore all reflection data outside the 3.66 ns region to improve the frequency characteristics (make it less noisy, in a sense).
5. Once the time-gating data has been entered, we change back to frequency domain and perform calibrations.
6. Different MUTs are placed in the MUT stand and  &#949;' is calculated for each using the add-on software provided by Agilent.

### Sources of Error

There are three main sources of errors that could affect the measurememts:

1. Antenna performance: The antennas to be used must be designed to the frequency sweep of the test setup. The antenna we used had a frequency range starting from 2 GHz while our measurement setup started from 1 GHz. This gave unreliable results below 2 GHz.
2. MUT stand: The MUT stand must be placed at the center of both the antennas and must be large enough to support the MUT that covers almost all of the antenna radiations.
3. Reflections: There can be unwanted reflections that might result in wave reflections reaching both the antennas. This must be minimized as much as possible.

### Results
![S11PreCalib](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab11/results/S11PreCalibTimeDomain.png)

![S21PostCalib](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab11/results/S21PostCalib.png)<br>
After calibration, and using antennas designed for the given frequency sweep, the S21 should be ideally 0 dB.

![DielectricConstants](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/abhaysanand/Lab11/results/DielectricConstants.png)

### Questions
1. **What does it mean to transform into the time domain?**<br>
Transforming to time-domain shows the wave propagation with respect to time. Much like the plot of a sine wave against time.
2. **How do you interpret the S11 data in time domain?**<br>
It shows the S11 parameter in terms of time. As in, the reflection caused at a particular time with wave propagation due to obstacles in free space.
3. **How does looking at the time domain help with the calibration?**<br>
We can exactly spot the location of the metal sheet and apply a time gating around that time.
4. **What are we looking for when we put the reflect in before performing the calibration?**<br>
We are looking for a peak in S11 that occurs due to the metal sheet. This peak indicates the reflection caused due to the metal sheet.
5. **How do the three materials measured compare to expectations?**<br>
* &#949;' of Air is 1 which is what we obtain for frequencies > 2 GHz. 
* &#949;' of Plexiglass about 2.3 to 3.5. We obtain values in the range 2.5 to 3.8 which is pretty close.
* Paper has a dielectric constant of 2.3. Assuming that thickened paper with air gaps in between would reduce &#949;' further, we can say it would be around 1.5, which is what we get.

## Conclusion
Very accurate dielectric measurememts were possible using Gated Reflect Line Dielectric measurements

## Hindsight
The concept of time gating was really interesting and the use of time-frequency domain transformations was new to me in the field of electromagnetics.
