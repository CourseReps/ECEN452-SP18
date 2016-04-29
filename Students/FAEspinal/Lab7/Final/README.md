# Lab 7 Report
Francisco Espinal 

## Background
In this lab we constructed a Wilkinson Power divider and a phase shifter. A Wilkinson power divider can either split an input signal into two equal output signals or can combine two signals and shoot it in the opposite direction. A phase shifter does exactly what its called it shifts the phase angle of a device.    

## Design
We used a Z_0 = 50 ohms reference impedance on a 62mil thick FR4 (e_r=4.1, tan d = 0.01) substrate to support a frequency range of 1 GHz to 5 GHz.  With these design specification we were able to use an online calculator to find the dimensions needed for both devices. And to find the lengths of each line I use the following equation. 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab3/Equation.png) <br>
## Procedure
To construct the Wilkinson power divider I started by calculating the impedance of each stub by using the equation (Z_0)Sqrt(2).  Then to get the physical lengths of the quarter wavelengths TL, I plugged in all of my given values and 90 degrees into the above equation. From here I just plug my values into HFSS to get my simulated values in order to compare them to the measured values. 
To construct the phase shifter, we started by cut up a 50-ohm piece of cooper tape and placing it on a FR4 board to get a reference angle. We measured it using the network analyzer and recorded the data. Next we added more lines so we could achieve a 90-degree and 180-degree shift. The lengths of the lines were calculated with the same equation as above. The resistor was 100 ohms, the formula used was 2(Z_0). 

|    |    Impedance (ohms)  | Width (mm) | Length (mm)|
| ----- |:-----:| :-----:|:------:|
|    Port 1   | 50 |  3.11| 0 |
|    Port 2|   70.1   | 1.67|17.3 |
|    Port 3  |   70.1   | 1.67| 17.3| 

## Results and Discussion

##### Wilkinson Power Divider
![Mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/WPD_S_Parameter_Plots.png) <br>
![Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/WPD_Phase_Plot.png) <br>
![M_Mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/WPD_Matched_S_Parameter.png) <br>
![M_Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/WPD_Matched_Phase_Plot.png) <br>



##### Phase Shifter

![S11_M](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/Phase_Shifter_S11_Magnitude_Plot.png) <br>
![S11_P](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/Phase_Shifter_S11_Phase_Plot.png) <br>
![S21_M](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/Phase_Shifter_S21_Magnitude_Polt.png) <br>
![S21_P](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/Phase_Shifter_S21_Phase_Plot.png) <br>


## Conclusion
The simulations for the power divider ran as excepted but for some unknown reason our phase shifter was not working. And it wasn’t just ours, a majority of the class had the same problem.  Why do you need a resistor in the power divider design? It allows all three ports to be matched, it fully isolates the ports by dissipating power into heat.  What modification did you have to make to the t-line widths/lengths to improve your simulated results? I didn't have to make any modifications. How did the presence of the additional micro strip line affect the thru measurements (difference between thru and thru2)? How could you improve the performance of your phase shifter if you had time to make a new one? In order to improve the phase shifter, I would cut one single strip of copper tape instead of multiple copper strips. This will require less soldering points, which is a good thing because im not good at soldering. 

## Hindsight
N/A

## Reflection
The lab was straight-forward, no changes are recommended. 

