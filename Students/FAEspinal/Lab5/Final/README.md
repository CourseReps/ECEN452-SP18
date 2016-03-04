# Lab 5 Report
Francisco A. Espinal

## Background
In this lab we designed a TRL calibration kit and a RF PIN diode series switch. The TRL calibration kit is vital when you wish to measure and characterize RF and microwave devices. This calibration method is extremely accurate, and is important when measuring high frequency devices. The kit removes any error introduced to the phase and magnitude by the cables, connector, and etcetera. The RF Pin diode series switch controls RF power. It’s pretty much an on and off switch. It has a positive, negative, and un-doped regions. The un-doped region lowers the capacitance between P and N regions; this makes the time of the switch from conducting to non-conducting longer.  

## Design
To calculate the width and effective dielectric of each device I used an online calculator. (http://www1.sphere.ne.jp/i-lab/ilab/tool/ms_line_e.htm) Thickness used was 62mil. To get the actual physical lengths I used the equation below.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab3/Equation.png) <br>
I plug in the effective dielectric, frequency, and 90 for theta because we wanted the quarter wavelength. I preformed the same method of calculations for both designs.
 
|      | Width (mm) | E_eff | Physical Length (mm) | Frequency (GHz) | Z_0(ohm) | E_r | 
| -------- |:------:|:---:|:------:|:-------:|:-----:|:-------:| 
| Thru        |   3.091796    |  3.157436  |   30     |   3.0     |   50   |   4.1     |  
| Line          |   3.091796        |  3.157436    |   44.069    |   3 .0    |   50   |   4.1     |
| Reflect        |   3.091796        |  3.157436    |   15    |   3.0    |   50   |   4.1     |
| PIN Ground       |   0.723388    |  2.843427  |   17.79    |   2.5     |   100   |   4.1     |
| PIN Bias       |   0.723388        |  2.843427    |   17.79        |   2.5     |   100   |   4.1     |
| PIN       |   3.10568        |  3.142464    |   16.9233        |   2.5     |   50   |   4.1     |

Using the S-Parameters I calculated the phase velocity. And with the phase velocity and physical length, I calculated the delay. To find the phase velocity, we must first find the E_eff. Using the equation above. I plug in 91 for theta and 14.069mm.  Phase_Velocity= (3E8)/(sqrt(E_eff)). 

|    |    Values   |
| ----- |:-----:|
|    Phase Velocity   |   1.6624E8m/s   | 
|    E_eff   |   3.25657   | 
|    theta   |   91.4   | 
|   Physical Length    |   14.069mm | 
|   Delay    |   84.829E-12   | 
|   Delay(Python)    |   83.92425E-12   | 


Next I used python to calculate the polynomial equation for the capacitance using the reflect line 

|      | C_0 | C_1 | C_2 | C_3 | 
| -------- |:------:|:---:|:------:|:-------:| 
| Capacitance      |   20.77421    |  52507.6178  |   -14279.5670   |   1285.792612     |     
|       |   1 |  x |   x^2|   x^3    |     

The values for the Bias Tee

|   Bias Tee  |    Value   | 
| ----- |:-----:|
|    C_bias   |   47nF   | 
|    R_bias   |   510 ohm| 




## Procedure
I started with the TRL calibration kit, first I had to calculate the desired widths for the reflect, thru, and line. I did so using the given values and plugging them in to an online mircostrip calculator. Using the same calculator I solved for the effective dielectric. Now in order to get the physical lengths we need the design frequency of the calculation. Which was f_0= (F_L + F_H)/2. This gave me 3GHz. Using all this information I plug it into the equation from above. I plugged the acquired length into HFSS and ran the simulation. I de-embedded all the ports to get the required data. 

Next I calculated all the values for the PIN diode series switch. I did the calculations similar to the previous design. But this time I had to include width and lengths for the chokes. I obtained the needed data from the calculator (effective dielectric, width). Then I plug them all in to the above equation to find the lengths of each stub. I put these values into HFSS and ran the simulation. Once I check that the values were accurate. I plugged them into the PINSeriesSwitch so I could test it while it was ON or OFF. I observed and recorded the results.     


## Results and Discussion
The way I know my design was working was by comparing it to David’s measured values, and they were quite similar. There was very little difference in the overall scheme of the devices. The little difference could have come from hand calculations errors, in other words human error. My graphs look very weird but its because of the scale that they’re in.  






####TASK 1
![Line S21 Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab5/Final/Compared%20Plots/ECEN_452_Compared_Line_S21_Phase.png) <br>
![Line S21 dB](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab5/Final/Compared%20Plots/ECEN_452_Compared_Line_S21_dB.png) <br>
![Thru S21 Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab5/Final/Compared%20Plots/ECEN_452_Compared_Thru_S21_Phase.png) <br>
![Thru S21 dB](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab5/Final/Compared%20Plots/ECEN_452_Compared_Thru_S21_dB.png) <br>
![Capacitance](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab5/Final/Compared%20Plots/ECEN_452_TRL_Capacitance.png) <br>

####TASK 2
![PIN switch S11 OFF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab5/Final/Compared%20Plots/PIN_Switch_Compared_S11_dB_OFF.png) <br>
![PIN switch S11 ON](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab5/Final/Compared%20Plots/PIN_Switch_Compared_S11_dB_ON.png) <br>
![PIN switch S21 OFF](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab5/Final/Compared%20Plots/PIN_Switch_Compared_S21_dB_OFF.png) <br>
![PIN switch S11 ON](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab5/Final/Compared%20Plots/PIN_Switch_Compared_S21_dB_ON.png) <br>

See the raw text of the tutorials for an example.

## Conclusion
The lab did what it was intended to do; I became more familiar with TRL calibration kit, PIN diode switch, HFSS, and python. It’s a good intermediate step for designing devices. I learn how to calculate width, E_eff, and physical lengths for any transmission line. And how to get the polynomial model using the s-parameters of the reflect line. All of my simulated data was very similar to measured data. No unexpected challenges, the lab did a good job at explaining everything.



## Hindsight
Before starting the lab I wish I would've read up on the purpose of each design. It would've helped my interpretation of the graphs, and made it easier for me to grasp the overall concept of how the design functioned.   

## Reflection
The most challenging parts of the lab was trying to understand why the y-axis would change every time I ran a simulation, and the small adjustments needed to achieve the desired performance. It was very sensitive. The knowledge we gained through the step-by-step process the lab was conducted was the most rewarding part of the lab. It baby steps allowed me to focus more on the why of the design process. The lab was well written, and didn't confuse me at any point.  
