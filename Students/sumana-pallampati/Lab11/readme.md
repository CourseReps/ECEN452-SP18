# Lab 11 Report
Sumana Pallampati

## Background
Free space measurement with GRL (Gated Reflect Line) callibration can be used to measure the dielectric constant of a solid with finite thickness. This callibration involves the use of time gating to obtain the reference plane of the material under test. The setup consists of two horn antennas located opposite and facing each other. They focus on the material under test which is kept in between them. In this lab, we used two dual polarized horn antennas which operate in the range of 2 GHz to 18 GHz.

## Design
There is no design involved in this lab.

## Procedure
The first step of the callibration process is to perform a SOLT callibration. This removes the effect of the coaxial cables. Then a reflect (same thickness as the material under test) is placed and the time domain waveform is obtained. By measuring the S11 in time domain, we can set the reference plane for callibration. Once we see the time at which reflection is occuring, we can place a 1 ns time gate and fourier transform it to get a flat line for S11. Then the material under test is placed in the setup and measurement is taken. In this lab, the thickness of the plexiglass sample was 5.6 mm. So we used a reflect of similar dimensions and thickness.  

## Results and Discussion
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab11/S11_TD_wReflect_preGRLcal.png) <br>
We can see from the graph that the reflect produces a maximum at 3.66 ns and thus we should place a time gate around this maximum.
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab11/S21_Thru_postGRL.png) <br>
The S21 of the thru should look like a straight line at 0 dB. But there is some discrepancy in the range of 1 - 3 GHz and this is due to the definition of the time gate.
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab11/eps_r_plot.png) <br>
The dielectric constant of plexiglass ranges from 2.6 to 3.5 which is close to the measured value range (2.5 to 3.8). The dielectric constant of air is known to be 1 and in the plot, it can be seen that it is 1. The dielectric constant of cardboard is in the range of 1.4 - 1.8. Thus, the measurement technique is fairly accurate. 

There are some inaccuracies in the callibration process and measurement. One reason can be because of a large beamwidth of the antennas used in the setup. Another reason is that the antennas are placed fairly close to the sample. 

## Conclusion
Free space measurement with GRL callibration is a good way to obtain dielectric constant of a solid. The dielectric constants of plexiglass, cardboard and air are obtained with this method and they match well with the data documented.

## Hindsight
I got a better understanding of the callibration process after the lab.

## Reflection
This is a good method of callibration and it can also be used to measure S21 of sheets or frequency selective surfaces.
