# Lab 11 Report
Alonzo Barraza 

## Background
In this final lab another calibration technique was studied. For this lab free space calibration was looked and the technique that was implemented is called a Gated Reflect Line or GRL. This technique is useful for free space measurements especially for horn antennas which were used in this lab.

## Design
Since this was a lab that consisted of only studying the GRL calibration, there was no design required for this lab.

## Procedure
Due to the nature of the calibration, David walked through the steps and demoed the GRL calibration for the lab. The set up for this calibration consisted of two horn antenna facing each other with a sheet I between them. These horn antennas were dual polarized with a frequency range from 2GHz to 18GHz. The first step was complete a full two-port SOLT calibration. This was to calibrate the cables that connected to the antennas. Once the cables were calibrated then the first step of the GRL was completed. This consisted of place a sample sheet in between the antennas. The sample was Plexiglas that had a thickness of 5.6mmwhich was the same thickness of the reflect sheet. The second step was replacing the sample with the metal reflect sheet. Once the calibration was completed, the data gathered had to go through a Time-Domain Fourier transform which allows to see where the calibration needs to be gates around. 

## Results and Discussion
![Dielectric Constants](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab11/dielectric.png) <br>
![S11 TD with Refelect (pre-GRL)](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab11/s11.png) <br>
![S21 Thur (post_GRL)](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab11/s21.png) <br>
## Conclusion
It can be seen that the gated reflection happens around 3.66ns. The software that is used for the TDF helps clean up the measurement so that the effect of the GRL can be accurately studied. However with the GRL properly executed, there were some errors that could be seen. The first one is that the measurement decreased which could credited to some frequency dependencies and calibration error. One error could be that the horn antennas are not perfectly matched up but since they are broadband adjusting them has little affect. 

## Hindsight
For my own Master’s project had to look up how to perform a GRL calibration so it was helpful to have some understanding of this lab beforehand. 

## Reflection
Each of these labs were useful and well-constructed. This lab in particular was a good way to see how to calibrate for free space measurement which is an important aspect of this field of study. All of the labs provided a great learning experience for the techniques that commonly used in the lab. 