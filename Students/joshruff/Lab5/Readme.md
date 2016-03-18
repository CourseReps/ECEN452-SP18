Lab 5 Report
Joshua Ruff

## Background
The TRL kit is used to calibrate a network analyzer in situations where an Open Short Load Calibration would be Less accurate. 

The PIN Diode can be used in a switching circuit such as a Bias Tee to control the flow of RF Signals. 
## Design
TRL Kit: 
![Parameters](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab5/TRL_Data/TRL_Calcs.png)<br>
The Reflect was taken to be the length of the reference plane, the Thru was double the length of the reflect, and the Line was a quarter wave length longer than the Thru. All of these were built on 50 Ohm line. 

PIN Diode: 
![Calculations](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab5/PIN_Data/PIN_Calcs.png)<br>
The width of the 100 Ohm Chokes was calculated, as well as the quarter wavelength at the design frequency. 

## Procedure
We calculated the major parameters for our TRL Kit and PIN Diode Switch, and simulated these devices with HFSS. We then Compared the simulated data to the measured results from David's prototypes. If any significant improvements could be made, the designs were adjusted during the simulation phase. 

'
## Results and Discussion
###TRL Kit
Line Magnitude and Phase: 
![Line S21 dB](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab5/TRL_Data/Line_S21_Magnitude.png) <br>
![Line S21 Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab5/TRL_Data/Line_S21_Phase.png)<br>
The design goals for the line were to have minimal attenuation and 90 degrees of phase shift at the design frequency, whicih is verified by this graph. 


Thru Magnitude and Phase
![Thru S21 dB](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab5/TRL_Data/Thru_S21_dB.png)<br>
![Thru S21 Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab5/TRL_Data/Thru_S21_Phase.png)<br>
The Thru segment had zero loss at the design frequency, as well as zero phase at the design frequency. 

Capacitance Polynomial Fit: 

![Capacitance](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab5/TRL_Data/Capacitance_Fit.png)<br>
The polynomial fit of the capacitance data shows a fairly close match to the capacitance curve in this graph. 

###PIN Diode 

![PIN S11](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab5/PIN_Data/PIN_Diode_S11.png)<br>
This graph compares the magnitude of the reflected signal from the pin diode circuit in both the ON and OFF states. The measured signal level took on approximately the same shape as the simulated signal, with some minor differences. In the OFF state, almost the entire signal is reflected back into the input ports. Additionally, there is a noticable resonance at 4.3 GHz where signal passes through the circuit. This is likely due to the quarter-wave chokes becoming closer to half-wave as the frequency doubles. This inverts the filter behavior and allows signal to pass through at these frequencies. In the ON state, the reflected signal is heavily attenuated in and around the design frequency of 2.5 GHz. Also, the reflection strength reached a minimum slightly below the design frequency, because... 


![PIN S21](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/joshruff/Lab5/PIN_Data/PIN_Diode_S21.png)<br>
This graph shows the signal passed through the pin diode circuit. As expected, for the most part it shows the opposite behavior of the S11 graph. When the diode is in the ON state, hardly any of the signal is attenuated. However, when the diode is in the off state, the signal passed through at the design frequency is attenuated. Again, there are resonances experienced at around double the design frequency. These are similar in nature to the ones on the S11 Graph, with the quarter-wave lengths approaching half-wave behavior at double the design frequency. 


## Conclusion
The TRL kit was designed to calibrate the Network Analyzer for 62 mil FR4 which will be used in designs throughout the semester. The graphs for both the simulated and measured Magnitude and phase matched the desired design characteristics for the TRL kit. The PIN diode also behaved as designed: it attenuated the transmitted signal in the OFF state, and let the transmitted signal through in the ON state. 

