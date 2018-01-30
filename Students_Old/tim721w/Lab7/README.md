#Lab 7 Report

Chung-Huan Huang

## Background
In this lab, Wilkinson power divider was designed and compared with simulation results. The design is based on following figure and operating frequency is set to be 2.5 GHz.<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/Wilkinson_equivalent_circuit.png) <br>

90 degree and 180 degree phase shifters are also fabricated and compared with THRU line.<br>

## Design
Using Microstrip online calculator, parameters can be easily calculated based on above figure and given substrate information (FR4). Parameters of power divider are setup as:<br>
<br>50ohm<br>
Feed line width: 3.1298828125 mm<br>
<br>70.71067ohm (square root of 2 * Z0)<br>
QW line width: 1.6767578125 mm<br>
QW line length: 17.295580370995644 mm<br>
Resistor 2*Z0  = 100 ohm<br>

Phase shifter design:<br>
THRU length: a mm <br>
90 degree length: a+14.0337 mm (add quarter wavelength to THRU length)<br>
180 degree length:a+28.0674 mm (add half wavelength to THRU length)<br>


##Procedure and Results
Simply key in above calculated parameters into HFSS file and simulate at certain frequency range. Simulated model is shown below.<br>

<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/model.png) <br>

Wilkinson power divider S parameters are shown below:<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/Wilkinson_S_dB.png) <br>

It can be seen that power splits equally to port 2 and port 3 (about -3dB by looking S21 and S31). Port 2 and port 3 are isolated at operating frequency (by looking at S32).<br>

Phase shifter S parameters are shown below:<br>
<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/phase_shifter_dB.png) <br>

<br>![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab7/phase_shifter_phase.png) <br>

It can be seen that there is no difference for THRU and THRU2. Due to error correction for unwrapping plot for 180 degree, 360 degree was deducted from 180 degree phase curve. However, 90 degree phase shifter only achieves 70 degrees phase difference and 180 degree phase shifter achieves about 140 degree phase difference. This may due to that our group measured microstrip line length from edge to edge. That makes realistic 90 degree and 180 degree phase shifter lengths are shorter than correct value.
<br>

## Discussion
The results of measurement data and simulated data are close to each other basically. However, there may be some curves such as S32(mag) are not match very well. The center frequency shifts about 1.5 GHz. This may due to that connectors may not be will implemented and microstrip line may not be fabricated as precise as simulated model.<br>

<br>Q1: The reason to include the resistor in the power divider design is to make three ports matched each other and also isolate port 2 from port 3.
<br>
<br>Q2: Width and length of microstrip line are calculated based on given substrate information. The calculation can be done using microtrip line calculator online. (http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm) 
<br>
<br>Q3: There are no much difference between THRU and THRU2 results in my group.
<br>
<br>Q4: For achieving better phase shifter, I would recalculate the phase shifter length of microstrip line from edge to edge. This will make my results more close to ideal value.
<br>
## Conclusion
Both simulation and hardware measurement of Wilkinson power divider are conducted. The results show out the correspondence of both data. 90 and 180 degree phase shifters are also present phase difference comparing with THRU phase. Although it is not the exact phase difference as what we expected, the results still on the right direction.<br>

## Hindsight
Small length variation will cause phase result turning out big different. It should be very careful when cutting copper tape.<br>

## Reflection
Fabricating using copper tape is not so easy. If there is enough time, I would prefer to do it one more time for better results.<br>
