#Lab 7 Report

Chung-Huan Huang

## Background
In this lab, Wilkinson power divider was designed and compared with simulation results. The design is based on following figure and operating frequency is set to be 2.5 GHz.<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/Wilkinson_equivalent_circuit.png)<br>

## Design
Using Microstrip online calculator, parameters can be easily calculated based on above figure and given substrate information (FR4). Parameters of power divider are setup as:<br>
<br>50ohm<br>
Feed line width: 3.1298828125 mm<br>
<br>70.71067ohm (¡Ô2Z0)<br>
QW line width: 1.6767578125 mm<br>
QW line length: 17.295580370995644 mm<br>
Resistor 2*Z0  = 100 ohm<br>

##Procedure and Results
Simply key in above calculated parameters into HFSS file and simulate at certain frequency range. Simulated model is shown below.<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/model.png)<br>

S parameters are shown below:<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/Wilkinson_S_dB.png)<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/Wilkinson_S_dB.png)<br>

<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/Wilkinson_S_phase.png)<br>

## Discussion
The results of measurement data and simulated data are close to each other basically. However, there may be some curves such as S32(mag) are not match very well. The center frequency shifts about 1.5 GHz. This may due to that connectors may not be will implemented and microstrip line may not be fabricated as precise as simulated model.<br>

## Conclusion
Both simulation and hardware measurement of Wilkinson power divider are conducted. The results show out the correspondence of both data.<br>

## Hindsight
None<br>

## Reflection
If possible, it¡¦s better to have a lab instruction document. That would make me more clearly to understand what to do for the lab.<br>
