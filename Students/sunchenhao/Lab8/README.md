#Lab 8 Report
Chenhao Sun

##Background

The branchline(Hybrid Coupler) the simplest type of quadrature coupler, since the circuitry is entirely planar. A ideal single-box branchline coupler is shown below. Each transmission line is a quarter wavelength. However, 3/4, 5/4 or 7/4 wavelengths (etc.) could also be used on each arm if the circuit layout requires it, the penalty is paid in decreasing bandwidth. A signal entering the top left port (port 1 in the figure) is split into two quadrature signals on the right (ports 2 and 3), with the remaining port 4 fully isolated from the input port at the center frequency. Remember that the lower output port (port 3) has the most negative transmission phase since it has the farthest path to travel.[1] <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/Hybrid%20Coupler.gif) <br>

Applications of rat-race couplers are numerous, and include mixers and phase shifters. The rat-race gets its name from its circular shape, shown below. The circumference is 1.5 wavelengths. For an equal-split rat-race coupler, the impedance of the entire ring is fixed at 1.41xZ0, or 70.7 ohms for a 50 ohm system. For an input signal Vin, the outputs at ports 2 and 4 are equal in magnitude, but 180 degrees out of phase. <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/Rat%20Race.gif) <br>

##Design
This assign is again based on FR4(4.1) with 62mil(1.57mm)thickness, working on 2.5GHz <br>
So We can calculating in online microstrio calculator, results as follow: <br>
50 Ohm line's width is 3.112 mm  <br>
QW length of 50 Ohm line is 16.88 mm <br>
0.707 * 50 Ohm line's width is 5.28 mm <br>
QW length of 0.707 * 50 Ohm line is 16.47 mm <br>

##Procedure
Calculating basic width and length of microstrip lines and apply them into HFSS file, and run. <br>
However, for Hybrid Coupler just these numbers are not good enough, because the frequency peaks are shifting to higher frequency badly. So I tune these parameters to get optimal results,Which is:<br>
Coupler_X_Length is 19 mm <br>
Coupler_Y_Length is 18.4 mm <br>
Also, Rat Race Coupler's frequency peak shift a little bit, but it can be tolerated.So I still use original parameters.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/HC_Structure.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/H_C_SP_dB.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/H_C_Phase_Difference.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/H_C_SP_PortMatching_dB.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/RR_Structure.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/R_R_SP_dB.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/R_R_SP_PortMatching_dB.png) <br>

##Results
Here are some results, compare simulation with measurement <br>
Hybrid Coupler's perfermance is as followed: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/Compare_H_C_S_P.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/Compare_H_C_Phase_Difference.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/Compare_H_C_S_P_PortMatching.png) <br>
Rat Race Coupler's perfermance is as followed: <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/Compare_R_R_S_P.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab8/Compare_R_R_S_P_PortMatching.png) <br>

##Discussion
After tuning Hybrid Coupler is basically work at 2.5GHz,S21 and S32 are both about -3.6dB, and other S parameters are both below -10 dB. And the phase differen between S21 and S31 is about 90 degree. THese both mean simulation work pretty good. <br>
And for Rat Race, although it's frequency peak shift a little, but it have good broadband perfermance, so at 2.5 GHz it still work pretty good.S21 and S31 are about -3.2dB, and other are both below -10 dB. <br>
The simulation and measurement has some difference, but can be tolerated, it's resonablt. <br>  

##Conclusion
The simulation of Hybrid Coupler and Rat Race Coupler is work fine, pretty much the same as measurement.

##Reference
[1]http://www.microwaves101.com/




