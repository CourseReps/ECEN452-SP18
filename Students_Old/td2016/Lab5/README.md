# Lab 5 Report
Thomas Darden

## Background
For this lab, we created a TRL kit and a RF PIN diode series switch. The TRL kit is to be designed to support a frequency range of 1 GHz to 5GHz and provide a 15mm reference plane beyond the SMA connectors conntected to an FR4 substrate. The lines will also have a 50 ohm reference impedance and the substrate shall be 62 mil thick. The PIN diode switch will utilize quarter-wave bias tees and shall have a center frequency of 2.5GHz. We should have a 10mm seperation from the 15mm reference planes set by the designed TRL calibration. Both devices will be tested in HFSS and designed in lab. We shall provide both results within this report.

## Design
Task 1: The first thing we are going to design is a TRL kit with a reference plane of 15mm.

Design Parameters:

Zo = 50 ohms

Reference Plane = 15mm

h = 62 mil = 1.5748mm

FR4 Er = 4.1

Frequency Range = 1GHz - 5GHz 

The first thing we must do is calculate the physical width of the microstrip lines. 
This measurement requires a specific design frequency within the middle of the range we wish to design our TRL kit at. We find the middle frequency to be:

F_Middle = (F_Low + F_High)/2 = (1GHz + 5GHz)/2 = 3GHz

From here we plug our design parameters and our F_Middle variable into a microstrip width calculator online to find the width to be 3.11mm.

Now that we know the widths of our lines, we must now find the lengths. 
We are given the Reference Length of 15mm.
The Through Length must be twice the Reference length to give us 15mm * 2 = 30mm.
The Line Length equals the Through Length plut the additional length of a quarter wavelength of the signal in the line. To find this additional length, we must also find the effective dielectric constant within the line to determine what the wavelength is. Luckily our microstrip calculator finds both of these values for us. We find the dielectric constant to be Eff = 3.17 and the quarter wavelength to be 14.04mm. Knowing this, the Line Length is found to be 44.04mm. 

This concludes the design portion of Task 1.

Task 2: For this task we must design a PIN Diode switch. 

Design Parameters:

fc = 2.5GHz

Reference Plane = 15mm

Zo = 50 ohms

FR4 Er = 4.1 

h = 62 mil


First we must find the width of the 50ohm line and the 100ohm lines. 

For the 50ohm line, we find:

width = 3.127mm

Eff = 3.157

For the 100ohm line, we find:

width = .7455mm

Eff = 2.878

We must now calculate the length of the quarter wavelength transmission lines for the bias tees. We can find this number by the following equation:

L_quarter = c/(4*Frequency*sqrt(Eff))

Using this equation, we find the length to be 17.68mm.

This concludes the design portion of task 2.

## Procedure
Task 1: 
We must simulate all three designs for the TRL kit in HFSS. We must make sure to use the de-embedding feature at each port. 

The TA will provide the measurements of the actual constructed TRL kit.

Task 2:
Simulate the design files in HFSS. Modify the the length of lines L_SCG and L_SCB to minimize the IL at the design frequency. Use these lengths and simulate the Series Switch file and simulate the file with the diode both ON and OFF.

The TA will provide the the measurements of the switch in both the ON and OFF positions. 

## Results and Discussion
Task 1:
From the simulations we performed in HFSS, we found the S11 parameters for all three designs to be the following:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab5/TRL_SPARA_S11_dB.png)<br>
It is shown that for the Reflect S11 parameter, we have a value close to 0. This means all power is being reflected, as expected.
For the other two designs, our reflection is minimized at our design frequency.

The S21 parameters, both simulated and measured, are shown in the following graph:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab5/TRL_SPARA_S21_dB.png)<br>
We can see that all of the S21 parameters are close to 0, showing minimized insertion loss. It is interesting to note though, that the value for the measured S21 parameters actually starts off around 1, which is impossible. This would imply that the lines are generating power, which is incorrect. This impossible measurement is an artifact of the network analyzer and should be assumed to be zero.

The phase of the S-Parameter excitations can be given by the following graphs:
For the simulated design:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab5/TRL_SPARA_S21_Phase.png)<br>
For the measured design:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab5/TRL_SPARA_S21_Phase_Measured.png)<br>
When initially simulated, we found that the line length of 44.04mm to be a little too long as our phase at 3GHz was a little above -90 degrees. When we altered this length to be 43.96mm, our phase was shown to be exactly -90 degrees, showing that our line length is correct. Our simulations and measurments appear to be in accordance with each other. 
From these parameters, we can also determine the phase velocity of the line and the delay of the line standard. 

phase_velocity = c/sqrt(Eff)

The above equation gives us a phase velocity of 1.701*10^8 m/s.

We can find the delay by the following:

delay = sqrt(Eff)*length/c

This gives us the delay of about .258ns.

From the output of the simulation files we recieved from HFSS, we can determine the function of the capactive open-circuit termination. This can be derived by using the reactance of the of the S11 parameter for the Reflect line.
Using this equation we can find the capacitance:

C=1/(2*pi*Frequency*Reactance)

Doing this allows us to find the capacitance and the 2nd order polynomial function. We used Excel to fit a curve to the data.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab5/Capacitance.png)<br>

For Task 2:
From the simulations performed in HFSS, we found that the lengths of the Bias Stub and the Ground Stub files needed to be slightly altered to minimize the insertion loss at 2.5GHz. We originally found the minimum loss to be above 2.5GHz, telling us we needed our lines to be a bit longer. Through trial and error, we found the optimal lengths to be L_SCG = 17.65mm and L_SCB = 18.25. These lengths gave us the following simulation graphs for the S-Parameters:
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab5/GroundStub.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab5/BiasStub.png)<br>
Using these lengths, we then plugged in all of our values into the PIN diode switch circuit. We then compared this data to the measured data obtained from the TA.
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab5/DiodeON.png)<br>
![image](https://github.com/CourseReps/ECEN452-Spring2016/blob/master/Students/td2016/Lab5/DiodeOFF.png)<br>
From the above graphs, we were able to see that our simulations were in accordance with the measured data. Our measured data actually did perform better than the simulations predicted by minimizing insertion loss more than expected. 

## Conclusion
From this lab I was able to design a TRL kit with relative accuracy and understand the effects that even the slightest change in length of a line can affect its response greatly. I also was able to learn how to obtain different measurements such as phase velocity and delay from the S-Parameters. From task 2 I was able to design a PIN diode series switch and see the effects it has on the propogation of high frequency signals.

## Hindsight
I wish I had known how to use HFSS more effectively before this lab began, as the simulations took me longer than they should have because I was not terribly sure how to use the program.

## Reflection
Overall, this lab was very straightforward and easy to understand. I like that we were first slowly introduced to the concept of how to design a simple microstip line for the network analyzer, as that will be important for future labs. A difficulty I encountered, again, was learning how to use HFSS. The templates the TA provided were very helpful though, as I did not have to create the designs from scratch.
