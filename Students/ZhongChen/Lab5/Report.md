#Lab 5 Report

## Calculation and design

TRL design:
Calculate the physical width and length of the microstrip with "online mictrostrip line calculator"
Width for Z0(50 ohm) = 3.115 mm <br>
Lambda/4 = 14.036 mm <br>

Then,TRL parameters can be implemented into HFSS:
Reflect: Width = 3.115 mm	
         Length = 15 mm (Provided reference plane beyond SMA and launch connectors)
Thru: Width = 3.115 mm	
      Length = 30 mm (Twice length of reflect)
Line: Width = 3.115 mm	
      Length = 44.036 mm (Length of Thru plus quarter-wavelength)

Since S21 phase is slightly shifted from the value we want, therefore I adjust the line length to 44.011 mm.

RF PIN Diode design:
Calculate the physical width and length of the mocroship lines through "online mictrostrip line calculator"
Width for Z0(50 ohm) = 3.1279 mm <br>

Width for Z0(100 ohm) = 0.7455 mm <br>
Lambda/4 = 17.6837 mm <br>

Then,examine those parameters using SCGroundStub and SCBiasStub model for better matching before we simulate PIN Diode model with the calculated data above. Therefore, parameters are slightly tuned as following:<br>
Length for SCGroungStub = 17.65 mm <br>
Length for SCGroungStub = 18.10 mm <br>

At last,input the lengths and widths we obtain from calculation and simulation into PIN Diode model and start simulation for both ON and OFF. <br>

## Procedure
TRL:<br>
	1. Calculation all parameters such as microstrip length and width  we need for simulation in HFSS; <br>
	2. De-embedding reference plane for each port; <br>
	3. Simulate HFSS file and check Thru and Line phase,then adjust the length and width if the result is not close to the desired value; <br>
	4. Extract reflect csv file and convert it into capacitance with python; <br>
	5. Extract all csv files we need and use python to plot figures compared with measured data. <br>

RF PIN Diode Switch:<br>
	1. Calculate all parameters such as microstrip length and width we need for simulation in HFSS <br>
	2. Simulate SCGroundStub HFSS file and adjust the length for a better matching; <br>
	3. Simulate SCBiasStub HFSS file and tune the length for a better matching; <br>
	4. Put all parameters we obtain above into PIN Diode model to simulate; <br>
	5. Extract all csv files we need and use python to plot figures compared with measured data. <br>

## Results 

TRL:<br>
S21 magnitude for Line<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab5/S21_dB_line.png) (br)

S21 Phase for line <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab5/S21_Phase_line.png) (br)

S21 magnitude for Thru<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab5/S21_dB_Thru.png) (br)

S21 Phase for Thru<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab5/S21_Phase_Thru.png) (br)

TRL Capacitance <br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab5/TRL_Capacitance.png) (br)

RF Pin Diode Switch: <br>
PIN Diode Switch OFF for S11<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab5/PIN_Diode_OFF_S11.png) (br)

PIN Diode Switch OFF for S21<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab5/PIN_Diode_OFF_S21.png) (br)

PIN Diode Switch ON for S11<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab5/PIN_Diode_ON_S11.png) (br)

PIN Diode Switch ON for S21<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/ZhongChen/Lab5/PIN_Diode_ON_S21.png) (br)

## Conclusion
The simulations and the measured data compared well to one another.   

## Reflection
The most difficult part of this lab was just the fine tunning of the simulations because one small change sometimes gave different results that made sense but at other times they would not. However, once that was overcame it was rewarding to learn the beginning steps of the whole design and testing process.
