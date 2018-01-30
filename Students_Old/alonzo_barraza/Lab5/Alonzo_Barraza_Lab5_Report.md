# Lab 5 Report
Alonzo Barraza 

## Background
In this lab there were two device that were simulated and tested. The first device was a TRL calibration kit that was meant to calibrate for a frequncy range from 1GHz to 5Ghz with the ceneter frequency being at 3GHz. The second device was a PIN diode switch that contained two short circuit choke lines. One was connected to ground and the other was a bias T-Line. This device operated in two modes which were the "ON" and "OFF" stage.

## Design
In order to simulate an accruate deisgn, the free online microstrip calculator was used to find the widths and lengths. For the TRL kit the parameters that were put into the calculator was a h = 1.5748mm, er = 4.1, f = 3000MHz (3GHz), and Z0 = 50ohms. The width was calculated to be 3.09mm and the quater-wave length was equal to 14.07mm. With these values the widths and lengths for the thru, reflect, and line could be implemented into the HFSS designs. Since there was a deembed of 15mm the reflect leghth was 15mm and the width was 3.09mm. The thru length standard is twice the length of the reflect therefore making it 30mm with a width of 3.09mm. After the reflect and thru were design, the line could be designed. The line length also has a standard of being a quater-wave length longer than the thru. This made the line length to be 44.07mm and the width was 3.09mm as well. Once all the values were enetered into thier respective HFSS design, a first round of simulations was conducted. When the simulations were completed, the results that were produced did not meet the criteria given in the lab instructions. This required some of the design parameters to ammended. The two parameters that had to be changed were the widths and the quater-wave length. The width was increased to 3.38mm which decraesed the impedance, making it closer to 50ohms. The quater-wave length was decreased to 13.8mm. Another parameter that needed to be changed was the width of the thru. At 3.37mm the S21 phase was -90degrees while at 3.38 it was 90degrees, so depending on which phase was desired, either could used. 

The second design was similar to the first one but there were some additional calculations. Using the same microstrip calculator, the width of the 50ohms line was calculated to be 3.105mm and the width of the 100ohm choke lines came out to be 0.723mm for a center frequency of 2.5GHz. The length of the 50ohm line was already given but the length of the chokes had to calculated. When the widths are calculated, the calculator calculates the effective quater-wavelength as well which for 100ohms was 17.79mm. In this design, the two choke lines had the same parameters. After the first simulation, the parameters had to be adjusted just like in the first design. This time the 50ohm width was increased to 3.22mm and the lengths of the chokes were also increased to 18.2mm for the bias line and 18mm for the ground line. The adjustment of the chokes helped center the low insertion loss at the center frequency.

## Procedure
For this lab, David ran through the calibration of both designs. First was the TRL kit. In order to create this particular kit, the reactance from the reflect line had to be converted to capaciatnce and then the coefficients from a third order polynomial had be calculated. This was done by exporting HFSS data to a csv and then it was implemented into a python code that did the conversion and calculated the coefficients. With the coefficents calculated, David entered them into the network anaylzer. Once the calibration was set, he calibrated the kit. He started by calibrating port 1 connected to the reflect and then port 2 to the reflect. Next was the thru and then the line. After each calibration the data was saved as a csv file so that it could be compared later.

In the second part was the lab, David calibrated the PIN diode switch. Similar to the first part, the device was calibrated with the diode in the "ON" and "OFF" stage. The data was saved into a csv file for comparsion to the simulation results. 

## Results and Discussion
![TRL Capacitance](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab5/TRL_Capcitance.png) <br>
![S21 Thru Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab5/S21_Thru_Magnitude.png) <br>
![S21 Thru Phasae](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab5/S21_Thru_Phase.png) <br>
![S21 Line Magnitude](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab5/S21_Line_Magnitude.png) <br>
![S21 Line Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab5/S21_Line_Phase.png) <br>
![S11 PIN Diode OFF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab5/S11_PIN_Diode_OFF.png)<br>
![S11 PIN Diode ON](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab5/S11_PIN_Diode_ON.png)<br>
![S21 PIN Diode OFF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab5/S21_PIN_Diode_OFF.png)<br>
![S21 PIN Diode ON](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/alonzo_barraza/Lab5/S21_PIN_Diode_ON.png)<br>


## Conclusion
The simulations and the measured data compared well to one another. The closest simulation-measurement result was with the PIN diode switch. Each result was the same but just offset from one another. As for the TRL kit, the data from the measurement might be in a diffrent scale because the graph shows a noisy figure while the simulated data is a smooth line.  

## Hindsight
After going through the lab, it would have been good to understand the use of PIN switch diode and the choke lines before hand. This would have helped understand the overall design and functionality of the device.

## Reflection
The most difficult part of this lab was just the fine tunning of the simulations because one small change sometimes gave different results that made sense but at other times they would not. However, once that was overcame it was rewarding to learn the beginning steps of the whole design and testing process.
