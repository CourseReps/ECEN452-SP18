# Lab 11 Report
Joshua Ruff

## Background
This lab introduced the gated calibration for free space systems. A two port calibration was used in lab to measure a plexiglass panel. A Fast Fourier Transform is used to move the signal into the time dowmain, where a time gate can be applied to filter out errors. 

## Procedure
The systematic errors described in the signal flow diagram can be removed using a gated calibration. First, the two ports are calibrated in air. An absorber sheet is used as a matched load, and finally a metal sheet is used as a short circuit. 
## Results and Discussion
![Time_Domain](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab11/Time_Domain.png)<br>
The local maximum seen at 3.66 GHz appears when the reflect is placed in between the probes. This means the time gating is placed around 3-4 seconds to filter out the other noise. Once this is done, we can proceed with the calibration. 
![Thru_PostCal](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab11/Thru_PostCal.png)<br>
After the calibration is complete, S21 should show as little attenuation as possible, and other than a slight error at lower frequencies, S21 is very close to the ideal of 0 dB. 
![Permittivity](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab11/Permittivity.png)<br>
As expected, Air has a relative permittivity of one or nearly one at all frequencies tested. Cardboard's relative permittivity is slighly higher than air's, and hovers around 1.4 as frequency increases. Plexiglass has the highest dielectric constant measured of the three materials. 
## Conclusion
A two port calibration of the network analyzer was used alongside time gating to measure the properties of different materials of a fixed thickness. 
