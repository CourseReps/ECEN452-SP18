# Lab 5 Report
Sumana Pallampati

## Background
* TRL Cal Kit - </br>
TRL Calibration is more accurate than SOLT Calibration as we can set a reference plane for the DUT and thus, it removes the inaccuracies caused due to the connectors and cables. Thus, it is widely used. Another advantage of this technique is that it need not be defined completely and as accurately as the SOLT calibration in regard to the standards used in the calibration. It can be tailor made for any substrate and on a need basis. 
* PIN Diode Series Switch - </br>
The switch finds its use in broadband circuit design at high frequencies. This circuit eliminates the need of a negative voltage to reverse bias the diode. When VC1 is 5V and VC2 is 0V, the diode is forward biased and it provides a low impedance path to the RF signal. When VC1 is 0V and VC2 is 5V, the insertion loss becomes high and most of the RF signal is reflected. Thus, the diode appears as an open circuit.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%208.13.56%20PM.png)

## Design
* TRL Cal Kit - </br>
Specifications - </br>
Frequency Range - 1 GHz to 5 GHz </br>
Substrate - FR4 </br>
Relative Dielectric Constant - 4.1 </br>
Height of Substrate - 62 mils or 1.5748 mm </br>
Distance of reference plane - 15 mm </br>
</br>
Thus, we set the length of relflect to 15 mm as that is the de-embed distance of reference plane. Since the length of the thru is double the length of the reflect, we set it to 30 mm. The line has an additional quarter wavelength, so we set the length to 30 + 14.1 = 34.1 mm. The quarter wavelength is obtained at 3 GHz (design frequency). Assuming 50 ohms as the impedance of the line and using the online microstrip line calculator, we get the width of the lines to be 3.10546 mm. The effective dielectric constant is obtained to be 3.14246. Then we use the values obtained above in the HFSS design. The values have to be modified and fine tuned to achieve the desired response. We had to change the widths of the microstrip lines to 3.37 mm to get the impedance to about 50 ohms. To achieve 90 degrees for the phase response of line standard at 3 GHz, the length had to be adjusted to 43.8 mm (the quarter wavelength had to be reduced to 13.8 mm). Then we used the Im(Z) of the reflect standard and convert the reactance to capacitance and use curve fitting program in python to obtain a third order polynomial for the data. We also obtained the propagation delay of the line standard. </br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%2010.55.14%20AM.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%2010.54.41%20AM.png)
</br>
* PIN Diode Series Switch - </br>
We obtain the width of the 50 ohm line to be 3.10546 mm. The width of the 100 ohm line is calculated as 0.72338 mm. The length of the quarter wave transmission lines for bias tees are found to be 17.79 mm. Then after running the initial simulation with these values, the width of the 50 ohm line is increased to 3.2 mm to increase the impedance to 50 ohms. The width of the 100 ohm lines are not varied. But the lengths of the short circuit bias stub is adjusted to 18.15 mm and the length of short circuit ground stub is increased to 18.1 mm to minimize the insertion loss at the operating frequency.

## Procedure
In the lab, the vector network analyzer was set up to callibrate the TRL cal kit. After the calibration was performed, the S11 magnitude and phase of thru was measured. The S21 magnitude and phase response of the line standard was also measured. After the calibration was performed, the magnitude of S11 and S21 of the PIN diode series switch was measured in the ON and the OFF state by giving bias. The results of the measurement were exported and compared with HFSS simulation results.

## Results and Discussion
The plots of the measured and simulated data for TRL Cal Kit are shown below - </br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%206.17.26%20PM.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%206.22.39%20PM.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%206.18.41%20PM.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%206.24.24%20PM.png)
The plots of the measured and simulated data for PIN Diode Series Switch are shown below - </br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%2011.05.20%20AM.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%2011.11.09%20AM.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%2011.03.06%20AM.png)
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab5/Screen%20Shot%202016-03-04%20at%2011.08.26%20AM.png)

## Conclusion
It is observed that the phase of S21 of the line standard is around 90 degrees for 3 GHz and magnitude of S21 of the thru and line is around 0 dB which indicates that there minimum reflection. The phase of S21 for thru is around 0 degrees. For the PIN diode series switch, in the ON condition, it has a very low return loss (S11) and low insertion loss (S21) at 2.5 GHz indicating that the diode provides a low impedance path for the RF signal. In the OFF condition, it has a very high return loss (S11) and low insertion loss (S21) at 2.5 GHz indicating that the diode behaves like an open circuit with most of the RF power being reflected. The measured data closely follows the simulated results in both the cases. 

## Hindsight
I got a better understanding of the s parameters and how their measurement can tell us about the functioning of the device. Moreover, I also understood the use of a bias tee.

## Reflection
The most challenging part of the lab was to arrive at the optimum values for the lengths and widths of the stubs. But, after obtaining that, I got a good insight into the design process of a TRL cal kit and a PIN Diode series switch.
