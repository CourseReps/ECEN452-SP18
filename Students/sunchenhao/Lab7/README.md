# Lab 7 Report
   Chenhao Sun
   
## Background
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab7/wilkinson-rf-power-splitter-design.jpg)
The Wilkinson Power Divider is a specific class of power divider circuit that can achieve isolation between the output ports while maintaining a matched condition on all ports[1].<br>
The quater-wave length trasformer work as matching network connecting between Port1 and Port2 or port 3. At port1, the parallel of looking-in impedance from port2 and port3 should equal to impedance of port1(50Ohm), so they are 100 Ohm. In order to transform 50 Ohm to 100 Ohms, the QW line's Impedance is Sqrt(50 * 100)= sqrt(2) * 50 = 70.7 . The resistor is used for improving isolation between port2 and port3. It's resistance is 2*Z0 = 100 Ohm.

##Design
This assignment work on 2.5GHz, at FR4 (Er = 4.1) and Substrate's height is 63 mil(1.57mm).
So based on these infromation, we can calculate that: <br>
Z0 = 50 Ohm,  the Width of TL is 3.11mm <br>
Z0 = 70.7 Ohm, the W is 1.67mm<br>
Quater-wave length is 17.3mm<br>

##Procedure
Base on the HFSS file from github, calculating width and length, and apply the values into HFSS, then get the simulation results. Final compare these to measure results.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab7/Lab7_Structure.png) <br>

##Results 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab7/Lab7_SParameter.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab7/S11_S21_dB.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab7/S11_S21_Phase.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab7/S22_S31_dB.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab7/S22_S31_Phase.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab7/S32_S33_dB.png) <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sunchenhao/Lab7/S32_S33_Phase.png) <br>

##Discussion
Both in simulation and measurement, S21 and S31 are about -3dB, and other especially S23 and S32 are both below -10dB, which means it work properly. <br>
There are some difference between simulation and measurement, however not big and I think it can be tolerated.

##Conclusion
This wilkinson power divier work properly.
