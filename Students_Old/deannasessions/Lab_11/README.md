# Lab 11 Report
Deanna Sessions

## Background
This lab was an introduction to time gated measurements using the network analyzer. The process of Gated-Reflect-Line (GRL) calibration allows for measurements to be taken using the VNA in which the analyzer only sees the time window that the sample exists within. For these purposes, two horn antennas were set up facing each other with a mounting structure oriented between them to hold the samples. The setup was then calibrated with reflecting sheet to find out exactly where the sample exists within the time of the measurement. This is most useful when doing electromagnetic testing in free space where the ambient noise of the environment would hinder the acquisition of clean data.

## Procedure
Prior to setting up the horn antennas with the VNA, an SOLT calibration must be performed on the cables that are being used. After the SOLT calibration has been performed (AND SAVED) then the GRL calibration can start. The two horn antennas are placed facing each other with a mounting structure between them. It is important that the distance between them is enough to keep the measurement in the far field for this particular method. The horns that we used function from 2-18GHz, but have roughly a 50 degree beamwidth that makes it very hard to focus the 3dB beamwidth on the sample while also keeping the horns in the far field. This could be fixed by creating a lensing structure for the horns, but this was not implemented for this lab. 

After the horns are placed, the GRL calibration is started by placing a reflecting plate (approximately the same size and thickness of the sample) within the mounting structure and viewing it within the time domain to see where the reflecting plate appears. This gives an approximate time for the VNA to calibrate around. The VNA is then switched to the GRL calibration software and the same metal plate is placed in the sample holder. The response is measured and then the plate is removed and the response is measured. After this is complete, the time gate is set up in the measurement software with the proper time and coefficients. This creates a smooth line at 0dB that is not changed by ambient noise. 

After the time gate is set up, then testing can be completed. For this lab, the dielectric of various materials were measured using the VNA dielectric software. Cardboard, Plexiglass, and air were measured and the results can be found below.
 
## Results and Discussion
Below is the S11 response in the time domain with the reflect plate in place. There is a distinct spike where the reflect plate is and this is used for calibrating the time gate.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_11/Lab11_S11_Reflect.png)<br>

Below is the S21 response of the thru after GRL calibration has taken place. The line is almost exactly on 0dB through the entire set of frequencies. The slight wavering from 0dB can be attributed to many issues, but one of the largest issues is the large beamwidth of the horn antennas.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_11/Lab11_S21_Thru.png)<br>

Below is a plot of the dielectric measurements taken with the GRL calibrated setup. Note how clean the data looks, this can be partially attributed to the added level of accuracy that GRL calibration presents.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/deannasessions/Lab_11/Lab11_dielectrics.png)<br>

## Conclusion
GRL calibrations are an innovative way to take measurements with a VNA in an electromagnetically noisy environment. This is advantageous for obvious reasons because an anechoic chamber isn't always available or necessary. The usage of time gates allows for most external signals to be filtered out while the space that holds the sample is measured allowing for a cleaner and more accurate set of data.

## Reflection
This lab is very similar to what I have been doing in the research lab during the semester so it was interesting to see the GRL calibration being used to measure dielectric properties of materials rather than the response of a frequency selective surface.
