# Lab 7 Report
Sumana Pallampati

## Background
* Phase Shifter - A phase shifter changes the phase of the input signal. In this lab, we designed a 90 degrees and 180 degrees phase shifter. The design for a 90 degrees phase shifter simply involves adding a quarter wavelength. Similarly, the design for a 180 degrees phase shift involves adding a half wavelength to the thru line length.
* Wilkinson Power Divider - The input signal is equally divided into two output signals with the same phase. Moreover, all the ports of the divider are matched. This is possible due to the addition of a 100 ohm resistor. The resistor also isolates the port 2 and port 3 at the centre frequency.

## Design
* For the 90 degree phase shifter, a total of quarter wavelength is added i.e. at 3 GHz, the quarter wavelength is 14.0639 mm. Therefore, at each side of the thru length, 7.03195 mm is added. The impedance of the line is 50 ohm (w=3.1mm). 
* For the 180 degree phase shifter, a total of half wavelength is added i.e. at 3 GHz, the quarter wavelength is 28.1278 mm. Therefore, at each side of the thru length, 14.0639 mm is added. The impedance of the line is 50 ohm (w=3.1mm). 
* For the Wilkinson Power Divider, the impedance of the feed line is 50 ohms (w=3.1 mm). The length of the quarter wave obtained from online calculator is 17.36mm at 2.5 GHz. The impedance of the line is 70.7 ohms (sqrt(2)*Z0). Thus, the width of the line is 1.65 mm. The length of the line is increased to 24.3 mm to obtain a low S11, S22 and S33 at 2.5 GHz. The increase can be due to the circular geometry.

## Procedure
In the lab, we designed a phase shifter with copper tape. First, we measured the phase of the 50 ohm thru. The phase obtained is reference. Then we added a half wavelength to the thru and measured the phase (180 degrees phase shift). Next, we added a quarter wavelength to the thru and measured the phase (90 degrees phase shift).

For the wilkinson power divider, the length of the quarterwave was adjusted in HFSS to obtain a low S11, S22 and S33 at 2.5 GHz. This was compared to the milled version (measured data).

## Results and Discussion
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/Phase_Shifter_S11.png)<br>
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/Phase_Shifter_S11_Phase.png)<br>
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/Phase_Shifter_S21.png)<br>
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/Phase_Shifter_S21_Phase.png)<br>
The reference phase was obtained as -421.8 deg. With 90 degrees phase shift, the phase measured was -490 deg. Which implies the phase shifted by 68.2 deg. With 180 degrees phase shift, the phase measured was -599.8 deg. Which implies the phase shifted by 178 deg.

![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/S11_wilkinson.png) <br>
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/S21_wilkinson.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/S22_wilkinson.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/S31_wilkinson.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/S32_wilkinson.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/S33_wilkinson.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/Wilkinson_Phase_S11_S22_S33.png)
![Plot_Name](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/sumana-pallampati/Lab7/Wilkinson_Phase_S21_S31_S32.png)<br>
The measured and simulated results are close to each other.

## Conclusion
The design of a phase shifter is just adding electrical length depending on how much phase shift is required. The design of a power divider depends on the power split required. For the power splitter, the length of the quarterwave had to be increased substantially to obtain low S11, S22 and S33. 

## Hindsight
I understood the concept of phase shift with increase in length. The concept of power splitter also became clear after the lab. 

## Reflection
The soldering and copper tape gave some trouble during the lab as the copper tape would not stick to the substrate.
