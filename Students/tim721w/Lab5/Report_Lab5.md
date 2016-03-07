# Lab 5 Report
Chung-Huan Huang 

## Background
In this lab, there are two tasks being simulated: TRL calibration kit and PIN diode switch. The TRL task is to design a calibration kit contains Thru-Reflect-Line microstrip line for calibrating at frequency from 1Ghz to 5Ghz with a center frequency of 3GHz. The second task is to design a PIN diode switch using quarter-wave bias tees to examine performance when diodes are both ON and OFF.

## Design
TRL design:
Calculate the physical width and length of the microstrip lines through microstrip online calculator (http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm). With parameters as er = 4.1, h = 1.5748mm, f = 3Ghz, widths can be calculatd as following: <br>
  Width for Z0(50ohm)= 3.115234375 mm <br>
  lambda/4 = 14.03649575801128 mm<br>
  er eff   = 3.1722150398472877 <br>

Therefore, TRL parameters can be implemented into HFSS and start simulating:
Reflect: Width = 3.115234375 mm 
	 length = 15 mm (provide 15mm reference plane beyond the SMA end launch connectors)
Thru: Width = 3.115234375 mm 
      Length = 30 mm (Twice length of Reflect)
Line: Width = 3.115234375 mm 
      Length = 44.03649575801128 mm (Length of Thru plus quarter-wavelength)
Since S21 phase is a slightly different from standart, thus we adjust length to 44.011456 mm

RF PIN Diode design:
Calculate the physical width and length of the microstrip lines through microstrip online calculator (http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm). With parameters as er = 4.1, h = 1.5748mm, f = 2.5Ghz, widths can be calculatd as following: <br>
  Width for Z0(50ohm)= 3.1279296875 mm <br>
  Length was given in HFSS<br>

  Width for Z0(100ohm)= 0.745513916015625 mm <br>
  Length(lambda/4) = 17.68371308266564 mm <br>

Before key in above widths and lengths into PIN diode model, we examine those parameters using SCGroundStub and SCBiasStub model for a better matching. Therefore, parameters are slightly fine-tune as following:<br>
  Length for SCGroundStub = 17.65 mm @   S11 = -47.05dB <br>
  Length for SCBiasStub = 18.08 mm @   S11 = -40.28dB <br>

Then put above lengths into PIN diode model and start simulation for both diode ON and OFF.<br>


## Procedure
TRL:<br>
	1. Calculate all parameters such as microstrip width, length and operating frequency we need in HFSS <br>
	2. De-embedding reference plane for each port<br>
	3. Simulate HFSS file and check Thru and Line phase, if not match with standard then fine-tune length<br>
	4. Extract Reflect csv file and convert it into capacitance using python file<br>

PIN diode switch:<br>
	1. Calculate all parameters such as microstrip width, length we need in HFSS <br>
	2. Simulate SCGroundStub HFSS file and fine-tune length for a better matching <br>
	3. Simulate SCBiasStub HFSS file and fine-tune length for a better matching <br>
	4. Record Step 2 and 3 parameters and put those parameters into PINSeriesSwitch model, simulate PINSeriesSwitch model for both diode ON and OFF <br>

## Results and Discussion

Task:<br>
S21 magnitude for Line<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab5/S21_Line_dB.png)<br>

S21 phase for Line<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab5/S21_Line_Phase.png)<br>

S21 magnitude for Thru<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab5/S21_Thru_dB.png)<br>

S21 phase for Thru<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab5/S21_Thru_Phase.png)<br>

TRL Capacitance<br>
Polynomial coefficients: <br>
C0 = -1.52543590008<br>
C1 = 55316.4289656<br>
C2 = -10405.6012169<br>
C3 = 582.382179152<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab5/TRL_Capacitance.png)<br>

Task2:<br>
PIN Diode Switch OFF for S11<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab5/PIN_Diode_OFF_S11.png)<br>

PIN Diode Switch ON for S11<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab5/PIN_Diode_ON_S11.png)<br>

PIN Diode Switch OFF for S21<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab5/PIN_Diode_OFF_S21.png)<br>

PIN Diode Switch ON for S21<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/tim721w/Lab5/PIN_Diode_ON_S21.png)<br>

## Conclusion
The key points for this lab is that you have to know the parameters of microstrip line such as lengths and widths. Not only plugging those parameters into simulation, but still need to fine tuning for a better matching. Through this lab, I gain more knowledge about Python and HFSS.

## Hindsight
None

## Reflection
The most difficult part of this lab is to fine tune the length for better matching. A slightly change of number may cause a huge result difference. Therefore, it's hard to choose correct number for those fine tune parameters. However, having this chance to go through whole process of designing TRL kit and PIN diode switch makes me understand more about the application of those devices. 
