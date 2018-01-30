# Lab 7 Report
Francisco Espinal 

## Background
In this lab we constructed a Wilkinson Power divider and a phase shifter. A Wilkinson power divider can either split an input signal into two equal output signals or can combine two signals and shoot it in the opposite direction. A phase shifter does exactly what its called it shifts the phase angle of a input.    

## Design
We used a Z_0 = 50 ohms reference impedance on a 62mil thick FR4 (e_r=4.1, tan d = 0.01) substrate to support a frequency range of 1 GHz to 5 GHz.  With these design specification we were able to use an online calculator to find the dimensions needed for both devices. And to find the lengths of each line I use the following equation. 
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Labs/Lab3/Equation.png) <br>

## Procedure
To construct the Wilkinson power divider I started by calculating the impedance of each stub by using the equation (Z_0)Sqrt(2).  Then to get the physical lengths of the quarter wavelengths TL, I plugged in all of my given values and 90 degrees into the above equation. The resistor was 100 ohms, the formula used was 2(Z_0). It allows all three ports to be matched; it fully isolates the ports by dissipating power into heat.  From here I just plug my values into HFSS to get my simulated values in order to compare them to the measured values. 
To construct the phase shifter, we started by cut up a 50-ohm piece of cooper tape and placing it on a FR4 board to get a reference angle. We measured it using the network analyzer and recorded the data. Next we added more lines so we could achieve a 90-degree and 180-degree shift. The lengths of the lines were calculated with the same equation as above. 

|    |    Impedance (ohms)  | Width (mm) | Length (mm)|
| ----- |:-----:| :-----:|:------:|
|    Port 1   | 50 |  3.11| 0 |
|    Port 2|   70.1   | 1.67|17.3 |
|    Port 3  |   70.1   | 1.67| 17.3| 

## Results and Discussion

##### Wilkinson Power Divider
![Mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/WPD_S_Parameter_Plots.png) <br>
S32 shows that the ports are isolated.
S21, and S31 show that the power was split.  

![Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/WPD_Phase_Plot.png) <br>

![M_Mag](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/WPD_Matched_S_Parameter.png) <br>
S11, S22, and S33 show that the ports are matched.

![M_Phase](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/WPD_Matched_Phase_Plot.png) <br>


Both the simulated and measured results are very identical. There are just some variations from the sources of errors. For example loss associated with microstrip lines or calculation error. 


##### Phase Shifter

![S11_M](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/Phase_Shifter_S11_Magnitude_Plot.png) <br>]
S11 shows that they are matched.

![S11_P](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/Phase_Shifter_S11_Phase_Plot.png) <br>
S21 shows the power.

![S21_M](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/Phase_Shifter_S21_Magnitude_Polt.png) <br>
![S21_P](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/FAEspinal/Lab7/Final/Phase_Shifter_S21_Phase_Plot.png) <br>

We couldn’t get ours to work so our phase is very off from the target. 


## Conclusion
The simulations for the power divider ran as excepted but for some unknown reason our phase shifter was not working. A majority of the class had the same problem. We should’ve made some more modifications but we didn’t know what else to modify after we altered our stub lengths of the 180 phase shift side. It might have been the presence of the additional micro strip line, but I doubt it could have been that because my thru and thru2 are practically identical. Thru2 just has a steeper slope because of the coupling. It has more loss. Maybe another way to improve the phase shifter would be to cut one single strip of copper tape instead of multiple copper strips. This will require less soldering points, which is a good thing because I’m not good at soldering.  

## Hindsight
N/A

## Reflection
The lab was straightforward, no changes are recommended. 

